
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

file_list = ['001.jpg', '002.jpg', '003.jpg', '004.jpg',
        '005.jpg', '006.jpg', '007.jpg', '008.jpg', '009.jpg', '010.jpg'];

bot = commands.Bot(command_prefix='!')

@bot.command(name="duck", help="Display one of 10 random ducks")
async def send_duck(ctx):

    print('There was a duck request')

    file = discord.File('ducks/' + random.choice(file_list),
            filename='duck.jpg')

    embed = discord.Embed()
    embed.set_image(url="attachment://duck.jpg")

    await ctx.send(file=file, embed=embed)

bot.run(TOKEN)

