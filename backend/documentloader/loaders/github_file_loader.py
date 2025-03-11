from langchain_community.document_loaders import GithubFileLoader

class GithubFileLoaderWrapper:
    def __init__(self, repo, file_path, branch="main"):
        self.loader = GithubFileLoader(repo, file_path, branch)

    def load(self):
        return self.loader.load()