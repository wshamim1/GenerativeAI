import os
from langchain_community.document_loaders import (
    CSVLoader,
    TextLoader,
    PyPDFLoader,
    JSONLoader,
    UnstructuredMarkdownLoader,
    UnstructuredWordDocumentLoader,
)

class DocumentLoader:
    loader_map = {
        '.csv': CSVLoader,
        '.txt': TextLoader,
        '.md': UnstructuredMarkdownLoader,
        '.docx': UnstructuredWordDocumentLoader,
        '.pdf': PyPDFLoader,
        '.json': JSONLoader,
    }

    def __init__(self, file_path, jq_schema='.', json_text_content=True):
        self.file_path = file_path
        self.jq_schema = jq_schema
        self.json_text_content = json_text_content

    def load(self):
        file_extension = os.path.splitext(self.file_path)[1].lower()
        loader_class = self.loader_map.get(file_extension)

        if not loader_class:
            raise ValueError(f"Unsupported file type: {file_extension}")

        if file_extension == '.json':
            loader = loader_class(
                self.file_path,
                jq_schema=self.jq_schema,
                text_content=self.json_text_content
            )
        else:
            loader = loader_class(self.file_path)

        return loader.load()

# Example Usage:
if __name__ == '__main__':
    # Generic example, change file_path as needed
    file_path = "/data/test.pdf"
    loader = DocumentLoader(file_path)
    doc = loader.load()[0]
    print(doc)
