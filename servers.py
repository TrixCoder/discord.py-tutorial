import discord
from discord.ext import commands
import asyncio

client = commands.Bot(description="Our Official Bot", command_prefix=commands.when_mentioned_or("<bot prefix here>"), pm_help = True)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    
def is_owner(ctx):
    return ctx.message.author.id == "<Your id>"

@client.command(pass_context = True)
@commands.check(is_owner)
async def servers(ctx):
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))
  
client.run('Token')
