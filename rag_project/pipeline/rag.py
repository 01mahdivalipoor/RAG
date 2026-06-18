from retrieval.retriever import Retriever
from prompts.template import PromptBuilder
from generation.generator import QwenGenerator


class RAGPipeline:

    def __init__(
        self,
        retriever,
        generator
    ):
        self.retriever = retriever
        self.generator = generator

    def ask(
        self,
        question: str
    ):

        chunks = self.retriever.retrieve(
            question
        )

        context = self.retriever.build_context(
            chunks
        )

        prompt = PromptBuilder.build(
            question=question,
            context=context
        )

        answer = self.generator.generate(
            prompt
        )

        return {
            "answer": answer,
            "chunks": chunks
        }
    
    def stream(
        self,
        question: str
    ):

        chunks = self.retriever.retrieve(
            question
        )

        context = self.retriever.build_context(
            chunks
        )

        prompt = PromptBuilder.build(
            question=question,
            context=context
        )

        for token in self.generator.stream(
            prompt
        ):
            yield token