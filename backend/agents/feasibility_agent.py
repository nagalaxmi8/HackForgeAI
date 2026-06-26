from services.gemini_service import ask_gemini
from services.json_parser import parse_json_response
from services.error_handler import handle_json_error


def analyze_feasibility(
    project_idea,
    team_size,
    skills,
    deadline_days
):
    prompt = f"""
You are a senior hackathon mentor.

Evaluate this project ONLY as a hackathon MVP (Proof of Concept).

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
    "score": 0,
    "complexity": "",
    "pros": [],
    "cons": [],
    "recommendation": "",
    "mvp_features": []
}}

IMPORTANT RULES:
- score MUST be an integer between 0 and 100.
- Do NOT return scores like 7 or 8.
- Example scores: 75, 60, 90.
- Assume only an MVP needs to be built.
- Recommendations must be practical.
- Suggest only features that can realistically be built within the deadline.
- If the project is related to hackathon planning, project management, or agentic AI systems, evaluate it in that context.
- Do not assume the project is a Government Tender platform unless explicitly mentioned.
- No markdown.
- Do not use ```json.
- Return only JSON.

Scoring Guide:
90-100 : Easily achievable MVP.
70-89 : Achievable with good planning.
50-69 : Achievable if scope is reduced.
30-49 : Very difficult.
0-29 : Not realistic.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)
    except Exception as e:
        return handle_json_error(e, response)