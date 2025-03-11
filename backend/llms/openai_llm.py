import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

class OpenAILLM:
    def __init__(self):
        self.llm = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            temperature=0.5,
            max_tokens=1000
        )

    def get_llm(self):
        return self.llm