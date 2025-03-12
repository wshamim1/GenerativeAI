import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# Load environment variables from .env file
load_dotenv()

class MistralAILLM:
    def __init__(self):
        api_key = os.getenv('MISTRAL_API_KEY')

        if not api_key:
            raise ValueError("Missing required environment variable: MISTRAL_API_KEY")

        self.llm = ChatMistralAI(
            api_key=api_key,
            max_tokens=1000,
            temperature=0
        )

    def get_llm(self):
        return self.llm