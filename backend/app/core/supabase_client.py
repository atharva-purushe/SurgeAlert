from supabase import create_client, Client
from app.core.config import settings

if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
    raise RuntimeError("❌ SUPABASE_URL or SUPABASE_KEY not set in environment.")

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
