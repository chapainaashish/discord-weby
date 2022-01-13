# await is used to suspends the execution of the sorrounding coroutine until the execution of each coroutine has finished
import os
import discord
import random
from messages import *
from word_list import *

# making instance of Client class which interacts with Discord Api(handles events, tracks state)
client = discord.Client()


@client.event
async def on_ready():
    """Handles the connection and prepare response"""
    global guild
    for guild in client.guilds:
        if guild.name == "GUILD":
            break

    # client.user represents to bot
    print(f"{client.user} is here!")

    # printing server name
    print(guild.name)


@client.event
async def on_member_join(member):
    """Handles new member join event"""
    await member.create_dm()
    await member.dm_channel.send(f"Let's welcome {member.name}, Welcome to the {guild.name}!")


@client.event
async def on_message(message):
    """Handles message event"""
    # Prevention for replying own message, i.e. "bot" message
    if message.author == client.user:
        return

    # Saying hello if message start with "Hello"
    if message.content.startswith(hello_hints):
        await message.channel.send(f"{random.choice(hello_hints)} {message.author.name}")

    # Cheering up if any sad word found
    elif any(word in message.content for word in sad_words) and any(word in message.content for word in weby):
        await message.channel.send(random.choice(cheer_ups))

    # Sending motivational quotes if any hints found
    elif any(word in message.content for word in quotes_hint) and any(word in message.content for word in weby):
        await message.channel.send(get_quote())

    # Wishing happy birthday if birthday related word found
    elif any(word in message.content for word in birthday_hint) and any(word in message.content for word in weby):
        await message.channel.send(random.choice(birthday_ups))

    # Sending today news if news related cordinates found
    elif any(word in message.content for word in news) and any(word in message.content for word in weby):
        for desc_news in auto_search():
            await message.channel.send(desc_news)

    # Completing query of sender
    elif any(word in message.content for word in weby):
        await message.channel.send(query_find(message.content))


client.run(os.environ.get("DISCORD"))
