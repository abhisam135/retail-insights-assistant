from langchain_core.messages import SystemMessage, HumanMessage
from app.utils.llm import get_llm


def summary_agent(state):
    llm = get_llm()
    metrics = state["metrics"]

    system_prompt = """
You are a senior business analyst.

Generate a concise executive summary:
- Overall performance
- Growth trends
- Top & bottom performers
- Key risks or opportunities

Limit to 6-8 sentences.
"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=str(metrics))
    ])

    return {"summary": response.content}