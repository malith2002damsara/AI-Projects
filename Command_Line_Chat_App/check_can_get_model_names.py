import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key=GEMINI_API_KEY)

print("Available Models:")
# ඔබට භාවිතා කළ හැකි සියලුම models ලැයිස්තුවක් ගනිමු
for model in client.models.list():
    print(model.name)