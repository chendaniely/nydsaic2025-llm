from chatlas import ChatAnthropic
from shiny.express import ui

from helper.get_coordinates import get_coordinates
from helper.get_weather import get_weather_check

# chat_client = ChatAnthropic()

# chat_client.register_tool(get_coordinates)
# chat_client.register_tool(get_weather_check)

# chat = ui.Chat(id="chat")
# chat.ui(
#     messages=[
#         "Hello! I am a weather bot! Where would you like to get the weather form?"
#     ]
# )


# @chat.on_user_submit
# async def _(user_input: str):
#     response = await chat_client.stream_async(user_input, content="all")
#     await chat.append_message_stream(response)

chat = ChatAnthropic()
chat.register_tool(get_coordinates)
chat.register_tool(get_weather_check)
chat.chat("What's the weather in NYC?")
