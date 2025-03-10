import os
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_community.chat_models import ChatOllama

load_dotenv()

class PostgresDatabase:
    def __init__(self):
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        db_name = os.getenv("POSTGRES_DB")
        model = os.getenv("OLLAMA_MODEL")

        uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
        self.db = SQLDatabase.from_uri(uri)
        self.llm = ChatOllama(model=model)
        self.chain = create_sql_query_chain(self.llm, self.db)

    def query(self, nl_question):
        sql_query = self.chain.invoke({"question": nl_question})
        print("Generated SQL Query:", sql_query)
        result = self.db.run(sql_query)
        return result

