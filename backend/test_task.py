from agents.task_agent import generate_tasks

response = generate_tasks(
    "AI system that classifies tenders into categories and summarizes them",
    3,
    ["Python", "React", "ML"],
    3
)

print(response)