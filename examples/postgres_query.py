import sys, os
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())


from backend.databases.postgres_db import PostgresDatabase
from backend.llms.ollama_llm import OllamaLLM
from backend.chains.sql_chain import GenericSQLChain

# Initialize MySQL database
mysql_db = PostgresDatabase().get_db()

# Initialize LLM
llm = OllamaLLM().get_llm()

# Define prompt template for generating MySQL query
prompt_template = """ 
Given an input question, first create a syntactically correct MySQL query to run,
then look at the results of the query and return the answer.
Question: {question}
"""

# Initialize Generic SQL Chain
db_chain = GenericSQLChain(llm, mysql_db)

# Input question
question = "List me all name starting with A from orders?"

# Execute the question using the db_chain
query_result = db_chain.run_query(question)

print("Query Result:", query_result)