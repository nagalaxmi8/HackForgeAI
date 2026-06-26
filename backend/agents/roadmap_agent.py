import json
from services.gemini_service import ask_gemini


def generate_roadmap(
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

Create a day-wise roadmap.

Return ONLY valid JSON:

{{
    "day_1": [],
    "day_2": [],
    "day_3": []
}}

Do not return markdown.
Do not use ```json.
Return only JSON.
"""

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)
    except Exception:
        return {
            "error": "Invalid JSON from Gemini",
            "raw_response": response
        }