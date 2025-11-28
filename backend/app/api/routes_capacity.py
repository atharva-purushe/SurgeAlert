from fastapi import APIRouter
from app.models.capacity_model import get_capacity_status

router = APIRouter()


@router.get("/")
def capacity_overview():
    """
    Returns current vs predicted capacity & utilization.
    """
    return get_capacity_status()
