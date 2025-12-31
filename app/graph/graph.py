from langgraph.graph import StateGraph, END
from app.graph.state import InfraState

from app.graph.nodes.intent import intent_agent
from app.graph.nodes.planner import planner_agent
from app.graph.nodes.generator import playbook_generator
from app.graph.nodes.validator import policy_validator
from app.graph.nodes.dry_run import dry_run_agent
from app.graph.nodes.executor import executor_agent
from app.graph.nodes.verify import verify_agent

def build_graph():
    g = StateGraph(InfraState)

    g.add_node("intent", intent_agent)
    g.add_node("plan", planner_agent)
    g.add_node("generate", playbook_generator)
    g.add_node("validate", policy_validator)
    g.add_node("dry_run", dry_run_agent)
    g.add_node("execute", executor_agent)
    g.add_node("verify", verify_agent)

    g.set_entry_point("intent")

    g.add_edge("intent", "plan")
    g.add_edge("plan", "generate")
    g.add_edge("generate", "validate")

    g.add_conditional_edges(
        "validate",
        lambda s: "generate" if s["validation_errors"] else "dry_run"
    )

    g.add_edge("dry_run", "execute")
    g.add_edge("execute", "verify")
    g.add_edge("verify", END)

    return g.compile()

