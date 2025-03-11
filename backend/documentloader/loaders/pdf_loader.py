from langchain_community.document_loaders import PyPDFLoader

class PyPDFLoaderWrapper:
    def __init__(self, file_path):
        self.loader = PyPDFLoader(file_path)

    def load(self):
        return self.loader.load()