from chatlas import ChatAnthropic
from shiny.express import ui

# Might instead be ChatAnthropic, ChatOpenAI, or some other provider
chat_client = ChatAnthropic()

chat = ui.Chat(id="my_chat")
chat.ui()


@chat.on_user_submit
async def handle_user_input(user_input: str):
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)
