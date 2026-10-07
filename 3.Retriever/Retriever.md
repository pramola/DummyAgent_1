Retrivers are the runnables that get some document/indexed and your query and then return the relevant response from the available indexed documents by matching their similarity using vector embeddings.

Their basic operation is 
User question
      ↓
   Retriever
      ↓
Relevant documents
      ↓
      LLM
      ↓
    Answer

1. First index the documents. Get them stored and their metadata information
2. Generate Embeddings out of them 
3. Now match accordingly with embeddings/key word and the other strategy shared below


LangChain supports different retrieval strategies, for example:

Vector store retriever — searches embeddings for semantically similar text.
BM25 retriever — uses keyword-based search.
Multi-query retriever — generates multiple search queries to improve retrieval.
Contextual compression retriever — retrieves documents and then filters/compresses them to the most relevant parts.
Parent document retriever — searches smaller chunks but returns their larger parent documents.

So within RAG(Retrieval - Augmented - Generation ) this can be the search/retrieval part. This is the middle part performaed in the RAG process/workflow

In RAG workflow normally, you first index all the data, index quality metadata, generate quality chunks from documents. After all this chunking & indexing. Prefer good chunking models and embedding models. As they will create meaningful chunks and create relevant better vectors
Second part plays its part which is retrieval that is more like similarity search.
Third part is generation where another model(text generating/chat model) gets the relevant result and the main user questions and efficiently combine text to generate a beautiful framed and well structured response.
