import discord
from discord.ext.commands import Bot

import platform
import logging
import os
import config
import asyncio



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
client = Bot(description=config.des, command_prefix=config.pref, intents=intents)

client.load_extension("cogs.roles")
client.load_extension("cogs.streamalerts")


@client.event
async def on_ready():

    print("Bot online!\n")
    print("Discord.py API version:", discord.__version__)
    print("Python version:", platform.python_version())
    print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
    print("Name : {}".format(client.user.name))
    print("Client ID : {}".format(client.user.id))
    print("Currently active on " + str(len(client.guilds)) + " server(s).\n")
    logger.info("Bot started successfully.")

    await client.change_presence(status=discord.Status.online, activity=discord.Game('with whales'))    


@client.command()
async def hello(ctx):
    def check(m):
        return m.author == ctx.author
    await ctx.send("Hello")
    msg = await client.wait_for('message', check=check)
    await ctx.send(f"You said {msg.content}. Hi again.")


client.run(config.token)

