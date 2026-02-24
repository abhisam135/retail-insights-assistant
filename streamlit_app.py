import streamlit as st

from app.utils.preprocessing import load_and_clean_data
from app.utils.db import create_connection, load_dataframe_to_duckdb
from app.utils.metrics import compute_metrics

from app.workflows.summary_graph import build_summary_graph
from app.workflows.qa_graph import build_qa_graph
from app.agents.summary_agent import summary_agent


st.set_page_config(page_title="Retail Insights Assistant", layout="wide")

st.title("📊 Retail Insights Assistant")


# ---------- DATA LOAD ----------
@st.cache_data
def load_data(file):
    df = load_and_clean_data(file)
    return df


@st.cache_resource
def init_system(df):
    conn = create_connection()
    load_dataframe_to_duckdb(conn, df)

    summary_graph = build_summary_graph(summary_agent)
    qa_graph = build_qa_graph()

    return conn, summary_graph, qa_graph


# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    conn, summary_graph, qa_graph = init_system(df)

    mode = st.radio("Select Mode", ["Summarization", "Q&A"])

    # ---------- SUMMARIZATION ----------
    if mode == "Summarization":
        if st.button("Generate Executive Summary"):
            metrics = compute_metrics(df)

            if "error" in metrics:
                st.error(metrics["error"])
            else:
                result = summary_graph.invoke({
                    "metrics": metrics
                })

                st.subheader("Executive Summary")
                st.write(result["summary"])

    # ---------- QA ----------
    if mode == "Q&A":
        user_q = st.text_input("Ask a business question")

        if st.button("Get Answer") and user_q:
            result = qa_graph.invoke({
                "question": user_q,
                "conn": conn,
                "df": df   # ✅ REQUIRED for dynamic schema SQL agent
            })

            if "error" in result:
                st.error(result["error"])
            else:
                st.success(result["answer"])