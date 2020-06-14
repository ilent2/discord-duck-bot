
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
UNAMES = os.getenv('DISCORD_UNAMES').strip().split(', ')

_dtypes = {
    UNAMES[0]: 2,
    UNAMES[1]: 0,
    UNAMES[2]: 20,
    UNAMES[3]: 6,
}

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
    dtype = _dtypes.get(user_name, 0)

    # Parse input
    parts = arg.split('+')
    parts = [p.split('-') for p in parts]

    dice = []

    def roll(num, sides):
        return [random.randint(1, sides) for _ in range(num)]

    def parse_part(part):

        if isinstance(part, str) and 'd' in part:
            num, sides = [int(n) for n in part.split('d', maxsplit=1)]

            rolls = roll(num, sides if dtype == 0 else dtype)

            dice.extend(rolls)
            return sum(rolls)

        return int(part)

    parts = [[parse_part(p) for p in part] for part in parts]
    for i, part in enumerate(parts):
        if len(part) > 1:
            parts[i] = part[0] - sum(part[:1])
        else:
            parts[i] = parse_part(part[0])

    result = sum(parts)

    msg = ("You rolled [" + ', '.join([str(d) for d in dice]) + '] : ' +
        str(result))

    await ctx.send(msg)

bot.run(TOKEN)

