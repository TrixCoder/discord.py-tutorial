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

def is_owner(ctx):
    return ctx.message.author.id == "Your id here" #replace_it_with_your_discord_id

@client.command(pass_context = True) #command_to_stop_your_bot_using-<prefix>shutdown
@commands.check(is_owner)
async def shutdown():
    await client.logout()
    
@client.event #adds_symbol_or_text_before_member's_nick_when_he_joins_a_particular_server
async def on_member_join(member):
    if member.server.id == "ServerID here":
     print("In our server" + member.name + " just joined")
     nickname = 'symbol/text here' + member.name #add_the_symbol_or_text_that_u_wanna__your_bot_add_before_a_member's_name_when_he/she_joins_your_server
     await client.change_nickname(member, nickname)
 
@client.event #welcomes_user_in_dm_on_member_join
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server rules and never try to break any rules. Also join our official server- https://discord.gg/vMvv5rr**',inline = False) #change_this_message_with_your_msg_that_you_wanna_ur_bot_send_in_dm_when_a_user_joins
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
   
    print("Sent message to " + member.name)

client.run('BOT TOKEN HERE') #add_your_bot_token_here
