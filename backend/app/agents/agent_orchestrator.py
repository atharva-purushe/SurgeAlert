from app.agents.surge_explainer import surge_explainer
from app.agents.resource_planner import resource_planner
from app.agents.procurement_agent import procurement_agent
from app.agents.deflection_agent import deflection_agent


def run_all_agents():
    return {
        "surge_explainer": surge_explainer(),
        "resource_planner": resource_planner(),
        "procurement": procurement_agent(),
        "deflection": deflection_agent(),
    }
