from fastapi import APIRouter, Query
from app.core.supabase_client import supabase

router = APIRouter()

@router.get("/")
def get_signals(limit: int = Query(100, ge=1, le=500)):
    resp = (
        supabase
        .table("signals")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return resp.data
