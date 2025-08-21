import chatlas as ctl
from pydantic import BaseModel


class Image(BaseModel):
    primary_shape: str
    primary_colour: str


chat = ctl.ChatOpenAI()
chat.extract_data(
    # https://picsum.photos/200/300
    ctl.content_image_url(
        "https://fastly.picsum.photos/id/19/200/300.jpg?hmac=znGSIxHtiP0JiLTKW6bT7HlcfagMutcHfeZyNkglQFM"
    ),
    data_model=Image,
)
