from services.gemini_service import ask_gemini
from services.json_parser import parse_json_response
from services.error_handler import handle_json_error


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

Create a realistic day-wise roadmap.

IMPORTANT:
- Adapt the roadmap to the number of days.
- If the deadline is short, prioritize MVP.
- If the deadline is long, include planning, testing, and polishing phases.
- Generate a roadmap for ALL days.

Return ONLY JSON.

Example:

{{
    "day_1": [],
    "day_2": [],
    "...": []
}}

No markdown.
Return only JSON.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)

    except Exception as e:
        return handle_json_error(e, response)