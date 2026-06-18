import re
from typing import List

from ingestion.loader import Document


class TextCleaner:
    def __init__(
        self,
        remove_extra_spaces: bool = True,
        remove_extra_newlines: bool = True,
    ):
        self.remove_extra_spaces = remove_extra_spaces
        self.remove_extra_newlines = remove_extra_newlines

    def clean_text(self, text: str) -> str:

        if self.remove_extra_spaces:
            text = re.sub(r"\s+", " ", text)

        if self.remove_extra_newlines:
            text = re.sub(r"\n{2,}", "\n", text)

        return text.strip()

    def clean_document(self, document: Document) -> Document:

        cleaned_text = self.clean_text(document.content)

        return Document(
            content=cleaned_text,
            source=document.source
        )

    def clean_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:

        return [
            self.clean_document(doc)
            for doc in documents
        ]