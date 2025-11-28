from app.core.supabase_client import supabase
from app.core.config import settings


def _get_latest_signal():
    resp = (
        supabase
        .table("signals")
        .select("*")
        .eq("hospital_id", settings.DEFAULT_HOSPITAL_ID)
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )
    if not resp.data:
        return None
    return resp.data[0]


def get_capacity_status():
    """
    Returns current vs simple predicted capacity for the main hospital.
    """
    latest = _get_latest_signal()
    if latest is None:
        return {"message": "No data yet. Wait for scheduler to generate signals."}

    # Example: baseline capacities – can move to 'hospitals' table
    baseline_beds = 2400
    baseline_icu = 350
    baseline_opd = 1200

    current = {
        "beds": latest["beds"],
        "icu": latest["icu"],
        "opd": latest["opd"]
    }

    # Very simple "prediction": +20% load for demo
    predicted = {
        "beds": int(latest["beds"] * 1.2),
        "icu": int(latest["icu"] * 1.25),
        "opd": int(latest["opd"] * 1.15),
    }

    utilization_now = {
        "beds": round(current["beds"] / baseline_beds * 100, 1),
        "icu": round(current["icu"] / baseline_icu * 100, 1),
        "opd": round(current["opd"] / baseline_opd * 100, 1),
    }

    utilization_peak = {
        "beds": round(predicted["beds"] / baseline_beds * 100, 1),
        "icu": round(predicted["icu"] / baseline_icu * 100, 1),
        "opd": round(predicted["opd"] / baseline_opd * 100, 1),
    }

    return {
        "current_load": current,
        "predicted_load": predicted,
        "current_utilization": utilization_now,
        "predicted_utilization": utilization_peak,
        "peak_time": "In ~4 hours (simulated)",  # static label for now
    }
