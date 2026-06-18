from pathlib import Path
from typing import List


class Document:
    def __init__(self, content: str, source: str):
        self.content = content
        self.source = source

    def __repr__(self):
        return f"Document(source={self.source})"


class TextLoader:
    def load(self, file_path: str) -> Document:
        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        return Document(
            content=content,
            source=str(path)
        )


class DirectoryLoader:
    def __init__(self, directory: str):
        self.directory = Path(directory)

    def load(self) -> List[Document]:
        documents = []

        for file in self.directory.glob("*.txt"):
            loader = TextLoader()
            documents.append(loader.load(file))

        return documents
    

# test_loader.py

from ingestion.loader import DirectoryLoader

loader = DirectoryLoader("data")

documents = loader.load()

for doc in documents:
    print(doc.source)
    print(doc.content[:100])