from typing import List

from models import Document, Chunk


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += (
                self.chunk_size
                - self.chunk_overlap
            )

        return chunks

    def chunk_document(
        self,
        document: Document
    ) -> List[Chunk]:

        text_chunks = self.split_text(
            document.content
        )

        chunks = []

        for idx, chunk_text in enumerate(text_chunks):

            chunk = Chunk(
                content=chunk_text,
                source=document.source,
                chunk_id=idx,
                metadata=document.metadata
            )

            chunks.append(chunk)

        return chunks

    def chunk_documents(
        self,
        documents: List[Document]
    ) -> List[Chunk]:

        all_chunks = []

        for document in documents:

            chunks = self.chunk_document(
                document
            )

            all_chunks.extend(chunks)

        return all_chunks