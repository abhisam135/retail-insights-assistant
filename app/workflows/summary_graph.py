from langgraph.graph import StateGraph, END
from typing import TypedDict

class SummaryState(TypedDict):
    metrics: dict
    summary: str

def build_summary_graph(summary_agent):

    workflow = StateGraph(SummaryState)

    workflow.add_node("summarizer", summary_agent)

    workflow.set_entry_point("summarizer")
    workflow.add_edge("summarizer", END)

    return workflow.compile()