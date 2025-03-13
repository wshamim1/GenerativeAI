from langchain_community.document_loaders import JSONLoader

class JSONLoaderWrapper:
    def __init__(self, file_path,jq_schema):
        self.loader = JSONLoader(file_path,jq_schema=jq_schema,text_content=False)

    def load(self):
        return self.loader.load()