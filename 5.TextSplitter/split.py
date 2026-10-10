from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter

text = "LangChain is a powerful framework for developing applications."

splitter = CharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=10,
    separator=" "
)

chunks = splitter.split_text(text)
print(chunks)   

text = "First paragraph.\n\nSecond paragraph."

splitter = RecursiveCharacterTextSplitter(
    chunk_size=80,
    chunk_overlap=20,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = splitter.split_text(text)
print(chunks) 


text = "LangChain simplifies working with LLMs by providing modular components."

splitter = TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=2
)

chunks = splitter.split_text(text)
print(chunks)     