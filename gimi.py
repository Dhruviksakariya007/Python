import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    """
    Gets a response from the Gemini AI model.

    Args:
        input_text: The user's input text.

    Returns:
        The response from the Gemini AI model.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash") 
        response = model.generate_content([input_text])
        return response.text
    except Exception as e:
        print(f"Error interacting with Gemini AI: {e}")
        return "An error occurred while processing your request."

if __name__ == "__main__":
    while True:
        user_input = input("Enter your question or request: ")
        if user_input.lower() == "exit":
            break

        response = get_gemini_response(user_input)
        print(response)