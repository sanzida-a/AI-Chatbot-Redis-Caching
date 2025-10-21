import asyncio
import os
import google.generativeai as genai

GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("❌ Missing GEMINI_API_KEY. Set it in .env or environment variables.")

genai.configure(api_key=GENAI_API_KEY)
MODEL_NAME = "gemini-2.5-flash"



    
async def generate_ai_response(query: str) -> str:
    """
    Calls the Gemini API asynchronously and returns text.
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: genai.GenerativeModel(MODEL_NAME).generate_content(query)
    )
    return response.text.strip() if response and response.text else "No response generated."
