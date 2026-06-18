import numpy as np

from sentence_transformers import (
    SentenceTransformer
)

from models import Chunk


class SemanticChunker:

    def __init__(
        self,
        model_name=
        "mixedbread-ai/mxbai-embed-large-v1",

        threshold=0.75
    ):

        self.model = (
            SentenceTransformer(
                model_name
            )
        )

        self.threshold = threshold

    def cosine_similarity(
        self,
        a,
        b
    ):
        return np.dot(a, b) / (
            np.linalg.norm(a)
            * np.linalg.norm(b)
        )

    def chunk_document(
        self,
        document
    ):

        sentences = (
            document.content.split(".")
        )

        embeddings = self.model.encode(
            sentences
        )

        chunks = []

        current = [
            sentences[0]
        ]

        chunk_id = 0

        for i in range(
            1,
            len(sentences)
        ):

            sim = (
                self.cosine_similarity(
                    embeddings[i - 1],
                    embeddings[i]
                )
            )

            if sim < self.threshold:

                chunks.append(
                    Chunk(
                        content=" ".join(
                            current
                        ),
                        source=document.source,
                        chunk_id=chunk_id
                    )
                )

                current = []
                chunk_id += 1

            current.append(
                sentences[i]
            )

        if current:

            chunks.append(
                Chunk(
                    content=" ".join(
                        current
                    ),
                    source=document.source,
                    chunk_id=chunk_id
                )
            )

        return chunks