from app.core.llm_client import run_gemini
from app.core.supabase_client import supabase


def respond_to_patient(message: str) -> str:
    """
    Very simple router bot – reads the patient message and suggests a hospital.
    For now, we just hardcode 2 hospitals and use Gemini to choose.
    """

    # You can later fetch this from Supabase 'hospitals' table
    hospitals = [
        {"name": "AIIMS Delhi", "distance_km": 4.2, "wait_min": 45, "load": "HIGH"},
        {"name": "Apollo Hospital", "distance_km": 5.1, "wait_min": 20, "load": "MEDIUM"},
    ]

    prompt = f"""
    A patient says: "{message}"

    You have the following hospitals:
    1) {hospitals[0]['name']} – {hospitals[0]['distance_km']} km away, wait {hospitals[0]['wait_min']} min, load {hospitals[0]['load']}
    2) {hospitals[1]['name']} – {hospitals[1]['distance_km']} km away, wait {hospitals[1]['wait_min']} min, load {hospitals[1]['load']}

    Pick ONE hospital recommendation.
    Reply in this format, short and clear:

    "🏥 <Hospital Name>
     📍 <distance> km away
     ⏱ Wait: <X> minutes
     🟢 Status: <Short status line>"

    Also add one line: "If symptoms worsen, go to the nearest emergency department immediately."
    """

    return run_gemini(prompt)
