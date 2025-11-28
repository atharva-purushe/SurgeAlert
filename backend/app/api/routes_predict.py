from fastapi import APIRouter
from app.models.surge_predictor import generate_surge_prediction

router = APIRouter()


@router.get("/")
def predict_surge():
    """
    Returns surge risk, time to peak, peak load and explanation.
    """
    return generate_surge_prediction()
