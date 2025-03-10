import os
from dotenv import load_dotenv
from langchain.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_community.chat_models import ChatOllama

load_dotenv()

class MySQLDatabase:
    def __init__(self):
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        db_name = os.getenv("MYSQL_DB")
        model = os.getenv("OLLAMA_MODEL", "deepseek-r1:1.5b")

        uri = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
        self.db = SQLDatabase.from_uri(uri)
        self.llm = ChatOllama(model=model)
        self.chain = create_sql_query_chain(self.llm, self.db)

    def query(self, nl_question):
        sql_query = self.chain.invoke({"question": nl_question})
        print("Generated SQL Query:", sql_query)
        result = self.db.run(sql_query)
        return result

# Example usage:
if __name__ == "__main__":
    db = MySQLDatabase()
    response = db.query("How many Alice are in the database?")
    print("Query Result:", response)