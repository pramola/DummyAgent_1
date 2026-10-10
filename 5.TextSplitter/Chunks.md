Text splitter are the components that are responsible for splitting/dividing whole document into smaller chunks/parts.

Document can be very large and loading at a single time is failure prone. No model can take all documents at a single time . They are limited by context window size and large text causes more computation leading to expensive operations.

Smaller chunks/parts that are splitted can be done in different ways.

Character Based Splitting:
    Splitting by fixed characters or count . 
    One way is splitting by 10 words. Thus it creates an array/list of 10-word sentences.
    Another way is by newline character. Thus it creates a list of all sentences.

Recursive splitting:
    Splitting by bigger seperators constraints. The sequence of splitting selection is 
    (paragraph) → \n (line) → (word) → "" (character)
    So First tries by splitting into paragraphs if the chunk is large split it by line and if line is very large then split by word. Recommended approach as the chunks maintains documents semantic meaning.

Structure Based Splitting:
    If a very structured document like a json, html, xml or anything else then this way it splits according to doc's structure and thus it maintains the semantic structure.
    Example - A code file can be chunked in terms of functions and classes

Semantic Splitting:
    Using a dedicated splitting model that tries to catch semantic meanings of paragraphs, sentences and thus it can be very beneficial and multiple paragraphs can point towards similar knowledge.
    How it works:
        Split text into individual sentences.
        Compute an embedding vector for each sentence.
        Calculate cosine similarity between consecutive sentences.
        Where similarity drops below a threshold (a "semantic boundary"), a new chunk begins.
        Chunks are merged if they're too small, respecting a max size limit.
