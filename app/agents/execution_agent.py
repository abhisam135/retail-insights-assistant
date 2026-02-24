def execution_agent(state):
    conn = state["conn"]
    sql = state["validated_sql"]

    try:
        result = conn.execute(sql).fetchdf()
    except Exception as e:
        return {"error": str(e)}

    if result.empty:
        return {"error": "Query returned no results"}

    return {"result": result.to_dict()}