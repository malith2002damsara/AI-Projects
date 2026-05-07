import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key=GEMINI_API_KEY)

while True:

 question = input("\nUser: ")

 # 2. Loop එක නැවැත්වීමට ක්‍රමයක් (Exit condition)
 if question.lower() in ["exit", "quit", "bye"]:
        print("Gemini: Good bye!")
        break # Loop එකෙන් එළියට යන්න

    # හිස් ප්‍රශ්න යැවීම වැළැක්වීමට
 if not question.strip():
        continue

 try:
    response = client.models.generate_content(
        # මෙම මොඩල් එක භාවිතා කරන්න
        model="gemini-flash-latest", 
        
        contents= question,
        config=types.GenerateContentConfig(
            max_output_tokens=1000, # labena mximum output word count eka 
            # n = 1 unama labena responce gana wee.
            temperature=0.9 # emka 0 unama eka prompt ekata ekama responce eka labee
        )
    )
    print("Gemini:" +"  "+ response.text)

 except Exception as e:
    print(f"Error occurred: {e}")