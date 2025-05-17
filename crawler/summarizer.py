"""
    crawler/summarizer.py
    This module contains a function to summarize text using the Gemini API.
"""

from google import genai
from dotenv import load_dotenv
import os

def summarize(text: str, sentence_count: int = 3) -> str:
    """
    Summarize the given text using the LsaSummarizer.

    Inputs:
        text (str): The text to summarize.
        sentence_count (int): The number of sentences to include in the summary.

    Returns:
        str: The summarized text.
    """
    load_dotenv()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    prompt = f"Summarize the following text in {sentence_count} sentences:\n\n{text}"
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

    print(f"Response: {response.text}")

    return response.text