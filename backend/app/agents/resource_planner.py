from app.core.llm_client import run_gemini
from app.models.surge_predictor import _get_latest_signal, _basic_numeric_forecast


def resource_planner():
    latest = _get_latest_signal()
    if latest is None:
        return "No signals yet. Cannot generate staffing plan."

    numeric = _basic_numeric_forecast(latest)

    prompt = f"""
    You are a hospital staffing planner.

    Based on:
    - Current beds load: {latest['beds']}
    - Predicted peak beds load: {numeric['beds_peak']}
    - Current ICU load: {latest['icu']}
    - Predicted peak ICU load: {numeric['icu_peak']}

    Generate:
    - Additional doctors needed (ED, ICU)
    - Additional nurses needed
    - Any recommended shift changes for the next 48 hours

    Respond in bullet points + one short summary paragraph.
    """

    return run_gemini(prompt)
