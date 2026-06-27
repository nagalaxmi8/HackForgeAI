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

Design a simple MVP architecture for this hackathon project.

Project Idea:
{project_idea}

Team Size:
{team_size}

Skills:
{skills}

Deadline:
{deadline_days} days.

Return ONLY valid JSON in this exact format:

{{
    "frontend": "",
    "backend": "",
    "database": "",
    "ai_model": "",
    "deployment": "",
    "flow": []
}}

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT use ```json.
- Design ONLY for a hackathon MVP.
- Prefer simple technologies.
- Prefer APIs over training custom models.
- Prefer monolithic architecture.
- Avoid unnecessary complexity.
- Do NOT recommend Kubernetes, Microservices, Docker, or Message Queues.

OUTPUT LIMITS:

- frontend: One technology only.
- backend: One technology only.
- database: One technology only.
- ai_model: One model or API only.
- deployment: One platform only.
- flow: Maximum 5 steps.

FLOW RULES:

- Each step must contain fewer than 5 words.
- Keep steps simple.
- Example:
  [
    "User Input",
    "React UI",
    "FastAPI",
    "Gemini API",
    "Results"
  ]

Return only JSON.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)

    except Exception as e:
        return handle_json_error(e, response)