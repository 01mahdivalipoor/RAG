from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from models import Chunk


class RecursiveChunker:

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=50
    ):

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
        )

    def chunk_document(
        self,
        document
    ):

        texts = self.splitter.split_text(
            document.content
        )

        chunks = []

        for idx, text in enumerate(texts):

            chunks.append(
                Chunk(
                    content=text,
                    source=document.source,
                    chunk_id=idx
                )
            )

        return chunks