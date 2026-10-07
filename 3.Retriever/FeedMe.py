from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. Load all markdown files
loader = DirectoryLoader(
    path=r"C:\Users\panka\Documents\Learning\Vue\vue-docs\src",  # adjust path
    glob="**/*.md",
    loader_cls=UnstructuredMarkdownLoader
)
docs = loader.load()
print(f"Loaded {len(docs)} documents")

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# 3. Create vector store (local, no API needed with Ollama)
embeddings = OllamaEmbeddings(model="all-minilm:l6-v2", base_url="http://localhost:11434")#use a embedding model only for vectorization of the text
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local(r"C:\Users\panka\Documents\Learning\Vue\vue-docs\src\guide\vue_faiss_index")  # persist to disk

# 4. Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 5. Build RAG chain
prompt = ChatPromptTemplate.from_template("""
Answer the question about Vue.js using only the context below.
If the answer isn't in the context, say "I don't know."

Context: {context}

Question: {question}
Answer:
""")

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

llm = ChatOllama(model="qwen3.5:4b", base_url="http://localhost:11434")  # or any local model

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 6. Ask questions
print(rag_chain.invoke("What is the Composition API in Vue?"))
# print(rag_chain.invoke("How do you use v-model?"))   