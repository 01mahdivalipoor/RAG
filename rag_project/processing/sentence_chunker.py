import nltk

from models import Chunk


class SentenceChunker:

    def __init__(
        self,
        max_sentences=5
    ):
        self.max_sentences = (
            max_sentences
        )

    def chunk_document(
        self,
        document
    ):

        sentences = nltk.sent_tokenize(
            document.content
        )

        chunks = []

        current = []

        chunk_id = 0

        for sentence in sentences:

            current.append(sentence)

            if len(current) >= self.max_sentences:

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