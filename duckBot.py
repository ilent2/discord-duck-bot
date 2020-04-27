
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

file_list = ['001.jpg', '002.jpg', '003.jpg', '004.jpg',
        '005.jpg', '006.jpg', '007.jpg', '008.jpg', '009.jpg', '010.jpg'];

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!duck'):
        print('There was a duck request')

        file = discord.File('ducks/' + random.choice(file_list),
                filename='duck.jpg')
        embed = discord.Embed()
        embed.set_image(url="attachment://duck.jpg")

        await message.channel.send(file=file, embed=embed)

client.run(TOKEN)

