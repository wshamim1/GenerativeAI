from langchain_community.document_loaders import CSVLoader

class CSVLoaderWrapper:
    def __init__(self, file_path):
        self.loader = CSVLoader(file_path)

    def load(self):
        return self.loader.load()