import os
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase

load_dotenv()

class SQLServerDatabase:
    def __init__(self):
        user = os.getenv("SQLSERVER_USER")
        password = os.getenv("SQLSERVER_PASSWORD")
        host = os.getenv("SQLSERVER_HOST")
        port = os.getenv("SQLSERVER_PORT")
        db_name = os.getenv("SQLSERVER_DB")

        uri = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"
        self.db = SQLDatabase.from_uri(uri)

    def get_db(self):
        return self.db