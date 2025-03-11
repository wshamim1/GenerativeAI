from langchain_community.document_loaders import WebBaseLoader

class MongodbLoaderWrapper:
    def __init__(self, web_url):
        self.loader = WebBaseLoader(web_url)

    def load(self):
        return self.loader.load()