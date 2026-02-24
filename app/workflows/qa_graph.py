from langgraph.graph import StateGraph, END
from typing import TypedDict

from app.agents.sql_agent import sql_agent
from app.agents.validation_agent import validation_agent
from app.agents.execution_agent import execution_agent
from app.agents.insight_agent import insight_agent


class QAState(TypedDict, total=False):
    question: str
    sql: str
    validated_sql: str
    result: dict
    answer: str
    conn: object
    error: str
    df: any


def has_error(state):
    return "error" in state


def build_qa_graph():
    workflow = StateGraph(QAState)

    workflow.add_node("sql", sql_agent)
    workflow.add_node("validate", validation_agent)
    workflow.add_node("execute", execution_agent)
    workflow.add_node("insight", insight_agent)

    workflow.set_entry_point("sql")

    workflow.add_edge("sql", "validate")

    workflow.add_conditional_edges(
        "validate",
        lambda s: "error" if has_error(s) else "ok",
        {"error": END, "ok": "execute"},
    )

    workflow.add_conditional_edges(
        "execute",
        lambda s: "error" if has_error(s) else "ok",
        {"error": END, "ok": "insight"},
    )

    workflow.add_edge("insight", END)

    return workflow.compile()