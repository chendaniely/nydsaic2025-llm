from chatlas import ChatOpenAI, interpolate_file

chat = ChatOpenAI()
chat.system_prompt = interpolate_file(
    "prompt.md",
    variables={"role": "Yoda"},
)
chat.system_prompt
