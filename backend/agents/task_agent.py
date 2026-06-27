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
You are a senior hackathon project manager.

Create a fair task allocation for this hackathon MVP.

Project Idea:
{project_idea}

Team Size:
{team_size}

Skills:
{skills}

Deadline:
{deadline_days} days.

Return ONLY valid JSON in this format:

{{
    "member_1": [],
    "member_2": [],
    "...": []
}}

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT use ```json.
- Assign work equally among team members.
- If team_size = 1, assign all work to one member.
- If team_size > 3, create member_4, member_5, etc.
- Focus only on MVP tasks.
- Avoid enterprise-level tasks.

OUTPUT LIMITS:

- Maximum 3 tasks per member.
- Every task must contain fewer than 8 words.
- Use short action phrases only.
- Do NOT include:
  - Day numbers
  - Time estimates
  - Explanations
  - Subtasks

Example:

{{
  "member_1": [
    "Setup React",
    "Build UI",
    "Connect APIs"
  ],
  "member_2": [
    "Create backend",
    "Gemini integration",
    "Testing"
  ],
  "member_3": [
    "Prompt tuning",
    "Deployment",
    "Presentation"
  ]
}}

Return only JSON.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)

    except Exception as e:
        return handle_json_error(e, response)