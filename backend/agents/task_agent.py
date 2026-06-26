import json
from services.gemini_service import ask_gemini


def generate_tasks(
    project_idea,
    team_size,
    skills,
    deadline_days
):
    prompt = f"""
You are an expert hackathon mentor.

Project Idea:
{project_idea}

Team Size:
{team_size}

Skills:
{skills}

Deadline:
{deadline_days} days.

Divide the work among exactly {team_size} team members.

Return ONLY valid JSON:

{{
    "member_1": [],
    "member_2": [],
    "member_3": []
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