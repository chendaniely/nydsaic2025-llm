import chatlas as ctl
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


chat = ctl.ChatOpenAI()
chat.extract_data(
    "My name is Susan and I'm 13 years old",
    data_model=Person,
)
