from services.gemini_service import ask_gemini
from services.json_parser import parse_json_response
from services.error_handler import handle_json_error


def generate_tasks(
    project_idea,
    team_size,
    skills,
    deadline_days
):
    prompt = f"""
You are a hackathon project manager.

Project Idea:
{project_idea}

Team Size:
{team_size}

Skills:
{skills}

Deadline:
{deadline_days} days.

IMPORTANT:
- This is a hackathon MVP.
- Distribute work fairly among all team members.
- If team_size = 1, assign all work to one person.
- If team_size > 3, create additional roles when necessary.
- Tasks should be realistic and achievable.
- Avoid enterprise-level tasks.

Return ONLY valid JSON in this format:

{{
    "member_1": [],
    "member_2": [],
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