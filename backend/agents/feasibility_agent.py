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

Evaluate this project ONLY as a Hackathon MVP (Proof of Concept).

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
    "score": 0,
    "complexity": "",
    "pros": [],
    "cons": [],
    "recommendation": "",
    "mvp_features": []
}}

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT use ```json.
- Do NOT explain your reasoning.
- Assume only an MVP needs to be built.
- Evaluate ONLY for a hackathon.

OUTPUT LIMITS:

- score: Integer between 0 and 100.
- complexity: One word only (Low, Medium, High).
- pros: Maximum 3 points.
- cons: Maximum 3 points.
- mvp_features: Maximum 5 features.
- recommendation: Maximum 2 short sentences.

WRITING RULES:

- Every bullet must contain fewer than 10 words.
- Keep every sentence concise.
- Avoid paragraphs.
- Avoid repetition.
- Use simple language.

Scoring Guide:

90-100 : Easily achievable MVP.
70-89 : Achievable with planning.
50-69 : Reduce scope.
30-49 : Very difficult.
0-29 : Not realistic.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)
    except Exception as e:
        return handle_json_error(e, response)