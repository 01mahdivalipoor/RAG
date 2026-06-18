from typing import List

from embeddings.embedder import EmbeddingModel
from vectordb.qdrant_store import QdrantStore
from models import RetrievedChunk


class Retriever:

    def __init__(
        self,
        embedder: EmbeddingModel,
        vector_store: QdrantStore,
        top_k: int = 5
    ):
        self.embedder = embedder
        self.vector_store = vector_store
        self.top_k = top_k

    def retrieve(
        self,
        query: str
    ) -> List[RetrievedChunk]:

        query_embedding = (
            self.embedder.embed_text(query)
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            limit=self.top_k
        )

        retrieved_chunks = []

        for result in results:

            chunk = RetrievedChunk(
                content=result.payload["content"],
                source=result.payload["source"],
                chunk_id=result.payload["chunk_id"],
                score=result.score
            )

            retrieved_chunks.append(chunk)

        return retrieved_chunks
    
    def build_context(
        self,
        chunks: List[RetrievedChunk]
    ) -> str:

        context_parts = []

        for chunk in chunks:

            context_parts.append(
                chunk.content
            )

        return "\n\n".join(
            context_parts
        )