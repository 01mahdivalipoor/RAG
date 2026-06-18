class PromptBuilder:

    @staticmethod
    def build(
        question: str,
        context: str
    ) -> str:

        return f"""
You are a retrieval-augmented assistant.

Rules:

1. Answer only from the provided context.
2. Do not invent facts.
3. If information is missing, say you don't know.
4. Keep answers concise.
5. Cite document snippets when possible.

Context:
{context}

Question:
{question}

Answer:
""".strip()