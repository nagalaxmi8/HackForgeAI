from agents.architecture_agent import generate_architecture

response = generate_architecture(
    "AI system that classifies tenders into categories and summarizes them",
    3,
    ["Python", "React", "ML"],
    3
)

print(response)