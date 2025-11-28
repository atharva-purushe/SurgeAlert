from app.core.llm_client import run_gemini
from app.models.surge_predictor import _get_latest_signal, _basic_numeric_forecast


def surge_explainer():
    latest = _get_latest_signal()
    if latest is None:
        return "No signals yet. Please wait for data generation."

    numeric = _basic_numeric_forecast(latest)

    prompt = f"""
    Explain to a hospital administrator in 3–4 sentences why a surge is expected.

    Data:
    - AQI: {numeric['aqi']}
    - Festival impact: {numeric['festival_impact']}
    - Days left for festival: {numeric['festival_days_left']}
    - Current beds load: {latest['beds']}
    - Predicted peak beds load: {numeric['beds_peak']}

    Be concise, professional, and actionable.
    """

    return run_gemini(prompt)
