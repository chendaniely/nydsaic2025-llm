import chatlas as clt
import numpy as np
import json


def len_ai(n):
    values = np.random.rand(n).tolist()
    chat = clt.ChatAnthropic(model="claude-sonnet-4-0")
    return chat.chat("How long is this array", json.dumps(values))


len_ai(10)
len_ai(100)
len_ai(1000)
len_ai(10_000)
len_ai(42)
len_ai(112)
len_ai(103)
len_ai(1337)


def len_ai(n):
    values = np.random.rand(n).tolist()
    chat = clt.ChatOpenAI(model="gpt-5")
    return chat.chat("How long is this array", json.dumps(values))


len_ai(10)
len_ai(100)
len_ai(1000)
len_ai(10_000)
len_ai(42)
len_ai(112)
len_ai(103)
len_ai(1337)
