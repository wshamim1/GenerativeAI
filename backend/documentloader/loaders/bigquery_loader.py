from langchain_community.document_loaders import BigQueryLoader

class BigQueryLoaderWrapper:
    def __init__(self, project, dataset, table):
        self.loader = BigQueryLoader(project=project, dataset=dataset, table=table)

    def load(self):
        return self.loader.load()