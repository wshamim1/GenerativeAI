from langchain_community.document_loaders import WikipediaLoader

class WikipediaLoaderWrapper:
    def __init__(self, wikipedia_page):
        self.loader = WikipediaLoader(wikipedia_page)

    def load(self):
        return self.loader.load()