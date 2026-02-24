# 🛍️ Retail Insights GenAI Assistant

**Multi-agent GenAI assistant for retail sales analytics using LangGraph, DuckDB, and LLMs**

---

## 📌 Overview

Retail Insights GenAI Assistant is a conversational analytics and executive-summarization system for retail sales datasets.

It enables business users to:

- Generate executive summaries from raw CSV data  
- Ask natural-language business questions  
- Automatically translate questions → SQL → insights  
- Analyze datasets with unknown schemas  
- Scale to large analytics architectures  

---

## ✨ Key Features

### 📊 Executive Summarization
Automatically generates business summaries from dataset statistics.

**Example output**

> Our company's overall performance has shown a steady growth trend, with a total of 128,975 records analyzed.  
> Key highlights include:
>
> • **Growth Trends:** The total sum of Amount has increased to $78,592,678.3, indicating growth in sales revenue.  
> • **Top Performers:** The most frequent categories include specific Order_IDs and a high occurrence of 'Shipped' status (77,804 times).  
> • **Bottom Performers:** The Sales_Channel category shows very low frequency for 'Non-Amazon'.  
> • **Risks & Opportunities:** A high number of cancelled orders (18,332) suggests fulfillment or customer satisfaction issues, while shipped orders indicate strong performance.
---

### 💬 Conversational Business Q&A
Ask natural language questions such as:

- Which category sells the most?  
- Total revenue in April 2022?  
- Top region by sales?  
- Which size performs best?  

System pipeline:

---

## 🧠 Multi-Agent Architecture

### Q&A Workflow (LangGraph)

<img width="186" height="236" alt="QA_workflow" src="https://github.com/user-attachments/assets/42118fa2-d3eb-49a2-9073-6ea5cdf88806" />


---

### Summarization Workflow

<img width="166" height="133" alt="Summary_workflow" src="https://github.com/user-attachments/assets/3c98f7b3-d05a-443e-9460-df3694bd4130" />


---

## 🖥️ Application Screenshots

### 🏠 Homepage (File Upload & Mode Selection)

<img width="900" alt="Homepage" src="https://github.com/user-attachments/assets/c3d46512-8c19-4e87-a998-2e8f68aa422c" />


---

### 📊 Executive Summary Output

<img width="900"  alt="Summary" src="https://github.com/user-attachments/assets/b1c5d23a-3b0b-4e3c-a3d0-ba965d5eebf3" />

 
---

### 💬 Conversational Q&A

<img width="900" alt="QA" src="https://github.com/user-attachments/assets/2c5d0057-a008-4d9d-83e4-7535d071c761" />


## 🏗️ Tech Stack

- Python  
- LangGraph  
- LangChain  
- DuckDB  
- Groq LLM (Llama-3)  
- Streamlit  

---

## 🚀 Installation

```bash
git clone https://github.com/abhisam135/retail-insights-assistant.git
cd retail-insights-assistant

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

Create .env file:
GROQ_API_KEY=your_key_here

Run CLI Mode
python main.py

Choose mode:
summary
qa

Run Streamlit UI
streamlit run streamlit_app.py
```
Upload CSV → Select mode → Generate insights.

## 🤖 Agents Implemented

* SQL Generation Agent → Converts natural language to SQL
* SQL Validation Agent → Ensures safe & valid SQL
* SQL Execution Agent → Runs query in DuckDB
* Insight Agent → Converts results to business insight
* Summary Agent → Generates executive summary

## 📈 Scalability Design (100GB+ Data)

Proposed production architecture:
* Data lake (S3 / ADLS)
* Parquet partitioning
* DuckDB / Spark analytics
* Warehouse (Snowflake / BigQuery)
* RAG for reports
* LLM orchestration with caching

## ❓ Example Questions
* Which size sells highest?
* Total sales in March 2022
* Top 5 categories
* Revenue by region

👨‍💻 Author

Abhishek

  


