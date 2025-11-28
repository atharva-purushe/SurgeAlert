from app.core.llm_client import run_gemini
from app.models.surge_predictor import _get_latest_signal, _basic_numeric_forecast


def procurement_agent():
    latest = _get_latest_signal()
    if latest is None:
        return "No signals yet. Cannot generate procurement plan."

    numeric = _basic_numeric_forecast(latest)

    prompt = f"""
    You are the hospital procurement agent.

    Based on:
    - Current beds load: {latest['beds']}
    - Predicted peak beds load: {numeric['beds_peak']}
    - Current ICU load: {latest['icu']}
    - Predicted peak ICU load: {numeric['icu_peak']}
    - AQI: {numeric['aqi']} (respiratory cases likely)

    Recommend:
    - Quantities of oxygen cylinders
    - N95 masks
    - Nebulizers / ventilator kits
    - Critical drugs (e.g., bronchodilators)

    Format:
    - Bullet list of items + quantities
    - Short justification.
    """

    return run_gemini(prompt)
