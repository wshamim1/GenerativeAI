import os
from dotenv import load_dotenv
from databricks_langchain import ChatDatabricks

# Load environment variables from .env file
load_dotenv()

class DatabricksLLM:
    def __init__(self, model_name):
        api_key = os.getenv('DATABRICKS_TOKEN')
        url = os.getenv('DATABRICKS_HOST')
        model = os.getenv('DATABRICKS_MODEL')

        if not api_key or not url or not model:
            raise ValueError("Missing one or more required environment variables: DATABRICKS_TOKEN, DATABRICKS_HOST, DATABRICKS_MODEL")

        self.llm = ChatDatabricks(
            api_key=api_key,
            url=url,
            model=model_name,
            max_tokens=1000,
            temperature=0
        )

    def get_llm(self):
        return self.llm