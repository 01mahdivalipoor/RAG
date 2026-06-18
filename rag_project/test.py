# PDF
#  ↓
# Chunk
#  ↓
# Embed
#  ↓
# Qdrant
#  ↓
# Retrieve
#  ↓
# Qwen3-8B
#  ↓
# Answer


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

# test_embedder.py
from embeddings.embedder import EmbeddingModel

embedder = EmbeddingModel()

vector = embedder.embed_text(
    "What is Retrieval Augmented Generation?"
)

print(type(vector))
print(len(vector))

vectors = embedder.embed_chunks(
    chunks
)

print(len(vectors))

#indexing test
from ingestion.loader import DirectoryLoader
from processing.cleaner import TextCleaner
from processing.chunker import TextChunker

from embeddings.embedder import EmbeddingModel
from vectordb.qdrant_store import QdrantStore


loader = DirectoryLoader("data")

documents = loader.load()

documents = TextCleaner().clean_documents(
    documents
)

chunks = TextChunker().chunk_documents(
    documents
)

embedder = EmbeddingModel()

vectors = embedder.embed_chunks(
    chunks
)

store = QdrantStore(
    collection_name="rag_docs",
    vector_size=len(vectors[0])
)

store.add_chunks(
    chunks,
    vectors
)

print("Indexed")

#search test
query = "What is RAG?"

query_vector = embedder.embed_text(
    query
)

results = store.search(
    query_vector,
    limit=3
)

for r in results:

    print("=" * 50)

    print(r.score)

    print(
        r.payload["content"]
    )