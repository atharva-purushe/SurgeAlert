from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.router_bot import respond_to_patient

router = APIRouter()


class RouterBotRequest(BaseModel):
    message: str


@router.post("/ask")
def ask_routerbot(payload: RouterBotRequest):
    """
    Patient side query: 'Where should I go right now?'
    """
    reply = respond_to_patient(payload.message)
    return {"reply": reply}
