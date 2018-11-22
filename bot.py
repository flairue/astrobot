# Work with Python 3.6
import random
import asyncio
import aiohttp
#import config

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = COMMANDPREF
TOKEN = TOKEN

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)

@client.event
async def on_message(message):
    # If the message author isn't the bot and the message starts with the
    # command prefix ('!' by default), check if command was executed
    if message.author.id != BOTID and message.content.startswith(BOT_PREFIX):
        # Remove prefix and change to lowercase so commands aren't case-sensitive
        message.content = message.content[1:].lower()

        # Shuts the bot down - only usable by the bot owner specified in config
        if message.content.startswith('shutdown') and message.author.id == OWNERID:
            await client.send_message(message.channel, 'Shutting down. Bye!')
            await client.logout()
            await client.close()

        # Allows owner to set the game status of the bot
        elif message.content.startswith('status') and message.author.id == OWNERID:
            await client.change_presence(game=discord.Game(name=message.content[7:]))

        # Help Message, sends a personal message with a list of all the commands
        # and how to use them correctly
        elif message.content.startswith('help'):
            import helpMessage
            #await client.send_message(message.channel, 'Sending you a PM!')
            #await client.send_message(message.author, helpMessage.help)
            await client.send_message(message.channel, helpMessage.help)

        #APOD
        elif message.content.startswith('apod'):
            import astropic
            try:
                url, title, expl = astropic.getAPOD(message.content)
                await client.send_message(message.channel, url)
                await client.send_message(message.channel, '**' + title
                                          + '**' + '\n ```' + expl + '```')
            except:
                await client.send_message(message.channel, 'Check your date, maybe?')

        #Fetching wikipedia page summary
        elif message.content.startswith('wiki'):
            import wiki
            await client.send_message(message.channel, wiki.wksum(message.content))

        #DateTime, needs so many improvements. This is just a placeholder.
        elif message.content.startswith('whattime'):
            import datecalc
            await client.send_message(message.channel, datecalc.whine)
            await client.send_message(message.channel, datecalc.now(message.content))

        #Moon phases
        elif message.content.startswith('moon'):
            import moon
            await client.send_message(message.channel, moon.phase(message.content))

        #Secret message for my bro
        elif message.content.startswith('anas'):
            await client.send_message(message.channel, 'ANASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')



async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
