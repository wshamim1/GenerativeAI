import os
import importlib

class DocumentLoader:
    loader_map = {
        '.csv': 'csv_loader.CSVLoaderWrapper',
        '.txt': 'text_loader.TextLoaderWrapper',
        '.md': 'markdown_loader.UnstructuredMarkdownLoaderWrapper',
        '.docx': 'word_loader.UnstructuredWordDocumentLoaderWrapper',
        '.pdf': 'pdf_loader.PyPDFLoaderWrapper',
        '.json': 'json_loader.JSONLoaderWrapper',
        '.xml': 'xml_loader.UnstructuredXMLLoaderWrapper',
        '.wiki': 'wikipedia_loader.WikipediaLoaderWrapper',
    }

    def __init__(self, file_path=None, jq_schema='.', json_text_content=True,
                 mongo_uri=None, db_name=None, collection_name=None, mongo_query=None,
                 github_repo=None, github_filepath=None, github_branch="main", github_issue_creator=None,
                 bigquery_project=None, bigquery_dataset=None, bigquery_table=None,
                 web_url=None, wikipedia_page=None):
        self.file_path = file_path
        self.jq_schema = jq_schema
        self.json_text_content = json_text_content
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.mongo_query = mongo_query
        self.github_repo = github_repo
        self.github_filepath = github_filepath
        self.github_branch = github_branch
        self.github_issue_creator = github_issue_creator
        self.bigquery_project = bigquery_project
        self.bigquery_dataset = bigquery_dataset
        self.bigquery_table = bigquery_table
        self.web_url = web_url
        self.wikipedia_page = wikipedia_page

    def load(self):
        if self.mongo_uri and self.db_name and self.collection_name:
            from .loaders.mongodb_loader import MongodbLoaderWrapper
            loader = MongodbLoaderWrapper(
                connection_string=self.mongo_uri,
                db_name=self.db_name,
                collection_name=self.collection_name,
                query=self.mongo_query
            )
            return loader.load()

        if self.github_repo and self.github_filepath:
            from .loaders.github_file_loader import GithubFileLoaderWrapper
            loader = GithubFileLoaderWrapper(
                repo=self.github_repo,
                file_path=self.github_filepath,
                branch=self.github_branch
            )
            return loader.load()
        
        if self.github_repo and self.github_issue_creator:
            from .loaders.github_issues_loader import GitHubIssuesLoaderWrapper
            loader = GitHubIssuesLoaderWrapper(
                repo=self.github_repo,
                github_issue_creator=self.github_issue_creator,
            )
            return loader.load()

        if self.bigquery_project and self.bigquery_dataset and self.bigquery_table:
            from .loaders.bigquery_loader import BigQueryLoaderWrapper
            loader = BigQueryLoaderWrapper(
                project=self.bigquery_project,
                dataset=self.bigquery_dataset,
                table=self.bigquery_table
            )
            return loader.load()

        if self.web_url:
            from .loaders.web_loader import WebBaseLoaderWrapper
            loader = WebBaseLoaderWrapper(self.web_url)
            return loader.load()

        if self.wikipedia_page:
            from .loaders.wikipedia_loader import WikipediaLoaderWrapper
            loader = WikipediaLoaderWrapper(self.wikipedia_page)
            return loader.load()

        if not self.file_path:
            raise ValueError("file_path must be specified if no other data source is provided.")

        file_extension = os.path.splitext(self.file_path)[1].lower()
        loader_class_path = self.loader_map.get(file_extension)

        if not loader_class_path:
            raise ValueError(f"Unsupported file type: {file_extension}")

        module_name, class_name = loader_class_path.rsplit('.', 1)
        module = importlib.import_module(f'backend.documentloader.loaders.{module_name}')
        loader_class = getattr(module, class_name)

        if file_extension == '.json':
            loader = loader_class(
                self.file_path,
                jq_schema=self.jq_schema,
                text_content=self.json_text_content
            )
        else:
            loader = loader_class(self.file_path)

        return loader.load()

