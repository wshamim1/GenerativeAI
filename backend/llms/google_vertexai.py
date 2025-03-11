import os
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI

# Load environment variables from .env file
load_dotenv()

class GoogleVertexAILLM:
    def __init__(self):
        project_id = os.getenv('GOOGLE_PROJECT_ID')
        application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        model = os.getenv('GOOGLE_MODEL')

        if not project_id or not application_credentials or not model:
            raise ValueError("Missing one or more required environment variables: GOOGLE_PROJECT_ID, GOOGLE_APPLICATION_CREDENTIALS, GOOGLE_MODEL")

        self.llm = ChatVertexAI(
            project_id=project_id,
            location=application_credentials,
            model=model,
            max_tokens=1000,
            temperature=0
        )

    def get_llm(self):
        return self.llm