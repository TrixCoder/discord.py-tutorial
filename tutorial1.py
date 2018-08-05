import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="BOT DESCRIPTION HERE", command_prefix="BOT PREFIX HERE", pm_help = False) #add_your_bot_description_with_prefix_here

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started <BOTNAME HERE>') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='<BOT STATUS HERE>')) #add_your_bot_status_here

@client.command()
async def ping(*args):
	await client.say("COMMAND RESPONCE HERE")

client.run('BOT TOKEN HERE') #add_your_bot_token_here
