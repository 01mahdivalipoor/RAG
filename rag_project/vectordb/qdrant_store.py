from typing import List

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from models import Chunk


class QdrantStore:

    def __init__(
        self,
        collection_name: str,
        vector_size: int,
        host: str = "localhost",
        port: int = 6333
    ):

        self.collection_name = collection_name

        self.client = QdrantClient(
            host=host,
            port=port
        )

        self._create_collection(
            vector_size
        )

    def _create_collection(
        self,
        vector_size: int
    ):

        collections = self.client.get_collections()

        existing = [
            c.name
            for c in collections.collections
        ]

        if self.collection_name in existing:
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    def add_chunks(
        self,
        chunks: List[Chunk],
        embeddings: List[List[float]]
    ):

        points = []

        for idx, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            point = PointStruct(
                id=idx,

                vector=embedding,

                payload={
                    "content": chunk.content,
                    "source": chunk.source,
                    "chunk_id": chunk.chunk_id
                }
            )

            points.append(point)

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(
        self,
        query_embedding: List[float],
        limit: int = 5
    ):

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit
        )

        return results