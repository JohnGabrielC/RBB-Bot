import discord
import os
import json
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
roys = ["rbb", "Rbb", "RBb", "RBB", "rBb", "RbB", "rbB", "rBB"]
commands = {"roys big": ["balls"],
            "roy's big": ["balls"],
            "roys": ["got big balls", "big balls",
                    "fat juicy delicious scrumptious ginormous jumbo cawck balls"],
            "roy's": ["got big balls", "big balls",
                    "fat juicy delicious scrumptious ginormous jumbo cawck balls"],
            "ken": ["is nice", "has hella girls"],
            "ray": ["is nice", "has hella girls"]} 

def load_counters():
    with open("counters.json", "r") as f:
        counters = json.load(f)
    return counters

def save_counters(counters):
    with open("counters.json", "w") as f:
        json.dump(counters, f)

@client.event
async def on_message(message):
    if message.content.lower() in commands:
        ran_num = random.randrange(0, len(commands[message.content]))
        await message.channel.send("{}".format(commands[message.content][ran_num]))

    elif message.content.lower() in roys:
        counters = load_counters()
        counters["rbb"] += 1
        await message.channel.send("Rbb Counter: {}".format(str(counters["rbb"])))
        save_counters(counters)

client.run(TOKEN)
