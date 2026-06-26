from services.gemini_service import ask_gemini

response = ask_gemini(
    "Explain FastAPI in one sentence."
)

print(response)