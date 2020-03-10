import os

import discord

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

@client.event
async def on_member_join(self, member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord Server!')

client.run(TOKEN)