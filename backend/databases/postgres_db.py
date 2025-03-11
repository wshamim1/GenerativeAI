import os
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase

load_dotenv()

class PostgresDatabase:
    def __init__(self):
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        db_name = os.getenv("POSTGRES_DB")

        uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
        self.db = SQLDatabase.from_uri(uri)

    def get_db(self):
        return self.db