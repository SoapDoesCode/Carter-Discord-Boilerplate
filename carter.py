# Sanware Framework MK III - Branch 'Carter-Discord Boilerplate'

# Boilerplate for linking Discord bot with a Carter API. Forked from CarterAPI's documentation.

# Do not edit this file unless intending to fork. Only edit bot.py.

import requests
import json

def SendToCarter(sentence, User, APIkey):
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": f"{sentence}",
        "key": f"{APIkey}",
        "playerId": f"{User}"
    }))

    RawResponse = response.json()
    Response = RawResponse["output"]
    FullResponse = Response["text"]
    ResponseOutput = FullResponse

    f = open("CarterResponse.txt", "w+")
    f.write(f"{ResponseOutput}")
    f.close()
