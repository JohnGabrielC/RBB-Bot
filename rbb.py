import discord
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
roys = ("rbb", "Rbb", "RBb", "RBB")

def load_counters():
    with open("counters.json", "r") as f:
        counters = json.load(f)
    return counters

def save_counters(counters):
    with open("counters.json", "w") as f:
        json.dump(counters, f)

@client.event
async def on_message(message):
    if message.content in roys:
        counters = load_counters()
        counters["rbb"] += 1
        await message.channel.send("rbb counter: {}".format(str(counters["rbb"])))
        save_counters(counters)


client.run(TOKEN)
