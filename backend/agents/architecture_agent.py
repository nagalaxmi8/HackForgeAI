import json
from services.gemini_service import ask_gemini


def generate_architecture(
    project_idea,
    team_size,
    skills,
    deadline_days
):
    prompt = f"""
You are an expert software architect.

Project Idea:
{project_idea}

Team Size:
{team_size}

Skills:
{skills}

Deadline:
{deadline_days} days.

Suggest the best architecture for an MVP hackathon project.

Return ONLY valid JSON in this format:

{{
    "frontend": "",
    "backend": "",
    "database": "",
    "ai_model": "",
    "deployment": "",
    "architecture": []
}}

Do not return markdown.
Return only JSON.
"""

    response = ask_gemini(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {
            "error": "Invalid JSON from Gemini",
            "raw_response": response
        }