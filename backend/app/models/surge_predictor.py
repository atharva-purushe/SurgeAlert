from app.core.supabase_client import supabase
from app.core.config import settings
from app.core.llm_client import run_gemini


# -------------------------------------------------
# Fetch latest signal safely
# -------------------------------------------------
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

    # DEBUG LOG – prints in backend terminal
    print("LATEST SIGNAL ROW:", resp.data)

    if not resp.data:
        return None

    return resp.data[0]


# -------------------------------------------------
# Safe getter helper (no more KeyErrors)
# -------------------------------------------------
def _safe(signal, key, default=0):
    return signal[key] if key in signal else default


# -------------------------------------------------
# Minimal numeric forecaster with safe access
# -------------------------------------------------
def _basic_numeric_forecast(signal):
    """
    Uses AQI + festival impact to create a surge factor.
    Automatically handles missing values.
    """

    aqi = _safe(signal, "aqi", 200)
    festival_impact = float(_safe(signal, "festival_impact", 0.1))

    # Simple severity model
    severity = max(0.0, (aqi - 200) / 200.0)
    surge_factor = 1.0 + (severity * 0.5) + (festival_impact * 0.5)

    beds = _safe(signal, "beds", 500)
    icu = _safe(signal, "icu", 80)
    opd = _safe(signal, "opd", 500)

    beds_peak = int(beds * surge_factor)
    icu_peak = int(icu * (1.0 + severity * 0.7))
    opd_peak = int(opd * (1.0 + festival_impact * 0.8))

    return {
        "beds_peak": beds_peak,
        "icu_peak": icu_peak,
        "opd_peak": opd_peak,
        "surge_factor": round(surge_factor, 2),
        "aqi": aqi,
        "festival_impact": festival_impact,
        "festival_days_left": _safe(signal, "festival_days_left", 3),
        "beds": beds,
        "icu": icu,
        "opd": opd,
    }


# -------------------------------------------------
# MAIN SURGE PREDICTION LOGIC
# -------------------------------------------------
def generate_surge_prediction():
    latest = _get_latest_signal()

    if latest is None:
        return {"error": "No signals found. Wait for scheduler to generate data."}

    numeric = _basic_numeric_forecast(latest)

    # LLM prompt
    prompt = f"""
    You are SurgeShield AI.

    Hospital signals:
    - AQI: {numeric['aqi']}
    - Current beds load: {numeric['beds']}
    - Predicted peak beds load: {numeric['beds_peak']}
    - Current ICU load: {numeric['icu']}
    - Predicted peak ICU load: {numeric['icu_peak']}
    - Current OPD visits: {numeric['opd']}
    - Predicted peak OPD visits: {numeric['opd_peak']}
    - Festival impact score: {numeric['festival_impact']}
    - Days left for festival: {numeric['festival_days_left']}

    Based on this, respond with:
    1. Surge risk level (Green / Yellow / Orange / Red / Black)
    2. Time to peak surge (approx days & hours)
    3. Peak load (%) compared to normal
    4. Top 4 surge drivers + % contribution
    5. 3–4 line guidance for hospital admin.
    """

    explanation = run_gemini(prompt)

    return {
        "numeric_prediction": numeric,
        "llm_explanation": explanation
    }
