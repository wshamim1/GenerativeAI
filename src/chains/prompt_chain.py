from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class GenericPromptChain:
    def __init__(self, llm, prompt_template):
        self.prompt = ChatPromptTemplate.from_template(prompt_template)
        self.llm = llm
        self.chain = self.prompt | self.llm | StrOutputParser()

    def run(self, **kwargs):
        return self.chain.invoke(kwargs)
