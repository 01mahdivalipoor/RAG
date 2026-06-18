from embeddings.embedder import EmbeddingModel

from vectordb.qdrant_store import QdrantStore

from retrieval.retriever import Retriever

from generation.generator import QwenGenerator

from pipeline.rag import RAGPipeline


def build_rag():

    embedder = EmbeddingModel()

    store = QdrantStore(
        collection_name="rag_docs",
        vector_size=1024
    )

    retriever = Retriever(
        embedder=embedder,
        vector_store=store,
        top_k=5
    )

    generator = QwenGenerator(
        model_name="qwen3:8b"
    )

    rag = RAGPipeline(
        retriever=retriever,
        generator=generator
    )

    return rag


def main():

    rag = build_rag()

    while True:

        question = input(
            "\nQuestion > "
        )

        if question.lower() in [
            "exit",
            "quit"
        ]:
            break

        result = rag.ask(
            question
        )

        print("\nAnswer:\n")

        print(
            result["answer"]
        )


if __name__ == "__main__":
    main()