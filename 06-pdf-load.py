from langchain_community.document_loaders import PyPDFLoader

FILE_PATH = "./data/layout-parser-paper.pdf"
def show_metadata(docs):
    if docs:
        print("[metadata]")
        print(list(docs[0].metadata.keys()))
        print("\n[examples]")
        max_key_length = max(len(k) for k in docs[0].metadata.keys())
        for k, v in docs[0].metadata.items():
            print(f"{k:<{max_key_length}} : {v}")

# Initialize the PDF loader
loader = PyPDFLoader(FILE_PATH)

# Load data into Document objects
docs = loader.load()

# Print the contents of the document
print(docs[10].page_content[:300])

# output metadata
show_metadata(docs)

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load Documents and split into chunks. Chunks are returned as Documents.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=200)
docs = loader.load_and_split(text_splitter=text_splitter)
print(docs[0].page_content)

# Initialize PDF loader, enable image extraction option
loader = PyPDFLoader(FILE_PATH, extract_images=True)

# load PDF page
docs = loader.load()

# access page content
print(docs[4].page_content[:300])

show_metadata(docs)

from langchain_community.document_loaders import PyPDFDirectoryLoader

# directory path
loader = PyPDFDirectoryLoader("./data/")

# load documents
docs = loader.load()

# print the number of documents
docs_len = len(docs)
print(docs_len)

# get document from a directory
document = docs[docs_len - 1]

# print the contents of the document
print(document.page_content[:300])

print(document.metadata)