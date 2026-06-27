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
You are a senior hackathon mentor.

Create a concise day-wise development roadmap for a hackathon MVP.

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
  "day_1": {{
    "subtitle": "",
    "goal": "",
    "tasks": [
      {{
        "title": "",
        "description": ""
      }}
    ]
  }},
  "day_2": {{
    "subtitle": "",
    "goal": "",
    "tasks": []
  }}
}}

Generate one object for EVERY day based on deadline_days.

If deadline_days = 5, return day_1 to day_5.
If deadline_days = 7, return day_1 to day_7.

IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT return markdown.
- Do NOT use ```json.
- Generate roadmap for ALL days.
- Adapt roadmap according to deadline_days.
- Include subtitle for every day.
- Include goal for every day.
- Maximum 3 tasks per day.
- Focus only on MVP development.
- Titles must be fewer than 6 words.
- Descriptions must contain only ONE short sentence.
- Descriptions should be 10–18 words.
- Goal should be 2–5 words.
- Subtitle should be 2–4 words.

OUTPUT LIMITS:

- Maximum 3 tasks per day.
- Title must be fewer than 6 words.
- Description must be only ONE short sentence.
- Description should be 10–18 words.
- Description should explain what the team will achieve.
- No time estimates.
- No team assignments.
- No long explanations.

Example:

{{
  "day_1": {{
    "subtitle": "Foundation & Setup",
    "goal": "Build Foundation",
    "tasks": [
      {{
        "title": "Project Setup",
        "description": "Initialize project structure and configure development environment."
      }},
      {{
        "title": "Backend APIs",
        "description": "Create FastAPI endpoints required for project analysis."
      }},
      {{
        "title": "Frontend UI",
        "description": "Build responsive interface for user input and results."
      }}
    ]
  }},

  "day_2": {{
    "subtitle": "Core Development",
    "goal": "Implement Features",
    "tasks": [
      {{
        "title": "Gemini Integration",
        "description": "Connect backend with Gemini API and validate responses."
      }},
      {{
        "title": "Testing",
        "description": "Verify API responses and fix major functional issues."
      }},
      {{
        "title": "UI Improvements",
        "description": "Improve styling and enhance user experience."
      }}
    ]
  }}
}}

Return only JSON.
"""

    response = ask_gemini(prompt)

    try:
        return parse_json_response(response)

    except Exception as e:
        return handle_json_error(e, response)