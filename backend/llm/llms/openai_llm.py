import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

class OpenAILLM:
    def __init__(self, model_name):
        api_key = os.getenv('OPENAI_API_KEY')
        print(api_key)
        print("-----")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        
        self.llm = ChatOpenAI(
            api_key=api_key,
            model=model_name,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

    def get_llm(self):
        return self.llm