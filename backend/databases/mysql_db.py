import os
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase

load_dotenv()

class MySQLDatabase:
    def __init__(self):
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        db_name = os.getenv("MYSQL_DB")

        uri = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
        self.db = SQLDatabase.from_uri(uri)

    def get_db(self):
        return self.db