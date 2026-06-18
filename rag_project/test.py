# test_loader.py

from ingestion.loader import DirectoryLoader

loader = DirectoryLoader("data")

documents = loader.load()

for doc in documents:
    print(doc.source)
    print(doc.content[:100])

# test_cleaner.py

from ingestion.loader import DirectoryLoader
from processing.cleaner import TextCleaner

loader = DirectoryLoader("data")

documents = loader.load()

cleaner = TextCleaner()

cleaned_documents = cleaner.clean_documents(documents)

for doc in cleaned_documents:
    print(doc.content[:300])

#test_chunker.py

from ingestion.loader import DirectoryLoader
from processing.cleaner import TextCleaner
from processing.chunker import TextChunker


loader = DirectoryLoader("data")
documents = loader.load()

cleaner = TextCleaner()
documents = cleaner.clean_documents(documents)

chunker = TextChunker(
    chunk_size=100,
    chunk_overlap=20
)

chunks = chunker.chunk_documents(
    documents
)

for chunk in chunks[:5]:
    print("=" * 50)
    print(chunk.chunk_id)
    print(chunk.content)