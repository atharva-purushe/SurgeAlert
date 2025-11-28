from fastapi import APIRouter
from app.agents.agent_orchestrator import run_all_agents

router = APIRouter()


@router.post("/run")
def run_agents():
    """
    Run all autonomous agents and return their recommended actions.
    """
    return run_all_agents()
