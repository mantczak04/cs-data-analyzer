from google import genai
from google.genai import types
import os


try:
    with open('db_context.txt', 'r') as f:
        CONTEXT = f.read()
except FileNotFoundError:
    CONTEXT = ""
    print('Error: LLM context file not found.')

SYSTEM_INSTRUCTION = """You are an expert SQL analyst.
    Your task is to write a single, executable SQL query for a DuckDB database based on a user's question.
    Use only the provided schema. DO NOT WRAP YOUR QUERY TO ```sql``` tags, or any other markdown formatting."""

llm_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sql(prompt: str) -> str:
    final_prompt = f"""{CONTEXT}
    Question: "{prompt}"
    SQL Query:"""

    try:
        response = llm_client.models.generate_content(
            model="gemini-2.5-pro",
            config = types.GenerateContentConfig(
                temperature=0.3,
                system_instruction=SYSTEM_INSTRUCTION
            ),
            contents=final_prompt
        )

        if not response.text:
            return "[ERROR] LLM failed to generate query."

        return response.text.strip()
    
    except Exception as e:
        print(f'[ERROR] An error occured with the LLM API: {e}')
        return f'LLM_API_ERROR: {e}'