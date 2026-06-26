from agents.roadmap_agent import generate_roadmap

response = generate_roadmap(
    "AI system that classifies tenders into categories and summarizes them",
    3,
    ["Python", "React", "ML"],
    3
)

print(response)