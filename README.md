# Project

This project provides a comprehensive framework for working with LangChain, LangGraph, RAG (Retrieval-Augmented Generation), Agents, and various Tools. It includes modules for loading documents, generating embeddings, interacting with databases, and running various chains and prompts.

## Project Structure
```
.env
backend/
    agents/
        agent_executor.py
    chains/
    databases/
    documentloader/
        __init__.py
        document_loader.py
    loaders/
        bigquery_loader.py
        csv_loader.py
        github_file_loader.py
        ...
    embeddings/
        ollama_embeddings.py
    langchain/
    langgraph/
    llms/
    splitter/
    tools/
    utils/
    vectorstores/
data/
    test.csv
    test.json
    test.pdf
examples/
    email_composer.py
    emojis.py
    emotions.py
    generate_stories.py
    mysql_query.py
    postgres_query.py
rag/
    removePIIdata.py
    summerize_document.py
README.md
requirements.txt
vectorDBs/
    chroma.sqlite3
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   ```sh 
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add the necessary environment variables as shown in the provided `.env` file.

## Usage

### Document Loading
The `DocumentLoader` class in `document_loader.py` supports loading documents from various sources including CSV, PDF, JSON, and more.

#### Example:
```python
from backend.documentloader.document_loader import DocumentLoader

file_path = "data/test.pdf"
loader = DocumentLoader(file_path)
doc = loader.load()
print(doc)
```

### Embeddings
The `OllamaEmbedding` class in `ollama_embeddings.py` provides methods to generate embeddings using the Ollama model.

#### Example:
```python
from backend.embeddings.ollama_embeddings import OllamaEmbedding

embeddings = OllamaEmbedding().get_embeddings()
print(embeddings)
```

### Examples
Several example scripts are provided in the `examples/` directory to demonstrate various functionalities:

- `email_composer.py`: Compose an email using a prompt chain.
- `emojis.py`: Generate an emoji based on input text.
- `emotions.py`: Classify the sentiment of a user's text.
- `generate_stories.py`: Generate a story based on a given title.
- `mysql_query.py`: Execute a MySQL query using a prompt chain.
- `postgres_query.py`: Execute a PostgreSQL query using a prompt chain.
- `rag/`: Contains scripts for Retrieval-Augmented Generation tasks.

### Running Examples
To run an example script, use the following command:

```sh
python examples/email_composer.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.