from langchain.vectorstores import FAISS
from langchain.embeddings import AzureOpenAIEmbeddings


class Memory:
    def __init__(self, **kwargs):
        self._embeddings = AzureOpenAIEmbeddings(chunk_size = 1)

    def get_embeddings(self):
        return self._embeddings

