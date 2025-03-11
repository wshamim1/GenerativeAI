import os
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase

load_dotenv()

class OracleDatabase:
    def __init__(self):
        user = os.getenv("ORACLE_USER")
        password = os.getenv("ORACLE_PASSWORD")
        host = os.getenv("ORACLE_HOST")
        port = os.getenv("ORACLE_PORT")
        db_name = os.getenv("ORACLE_DB")

        uri = f"oracle+cx_oracle://{user}:{password}@{host}:{port}/?service_name={db_name}"
        self.db = SQLDatabase.from_uri(uri)

    def get_db(self):
        return self.db