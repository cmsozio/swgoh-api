import os

import discord
from discord.ext import commands

# Load up .env variables
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

import swgoh_parser

swgoh = swgoh_parser.SWGOHParser()

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='characters')
async def characters(ctx):
    content = ctx.message.content.split()
    content.pop(0)
    allycodes = []
    for allycode in content:
        if '-' in allycode:
            await ctx.send(content='Ally code must be a number, do not add \'-\' in your ally codes.')
            return
        try:
            allycode = int(allycode)
        except:
            await ctx.send(content='Ally code must be a number.')
            return
        allycodes.append(allycode)
    message = swgoh.get_player_characters(allycodes)
    for mes in message:
        await ctx.send(content=mes)

bot.run(TOKEN)