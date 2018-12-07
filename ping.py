import discord
from discord.ext import commands
import time

client = commands.Bot(description="Our Official Bot", command_prefix=commands.when_mentioned_or("<bot prefix>"), pm_help = True)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')

@client.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    await client.say("Ping: {}ms".format(round((t2-t1)*1000)))
    
client.run('Token')
