from services.gemini_service import ask_gemini
from services.json_parser import parse_json_response
from services.error_handler import handle_json_error


def generate_architecture(
    project_idea,
    team_size,
    skills,
    deadline_days
):
    prompt = f"""
You are a senior software architect and hackathon mentor.

Design an MVP architecture for this hackathon project.

Project Idea:
{project_idea}

Team Size:
{team_size}

Skills:
{skills}

Deadline:
{deadline_days} days.

IMPORTANT:
- This is a hackathon MVP, not a production system.
- Prefer simple technologies and fast implementation.
- Prefer APIs over training custom ML models.
- Prefer monolithic architecture over microservices.
- Avoid unnecessary complexity.

Do NOT suggest:
- Training custom models
- Kubernetes
- Microservices
- Message queues
- Complex databases
- Docker unless absolutely necessary

Return ONLY valid JSON in this format:

{{
    "frontend": "",
    "backend": "",
    "database": "",
    "ai_model": "",
    "deployment": "",
    "flow": []
}}

Where:
- frontend = recommended frontend technology
- backend = recommended backend technology
- database = recommended database
- ai_model = recommended AI model/API
- deployment = recommended deployment method
- flow = step-by-step system flow.

No markdown.
Do not use ```json.
Return only JSON.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)

    except Exception as e:
        return handle_json_error(e, response)