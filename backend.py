import os
from dotenv import load_dotenv
from google import genai

load_dotenv(".env")


def get_Client():
    api_key = os.getenv("GEMINI_API_KEY")

    print("API key loaded:", api_key is not None)

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    return genai.Client(api_key=api_key)


def get_gemini_response(client, user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        return response.text

    except Exception as e:
        import traceback
        traceback.print_exc()
        return str(e)