from app.core.llm_client import run_gemini
from app.models.surge_predictor import _get_latest_signal, _basic_numeric_forecast
from app.services.sms_service import send_sms

def deflection_agent():
    latest = _get_latest_signal()
    if latest is None:
        return "No signals yet. Cannot generate deflection strategy."

    numeric = _basic_numeric_forecast(latest)

    prompt = f"""
    You are designing a patient deflection strategy for a crowded hospital.

    Data:
    - Current beds load: {latest['beds']}
    - Predicted peak beds load: {numeric['beds_peak']}
    - Current ICU load: {latest['icu']}
    - Predicted peak ICU load: {numeric['icu_peak']}

    Generate:
    - Which kinds of patients should be deflected (non-critical cases)
    - How many % of ED visits to deflect
    - Suggested messaging for patients (SMS) advising them on alternative days or hospitals.

    Respond with:
    - A short 3-bullet strategy
    - A sample SMS text.
    """

    return run_gemini(prompt)
# def deflection_agent():
#     ...
#     advice = run_gemini(prompt)

#     # Example: send SMS to a demo number
#     send_sms("+919999999999", advice)

#     return advice