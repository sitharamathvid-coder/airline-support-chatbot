# ✈️ Airline Customer Support System

An **AI-powered airline chatbot** that combines:

* 🔍 SQL-based flight data (PostgreSQL)
* 📘 RAG-based policy answers
* 🛡️ Guardrails for safe AI responses
* 🔄 n8n workflows for orchestration
* 💬 Streamlit UI for interaction

---

## 🚀 Features

* ✈️ Query real-time flight data
* 📘 Answer airline policies & FAQs
* 🧠 Smart query classification (SQL / RAG / Other)
* 🛡️ Input & output safety filtering
* 💬 Interactive chatbot UI

---

## 🏗️ Setup Guide

Follow the steps below to run the project locally:

---

### 1️⃣ Create GitHub Repository

Create a new repository and clone it locally.

---

### 2️⃣ Start GitHub Codespace (Optional)

You can use Codespaces for cloud development.

---

### 3️⃣ Install n8n

```bash
npm install n8n -g
```

---

### 4️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 5️⃣ Activate Environment & Install Dependencies

```bash
venv\Scripts\activate   # Windows
pip install llm-guard fastapi uvicorn streamlit requests psycopg2
```

---

### 6️⃣ Start PostgreSQL (Docker)

```bash
docker run -it -d -p 5432:5432 -e POSTGRES_PASSWORD=mypassword --name=postgrescont postgres:latest
```

👉 Ensure port **5432 is public**

---

### 7️⃣ Setup Database & Table

```bash
docker exec -it postgrescont psql -U postgres
```

```sql
SELECT datname FROM pg_database WHERE datistemplate = false;

CREATE DATABASE airlinedb;

\c airlinedb;

CREATE TABLE IF NOT EXISTS flights (
    id BIGINT PRIMARY KEY,
    flight_no TEXT NOT NULL,
    airline_code TEXT NOT NULL,
    airline_name TEXT NOT NULL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    departure_scheduled TIMESTAMP NOT NULL,
    arrival_scheduled TIMESTAMP NOT NULL,
    departure_date DATE GENERATED ALWAYS AS (departure_scheduled::date) STORED,
    departure_time TIME GENERATED ALWAYS AS (departure_scheduled::time) STORED,
    arrival_date DATE GENERATED ALWAYS AS (arrival_scheduled::date) STORED,
    arrival_time TIME GENERATED ALWAYS AS (arrival_scheduled::time) STORED,
    status TEXT CHECK (status IN ('On Time','Delayed','Cancelled')),
    delay_minutes INT DEFAULT 0,
    delay_reason TEXT DEFAULT '',
    terminal TEXT,
    gate TEXT,
    aircraft_type TEXT,
    seats_total INT,
    seats_booked INT,
    fare_inr INT
);
```

---

### 8️⃣ Insert Data

```bash
python add_data_to_db.py
```

---

### 9️⃣ Start Guardrail API

```bash
uvicorn guardrail_api:app --reload
```

---

### 🔟 Start n8n

```bash
n8n start
```

👉 Import your workflow
👉 Activate it

---

### 1️⃣1️⃣ Run Streamlit

```bash
streamlit run app.py
```

---

## 🔗 Webhook

```text
http://localhost:5678/webhook/airline-chat
```

---

## 🧪 Example Queries

### ✈️ SQL

* Show flights from BLR to PNQ
* Are there any flights from BOM to HYD?

### 📘 Policy

* What is baggage policy?
* Are power banks allowed?

### 🔴 Unsafe

* bomb attack

---

## 🧠 Tech Stack

* Streamlit
* n8n
* PostgreSQL
* OpenAI
* Pinecone
* FastAPI

---

## 👩‍💻 Author

**Sithara**
Generative AI & Agentic AI Learner

---

## 🎓 Project Note

> This project demonstrates how AI systems can integrate SQL, RAG, and guardrails into a real-world airline support assistant.
