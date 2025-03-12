import os
from dotenv import load_dotenv
from langchain_ollama.chat_models import ChatOllama

# Load environment variables from .env file
load_dotenv()

class OllamaLLM:
    def __init__(self, model_name):

        self.llm = ChatOllama(
            model=model_name
        )

    def get_llm(self):
        return self.llm
