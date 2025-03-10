
from langchain_experimental.sql import SQLDatabaseSequentialChain

class GenericSQLChain:
    def __init__(self, llm, sql_database, verbose=True, use_query_checker=True, top_k=1):
        self.chain = SQLDatabaseSequentialChain.from_llm(
            llm=llm,
            db=sql_database,
            verbose=verbose,
            use_query_checker=use_query_checker,
            top_k=top_k
        )

    def run_query(self, question):
        return self.chain.run(question)


