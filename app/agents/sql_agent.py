from langchain_core.messages import SystemMessage, HumanMessage
from app.utils.llm import get_llm
from app.prompts.sql_prompt import SQL_SYSTEM_PROMPT_TEMPLATE


def get_schema(df):
    return ", ".join(df.columns)


def generate_sql_query(user_question: str, df) -> str:
    llm = get_llm()

    schema = get_schema(df)
    system_prompt = SQL_SYSTEM_PROMPT_TEMPLATE.format(schema=schema)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_question)
    ]

    response = llm.invoke(messages)

    sql = response.content.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


# LangGraph wrapper
def sql_agent(state):
    sql = generate_sql_query(state["question"], state["df"])
    return {"sql": sql}