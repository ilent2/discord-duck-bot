
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
UNAMES = os.getenv('DISCORD_UNAMES').strip().split(', ')

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

@bot.command(name="goose", help="We don't like gooses here, go somewhere else")
async def send_goose_link(ctx):

    msg = "https://goose.game/";
    await ctx.send(msg)

@bot.command(name="niceroll", help="A better dice roller")
async def send_goose_link(ctx, *, arg):

    user_name = str(ctx.author)
    if user_name == UNAMES[0]:
        dtype = 2

    elif user_name == UNAMES[1]:
        dtype = 0

    elif user_name == UNAMES[2]:
        dtype = 20

    elif user_name == UNAMES[3]:
        dtype = 6

    else:
        print('Unknown user: ' + user_name)
        dtype = 0

    # Parse input
    parts = arg.split('+')
    parts = [p.split('-') for p in parts]

    dice = []

    def roll(num, sides):
        return [random.randint(1, sides) for _ in range(num)]

    def parse_part(part):

        if type(part) is str and 'd' in part:
            num, sides = [int(n) for n in part.split('d')]

            if dtype != 0:
                rolls = roll(num, dtype)
            else:
                rolls = roll(num, sides)

            dice.extend(rolls)
            return sum(rolls)

        else:
            return int(part)


    for ii in range(len(parts)):
        for jj in range(len(parts[ii])):

            parts[ii][jj] = parse_part(parts[ii][jj])

        if len(parts[ii]) > 1:
            parts[ii] = parts[ii][0] - sum(parts[ii][1:])
        else:
            parts[ii] = parse_part(parts[ii][0])

    result = sum(parts)

    msg = ("You rolled [" + ', '.join([str(d) for d in dice]) + '] : ' +
        str(result))

    await ctx.send(msg)

bot.run(TOKEN)

