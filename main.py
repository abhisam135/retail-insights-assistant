from app.utils.preprocessing import load_and_clean_data
from app.utils.db import create_connection, load_dataframe_to_duckdb

from app.utils.metrics import compute_metrics
from app.agents.summary_agent import summary_agent
from app.workflows.summary_graph import build_summary_graph
from app.workflows.qa_graph import build_qa_graph


DATA_PATH = "data/sales_data.csv"


def initialize_data():
    """Load, preprocess, and register data once."""
    df = load_and_clean_data(DATA_PATH)

    conn = create_connection()
    load_dataframe_to_duckdb(conn, df)

    return df, conn


# ---------- MODE 1: SUMMARIZATION ----------
def run_summary(df):
    
    metrics = compute_metrics(df)

    graph = build_summary_graph(summary_agent)
    result = graph.invoke({"metrics": metrics})

    print("\n=== EXECUTIVE SUMMARY ===\n")
    print(result["summary"])


# ---------- MODE 2: Q&A ----------
def run_qa(conn, df):
    graph = build_qa_graph()

    while True:
        q = input("\nAsk a question (or 'exit'): ")

        if q.lower() == "exit":
            break

        result = graph.invoke({
            "question": q,
            "conn": conn,
            "df": df 
        })

        if "error" in result:
            print("Error:", result["error"])
        else:
            print("\nAnswer:")
            print(result["answer"])


def main():
    df, conn = initialize_data()

    mode = input("Choose mode (summary / qa): ").strip().lower()

    if mode == "summary":
        run_summary(df)
    elif mode == "qa":
        run_qa(conn, df)
    else:
        print("Invalid mode. Choose 'summary' or 'qa'.")


if __name__ == "__main__":
    main()