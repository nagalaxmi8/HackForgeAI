from fastapi import FastAPI
from models.project import ProjectRequest

from agents.feasibility_agent import analyze_feasibility
from agents.architecture_agent import generate_architecture
from agents.task_agent import generate_tasks
from agents.roadmap_agent import generate_roadmap
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HackForge AI",
    description="Multi-Agent Hackathon Planning Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def home():
    return {
        "status": "success",
        "message": "HackForge AI Backend Running"
    }


@app.post("/analyze", tags=["Agents"])
def analyze_project(data: ProjectRequest):

    feasibility = analyze_feasibility(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )
    print("========== FEASIBILITY ==========")
    print(feasibility)

    architecture = generate_architecture(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )
    print("========== ARCHITECTURE ==========")
    print(architecture) 

    tasks = generate_tasks(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )
    print("========== TASKS ==========")
    print(tasks)
    roadmap = generate_roadmap(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )

    print("========== ROADMAP ==========")
    print(roadmap)  

    return {
        "status": "success",
        "data": {
            "feasibility": feasibility,
            "architecture": architecture,
            "tasks": tasks,
            "roadmap": roadmap
        }
    }