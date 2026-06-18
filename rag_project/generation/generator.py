import ollama


class QwenGenerator:

    def __init__(
        self,
        model_name="qwen3:8b"
    ):
        self.model_name = model_name

    def generate(
        self,
        prompt: str
    ) -> str:

        response = ollama.chat(
            model=self.model_name,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def stream(
        self,
        prompt: str
    ):

        stream = ollama.chat(
            model=self.model_name,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            stream=True
        )

        for chunk in stream:

            yield chunk["message"]["content"]