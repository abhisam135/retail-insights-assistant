from langchain_core.messages import SystemMessage, HumanMessage
from app.utils.llm import get_llm

INSIGHT_PROMPT = """
You are a senior retail business analyst.
Convert structured query results into an executive business insight.
"""

def insight_agent(state):
    if "result" not in state:
        return state  # propagate error safely

    llm = get_llm()

    result = state["result"]
    question = state["question"]

    response = llm.invoke([
        SystemMessage(content=INSIGHT_PROMPT),
        HumanMessage(content=f"Question: {question}\nData: {result}")
    ])

    return {"answer": response.content}