from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

document = Document(page_content="Hello, welcome to LangChain Open Tutorial!")

# Check the attributes using __dict__
document.__dict__

# Add metadata
document.metadata["source"] = "./example-file.pdf"
document.metadata["page"] = 0

# Check metadata
document.metadata

# Example file path
FILE_PATH = "./data/01-document-loader-sample.pdf"

# Set up the loader
loader = PyPDFLoader(FILE_PATH)

# Load Documents
docs = loader.load()

# Check the number of loaded Documents
len(docs)

# Check Documents
docs[0:10]

# Set up the TextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=128, chunk_overlap=0)

# Split Documents into chunks
docs = loader.load_and_split(text_splitter=text_splitter)