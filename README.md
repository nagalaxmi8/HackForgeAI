# HackForge AI – Autonomous Project Feasibility & Execution Planner

An AI-powered multi-agent platform that helps hackathon teams transform project ideas into structured and actionable execution plans.

---

# 👥 Team Details

**Team Name: AgentForge

**Team Members**
- Bhukya Eswari
- Darnasi Nagalakshmi
- Kathari Krishna Pramoditha

**Hackathon**
XLVentures.AI – Agentic AI Hackathon

---

# 📌 Project Overview

HackForge AI is an AI-powered multi-agent platform designed to simplify project planning for hackathons, student projects, and rapid software development.

Instead of spending hours discussing feasibility, selecting technologies, assigning tasks, and creating execution plans, users simply provide basic project information such as the project idea, team size, technical skills, and project deadline.

The platform leverages multiple AI agents powered by Google Gemini API to automatically generate:

- ✅ Project Feasibility Analysis
- 🏗️ Recommended Software Architecture
- 👥 Intelligent Team Task Allocation
- 📅 Development Roadmap
- ⚠️ Risk Analysis and Recommendations

By automating the planning phase, HackForge AI enables teams to focus on implementation, improving productivity and increasing the chances of successful project completion.

---

# ✨ Features

## 📊 Feasibility Analysis Agent

- Calculates project feasibility score
- Estimates project complexity
- Lists advantages and challenges
- Suggests MVP scope
- Provides implementation recommendations

---

## 🏗️ Architecture Recommendation Agent

Automatically recommends:

- Frontend technologies
- Backend technologies
- Database
- AI Model / APIs
- Deployment strategy
- Overall system architecture

---

## 👥 Task Allocation Agent

Distributes project responsibilities based on:

- Team size
- Technical skills
- Project requirements

Generates balanced work allocation for all members.

---

## 📅 Roadmap Generation Agent

Creates:

- Day-wise implementation roadmap
- Development milestones
- Feature prioritization
- Suggested execution timeline

---

## ⚠️ Risk Analysis Agent

Identifies:

- Technical risks
- Timeline risks
- Skill gaps
- Project dependencies

Provides mitigation recommendations.

---

# 🛠 Technology Stack

## Frontend

- React.js
- Vite
- CSS3
- Axios
- React Router DOM
- Lucide React
- React Icons

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn
- Python Dotenv

## AI & APIs

- Google Gemini 2.5 Flash API

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
HackForgeAI
│
├── backend
│   ├── agents
│   ├── models
│   ├── services
│   ├── prompts
│   └── main.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔗 GitHub Repository

Repository:

**https://github.com/Pramoditha1712/HackForgeAI**

Clone the repository:

```bash
git clone https://github.com/Pramoditha1712/HackForgeAI.git
cd HackForgeAI
```

---

# ⚙️ Setup Instructions

## Prerequisites

Install the following software before running the project:

- Python 3.10 or above
- Node.js v18 or above
- npm
- Git
- Google Gemini API Key

---

## Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the backend folder:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Install Axios:

```bash
npm install axios
```

Install React Router DOM:

```bash
npm install react-router-dom
```

Install Lucide React:

```bash
npm install lucide-react
```

Install React Icons:

```bash
npm install react-icons
```

Run frontend:

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# ▶️ Running the Application

1. Start the backend server.

```bash
uvicorn main:app --reload
```

2. Start the frontend.

```bash
npm run dev
```

3. Open:

```
http://localhost:5173
```

4. Enter:

- Project Idea
- Team Size
- Technical Skills
- Project Deadline

5. Click **Generate AI Plan**.

The platform will generate:

- Feasibility Analysis
- Recommended Software Architecture
- Team Task Allocation
- Development Roadmap
- Risk Analysis

---

# 📡 API Endpoint

## Analyze Project

**POST**

```
/analyze
```

### Sample Request

```json
{
  "project_idea": "AI-powered hackathon mentor",
  "team_size": 3,
  "skills": [
    "Python",
    "React",
    "FastAPI"
  ],
  "deadline_days": 3
}
```

### Sample Response

```json
{
  "status": "success",
  "data": {
    "feasibility": {},
    "architecture": {},
    "tasks": {},
    "roadmap": {},
    "risks": {}
  }
}
```

---

# 📝 Additional Notes

- Ensure a valid Google Gemini API key is added to the `.env` file before starting the backend.
- Both frontend and backend servers must be running simultaneously.
- This project is developed as an MVP for the XLVentures.AI Agentic AI Hackathon.
- The architecture is modular, making it easy to extend with additional AI agents and new planning capabilities.

---

# 🚀 Future Enhancements

- User Authentication
- Project History
- Team Collaboration Workspace
- Export Reports as PDF
- GitHub Integration
- Multi-LLM Support
- Automatic Architecture Diagram Generation
- Cloud Deployment Support

---

# 👨‍💻 Developed By

**Team AgentForge**

Developed for the **XLVentures.AI Agentic AI Hackathon**.