

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

class AnthropicLLM:
    def __init__(self):
        self.llm = ChatAnthropic(
            api_key=os.getenv('ANTHROPIC_API_KEY'),
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            temperature=0
        )

    def get_llm(self):
        return self.llm
