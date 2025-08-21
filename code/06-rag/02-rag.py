from chatlas import ChatOpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

chat = ChatOpenAI(
    system_prompt="You are a helpful, but terse, assistant. "
    "If you can't answer the question based on the trusted content, say so.",
)


docs = SimpleDirectoryReader("code/06-rag/data").load_data()
index = VectorStoreIndex.from_documents(docs)


# from llama_index.core import StorageContext, load_index_from_storage

# Load the knowledge store (index) from disk
# storage_context = StorageContext.from_defaults(persist_dir="./storage")
# index = load_index_from_storage(storage_context)


def retrieve_trusted_content(query):
    retriever = index.as_retriever(similarity_top_k=5)
    nodes = retriever.retrieve(query)
    return [f"<excerpt>{x.text}</excerpt>" for x in nodes]


user_query = "What is the capital of the moon?"
trusted_content = retrieve_trusted_content(user_query)

chat.chat(*trusted_content, "what is the capital of the moon?")
