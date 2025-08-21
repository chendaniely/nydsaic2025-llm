from chatlas import ChatOpenAI

chat = ChatOpenAI(
    system_prompt="You are a helpful, but terse, assistant. "
    "If you can't answer the question based on the trusted content, say so.",
)

user_query = "What is the capital of the moon?"

chat.chat(user_query)
