from agents.feasibility_agent import analyze_feasibility

response = analyze_feasibility(
    "HackForge AI - Multi-Agent Platform that analyzes project ideas, generates architecture, allocates tasks, and creates development roadmaps.",
    3,
    ["Python", "React", "FastAPI", "Gemini"],
    3
)

print(response)