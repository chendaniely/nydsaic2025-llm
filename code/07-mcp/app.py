from chatlas import ChatOpenAI
from shiny import reactive
from shiny.express import ui

chat_client = ChatOpenAI()


@reactive.effect
async def _():
    await chat_client.register_mcp_tools_stdio_async(
        command="deno",
        args=[
            "run",
            "-N",
            "-R=node_modules",
            "-W=node_modules",
            "--node-modules-dir=auto",
            "jsr:@pydantic/mcp-run-python",
            "stdio",
        ],
    )


chat = ui.Chat("chat")
chat.ui(
    messages=[
        "Hi! Try asking me a question that can be answered by executing Python code."
    ],
)
chat.update_user_input(
    value="What's the 47th number in the Fibonacci sequence?"
)


@chat.on_user_submit
async def _(user_input: str):
    stream = await chat_client.stream_async(user_input, content="all")
    await chat.append_message_stream(stream)
