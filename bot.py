# Sanware Framework MK III - Branch 'Carter-Discord Boilerplate'

# Boilerplate for linking Discord bot with a Carter API. Written by TheMechanic57.

# Load packages.

import os
import nextcord as discord
from dotenv import load_dotenv
from carter import *

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Modified to use the .env file for API keys

# To use this, open the .env file and replace the text in the quotes with your API keys. (do not remove the quotes)

load_dotenv()

APIkey = os.getenv("CARTER_API_KEY")

DiscordAPI = os.getenv("DISCORD_API_KEY")
# Modified to use the .env file for API keys

RawUIName = "REPLACE THIS WITH THE NAME OF YOUR CARTER AGENT. IT CAN BE ANY STRING."

# Program

print(f"{RawUIName} is online.") # This is just a confirmation that the bot is actually getting somewhere

@client.event
async def on_message(message):
    # Script is below.

    if message.author == client.user:
        return

    User = message.author
    sentence = message.content
    sentence = sentence.lower()
    UIName = RawUIName.lower()

    if UIName in sentence:
        SendToCarter(sentence, User, APIkey)
        with open('CarterResponse.txt') as f:
            ResponseOutput = f.read()

        print(message.content)
        await message.channel.send(f"{ResponseOutput}")
        print(ResponseOutput)
        os.remove("CarterResponse.txt")
    else:
        pass

client.run(DiscordAPI)
