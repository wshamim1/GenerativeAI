from langchain_community.document_loaders import GitHubIssuesLoader

class GitHubIssuesLoaderWrapper:
    def __init__(self, repo, github_issue_creator):
        self.loader = GitHubIssuesLoader(repo, github_issue_creator)

    def load(self):
        return self.loader.load()