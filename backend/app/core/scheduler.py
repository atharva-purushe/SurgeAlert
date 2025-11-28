from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger

from app.core.supabase_client import supabase
from app.core.config import settings
from app.models.signal_generator import generate_full_signal_packet

scheduler = BackgroundScheduler()


def generate_and_push_signals():
    """Generate new signals and push to Supabase."""
    try:
        packet = generate_full_signal_packet(hospital_id=settings.DEFAULT_HOSPITAL_ID)
        # Map packet to columns of 'signals' table
        insert_payload = {
    "hospital_id": packet["hospital_id"],
    "pm25": packet["pm25"],
    "pm10": packet["pm10"],
    "aqi": packet["aqi"],
    "beds": packet["beds"],
    "icu": packet["icu"],
    "opd": packet["opd"],
    "festival_days_left": packet["festival_days_left"],
    "festival_impact": packet["festival_impact"],
    "mobility_transit": packet["mobility_transit"],
    "mobility_retail": packet["mobility_retail"],
    "mobility_workplace": packet["mobility_workplace"],
}

        supabase.table("signals").insert(insert_payload).execute()
        logger.info(f"📡 Signals pushed to Supabase: {insert_payload}")
    except Exception as e:
        logger.error(f"Error in generate_and_push_signals: {e}")


def start_scheduler():
    # Every 15 seconds for demo; change to minutes in real use
    scheduler.add_job(generate_and_push_signals, "interval", seconds=15)
    scheduler.start()
