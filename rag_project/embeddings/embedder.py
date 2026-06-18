from typing import List

from sentence_transformers import SentenceTransformer

from models import Chunk


class EmbeddingModel:

    def __init__(
        self,
        model_name: str = "mixedbread-ai/mxbai-embed-large-v1"
    ):
        self.model = SentenceTransformer(
            model_name
        )

    def embed_text(
        self,
        text: str
    ) -> List[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_chunks(
        self,
        chunks: List[Chunk]
    ) -> List[List[float]]:

        texts = [
            chunk.content
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()