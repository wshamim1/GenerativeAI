

from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentsSplitter:

    def __init__(self, document):
        self.document = document

    
    def split_document(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False,
        )

        # Combine all loaded documents
        
        splited_documents = text_splitter.split_documents(self.document)
        print(splited_documents)
        return splited_documents
    



    