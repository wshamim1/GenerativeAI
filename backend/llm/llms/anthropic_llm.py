import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env file
load_dotenv()

class AnthropicLLM:
    def __init__(self, model_name):
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("Missing required environment variable: ANTHROPIC_API_KEY")

        self.llm = ChatAnthropic(
            api_key=api_key,
            model=model_name,
            max_tokens=1000,
            temperature=0
        )

    def get_llm(self):
        return self.llm