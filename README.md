# 🚀 HackForge AI

An AI-powered multi-agent platform that helps hackathon teams transform project ideas into actionable development plans.

HackForge AI analyzes a project idea and automatically generates:

* ✅ Feasibility Analysis
* 🏗️ System Architecture
* 👥 Team Task Allocation
* 📅 Development Roadmap

Built using **FastAPI**, **React**, and **Google Gemini API**.

---

# ✨ Features

## 🔍 Feasibility Agent

* Calculates project feasibility score
* Identifies complexity
* Lists pros and cons
* Provides recommendations
* Suggests MVP features

## 🏗️ Architecture Agent

* Recommends:

  * Frontend technology
  * Backend technology
  * Database
  * AI models/APIs
  * Deployment strategy
  * System flow

## 👥 Task Allocation Agent

* Distributes tasks among team members based on:

  * Team size
  * Skills
  * Project requirements

## 📅 Roadmap Agent

* Generates a day-wise development roadmap
* Adapts according to project deadline

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Vite
* CSS

## Backend

* Python
* FastAPI
* Uvicorn

## AI

* Google Gemini API

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
HackForgeAI
│
├── backend
│   ├── agents
│   ├── models
│   ├── services
│   └── main.py
│
├── frontend
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/nagalaxmi8/HackForgeAI.git
cd HackForgeAI
```

---

## Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run Backend:

```bash
cd backend
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# 📡 API Endpoint

## Analyze Project

**POST**

```text
/analyze
```

### Request Body

```json
{
  "project_idea": "AI-powered hackathon mentor",
  "team_size": 3,
  "skills": ["Python", "React", "FastAPI"],
  "deadline_days": 3
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "feasibility": {},
    "architecture": {},
    "tasks": {},
    "roadmap": {}
  }
}
```

---

# 🚀 Future Enhancements

* Project history
* Export reports as PDF
* Team collaboration features
* Multi-LLM support
* Architecture diagram generation
* Authentication system

---

# 👥 Team

Developed by the **HackForge AI Team** for hackathons and rapid project planning.

---

# 📄 License

This project is licensed under the MIT License.
