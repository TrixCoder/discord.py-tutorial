import discord
import asyncio
from discord.ext import commands

client = commands.Bot(description="BOT DESCRIPTION HERE", command_prefix="BOT PREFIX HERE", pm_help = False) #add_your_bot_description_with_prefix_here

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+'')
    print('--------')
    print('--------')
    print('Started <BOTNAME HERE>') #add_your_bot_name_here
    return await client.change_presence(game=discord.Game(name='<BOT STATUS HERE>')) #add_your_bot_status_here

@client.command(pass_context=True)
async def ping(ctx): #replace_ping_from_any_other_command_name_like_hu,hello,etc
    await client.say("COMMAND RESPONCE HERE") #replace_responce_with_any_responce_that__you_want_when_command_is_used

client.run('BOT TOKEN HERE') #add_your_bot_token_here
