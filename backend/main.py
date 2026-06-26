from fastapi import FastAPI
from models.project import ProjectRequest
from agents.feasibility_agent import analyze_feasibility
from agents.architecture_agent import generate_architecture
from agents.task_agent import generate_tasks
from agents.roadmap_agent import generate_roadmap
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "HackForge AI Backend Running"
    }
@app.post("/analyze")
def analyze_project(data: ProjectRequest):

    feasibility = analyze_feasibility(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )

    architecture = generate_architecture(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )

    tasks = generate_tasks(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )

    roadmap = generate_roadmap(
        data.project_idea,
        data.team_size,
        data.skills,
        data.deadline_days
    )

    return {
        "feasibility": feasibility,
        "architecture": architecture,
        "tasks": tasks,
        "roadmap": roadmap
    }