import os
import google.generativeai as genai
from app.core.config import settings

if not settings.GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not set in environment.")

genai.configure(api_key=settings.GEMINI_API_KEY)


def get_gemini_model():
    # Can switch to other models here if needed
    return genai.GenerativeModel("gemini-2.0-flash-lite")


def run_gemini(prompt: str) -> str:
    """Simple wrapper for Gemini text generation."""
    try:
        model = get_gemini_model()
        resp = model.generate_content(prompt)
        return resp.text or ""
    except Exception as e:
        # Fail gracefully – backend should not crash
        return f"(Gemini error: {e})"
