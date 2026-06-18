from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(
    pdf_path: str,
    add_source_metadata: bool = True,
) -> List[Document]:
    """
    Load PDF and return LangChain Documents.

    Args:
        pdf_path: path to pdf file
        add_source_metadata: add filename metadata

    Returns:
        List[Document]
    """

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    if add_source_metadata:
        file_name = Path(pdf_path).name

        for doc in docs:
            doc.metadata["source"] = file_name

    return docs


if __name__ == "__main__":

    documents = load_pdf(
        pdf_path="data/my_book.pdf"
    )

    print(f"Pages: {len(documents)}")

    print("\nMetadata:")
    print(documents[0].metadata)

    print("\nContent:")
    print(documents[0].page_content[:500])