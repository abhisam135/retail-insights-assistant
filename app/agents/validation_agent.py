def validation_agent(state):
    sql = state["sql"].lower()

    unsafe = ["delete", "drop", "update", "insert", "alter"]

    if any(word in sql for word in unsafe):
        return {"error": "Unsafe SQL detected"}

    if "select" not in sql:
        return {"error": "Invalid SQL generated"}

    return {"validated_sql": state["sql"]}