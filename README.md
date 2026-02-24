Retail Insights GenAI Assistant

Multi-agent GenAI assistant for retail sales analytics using LangGraph, DuckDB, and LLMs.

Overview

This project implements a conversational analytics and summarization assistant for retail sales datasets.
It supports:

Executive data summarization

Natural-language business queries

Multi-agent reasoning workflow

Dynamic CSV schema handling

Scalable architecture design

Features
Summarization Mode

Generates executive summary from dataset statistics.

Example output:

“Overall sales are concentrated in a few high-value segments, with strong contribution from select regions and product categories…”

Conversational Q&A Mode

Users can ask business questions such as:

Which category sells the most?

Total revenue in April 2022?

Top region by sales?

System converts natural language → SQL → insight.

Architecture

Multi-agent LangGraph workflow:

User Question
→ SQL Agent
→ Validation Agent
→ Execution Agent
→ Insight Agent

Summarization pipeline:

CSV
→ Metrics Engine
→ LLM Summary Agent

Tech Stack

Python

LangGraph

LangChain

DuckDB

Groq LLM (Llama-3)

Streamlit

Installation
git clone <your-repo-url>
cd retail-insights-assistant

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

Create .env:

GROQ_API_KEY=your_key
Run CLI
python main.py

Choose mode:

summary
qa
Run UI
streamlit run streamlit_app.py

Upload CSV → choose mode.

Multi-Agent Design

Agents implemented:

SQL Generation Agent

SQL Validation Agent

SQL Execution Agent

Insight Generation Agent

Summary Agent

Scalability Design (100GB+)

Proposed architecture:

Data lake (S3 / ADLS)

Parquet partitioning

DuckDB / Spark analytics

Warehouse layer (Snowflake/BigQuery)

RAG for reports

LLM orchestration with caching

Example Queries

Which size sells highest?

Total sales in March 2022

Top 5 categories

Author

Your Name
GenAI Assignment — Blend360