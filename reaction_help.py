import discord
import asyncio
from discord.ext import commands

client = commands.Bot(description="MultiVerse Official Bot", command_prefix="mv!", pm_help = True)
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started BOT')

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = 'mv!donate',value ='Sends donation link',inline = False)
        embed.add_field(name = 'mv!invite or mv!authlink',value ='Use it to invite our bot to your server',inline = False)
        embed.add_field(name = 'mv!upvote',value ='Use this command to upvote our bot(Link will be in dm)',inline = False)
        embed.add_field(name = 'mv!meme',value ='Use this command to get random memes.(Sometimes it sends same meme again and again)',inline = False)
        embed.add_field(name = 'mv!serverinvite ',value ='Use it to get server invite link.',inline = False)
        embed.add_field(name = 'mv!rolldice',value ='Use it like ``mv!rolldice <1-6 any number that you want to guess in dice>``',inline = False)
        embed.add_field(name = 'mv!avatar',value ='Use it like ``mv!avatar or mv!avatar @user``',inline = False)
        embed.add_field(name = 'mv!ping',value ='Use it to check ping of bot',inline = False)
        embed.add_field(name = 'mv!flipcoin',value ='Use it like ``mv!rolldice <Your prediction>`` prediction = heads, tails or coin self destructed)``',inline = False)
        embed.add_field(name = 'mv!enterme',value ='Use it like ``mv!enterme <giveaway channel>`` to enter in a giveaway running in a particular channel',inline = False)
        embed.add_field(name = 'mv!poll ',value ='Use it like ``mv!poll "Question" "Option1" "Option2" ..... "Option9"``.',inline = False)
        embed.add_field(name = 'mv!guess ',value ='To play guess game use ``mv!guess <number> and number should be between 1-10``',inline = False)
        embed.add_field(name = 'mv!github ',value ='Use it like- ``mv!github uksoftworld/DarkBot``',inline = False)
        embed.add_field(name = 'mv!bottutorial ',value ='Use it like ``mv!bottutorial <tutorial name by darklegend>``',inline = False)
        embed.add_field(name = 'mv!dyno ',value ='Use it like ``mv!dyno <dyno command name>``',inline = False)
        embed.add_field(name = 'mv!happybirthday @user ',value ='To wish someone happy birthday',inline = False)
        embed.add_field(name = 'mv!verify ',value ='Use it to get verified role. Note- It needs proper setup.',inline = False)
        await client.send_message(user,embed=embed)
      if reaction.emoji == '🇲':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'mv!partner(Admin permission required) (Cooldown of 12hours)',value ='Use it like ``mv!partner <partnership description>`` to partner with many servers with are connected with MultiVerse Official bot',inline = False)
        embed.add_field(name = 'mv!dm(Admin permission required) ',value ='Use it like ``mv!dm @user <text>`` to dm user from bot',inline = False)
        embed.add_field(name = 'mv!say(Admin permission required) ',value ='Use it like ``mv!say <text>``',inline = False)
        embed.add_field(name = 'mv!showme(Requires a role named Giveaways)',value ='To see how many people are taking part in giveaway',inline = False)
        embed.add_field(name = 'mv!pickwinner(Requires a role named Giveaways)',value ='To pick winner',inline = False)
        embed.add_field(name = 'mv!embed(Admin permission required) ',value ='Use it like ``mv!embed <text>``',inline = False)
        embed.add_field(name = 'mv!membercount(Kick members Permission Required) ',value ='Use it like ``mv!membercount`` to get membercount',inline = False)
        embed.add_field(name = 'mv!removemod(Admin Permission Required)',value ='Use it like ``mv!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
        embed.add_field(name = 'mv!makemod(Admin Permission Required)',value ='Use it like ``mv!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
        embed.add_field(name = 'mv!friend(Admin Permission Required) ',value ='Use it like ``mv!friend @user`` to give anyone Friend of Owner role',inline = False)
        embed.add_field(name = 'mv!role(Manage Roles Permission Required)',value ='Use it like ``mv!role @user <rolename>``.',inline = False)
        embed.add_field(name = 'mv!setnick(Manage nickname permission required)',value ='Use it like ``mv!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
        embed.add_field(name = 'mv!english(Kick members Permission Required)',value ='Use it like ``mv!english @user`` when someone speaks languages other than English.',inline = False)
        embed.add_field(name = 'mv!serverinfo(Kick members Permission Required) ',value ='Use it like ``mv!serverinfo`` to get server info',inline = False)
        embed.add_field(name = 'mv!userinfo(Kick members Permission Required) ',value ='Use it like ``mv!userinfo @user`` to get some basic info of tagged user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏭'
        await client.add_reaction(react_message, reaction)
    
      if reaction.emoji == '⏭':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'mv!unbanall(Unban members Permission Required)',value ='Use it like ``mv!unbanall`` to unban all members',inline = False)
        embed.add_field(name = 'mv!kick(Kick members Permission Required)',value ='Use it like ``mv!kick @user`` to kick any user',inline = False)
        embed.add_field(name = 'mv!roles(Kick members Permission Required) ',value ='Use it to check roles present in server',inline = False)
        embed.add_field(name = 'mv!clear(Manage Messages Permission Required)',value ='Use it like ``mv!purge <number>`` to clear any message',inline = False)
        embed.add_field(name = 'mv!mute(Mute members Permission Required)',value ='Use it like ``mv!mute @user <time in minutes>`` to mute any user. **Note-You need to add Muted role in your server if it is not already there also you must need to change permission of all channels and disable send_message permission for Muted role.**',inline = False)
        embed.add_field(name = 'mv!unmute(Mute members Permission Required) ',value ='Use it like ``mv!unmute @user`` to unmute anyone',inline = False)
        embed.add_field(name = 'mv!ban(Ban members Permission Required) ',value ='Use it like ``mv!ban @user`` to ban any user',inline = False)
        embed.add_field(name = 'mv!rules(Kick members Permission Required)',value ='Use it like ``mv!rules @user <violation type>`` to warn user',inline = False)
        embed.add_field(name = 'mv!warn(Kick members Permission Required)',value ='Use it like ``mv!warn @user <violation type>`` to warn any user',inline = False)    
        embed.add_field(name = 'mv!norole(Kick members Permission Required) ',value ='Use it like ``mv!norole @user`` to warn anyone if he/she asks for promotion',inline = False)
        embed.add_field(name = 'mv!getuser(Kick members Permission Required) ',value ='Use it like ``mv!getuser @rolename`` to get list of all users having a particular role',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏮'
        await client.add_reaction(react_message, reaction)
    
      if reaction.emoji == '⏮':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Moderation Commands Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'mv!announce(Admin Permission required) ',value ='To make bot announce anything using ``mv!announce <channel> <msg>``. Note- It does not annoy people by tagging everyone or here.',inline = False)
        embed.add_field(name = 'mv!say(Admin permission required) ',value ='Use it like ``mv!say <text>``',inline = False)
        embed.add_field(name = 'mv!embed(Admin permission required) ',value ='Use it like ``mv!embed <text>``',inline = False)
        embed.add_field(name = 'mv!membercount(Kick members Permission Required) ',value ='Use it like ``mv!membercount`` to get membercount',inline = False)
        embed.add_field(name = 'mv!removemod(Admin Permission Required)',value ='Use it like ``mv!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
        embed.add_field(name = 'mv!makemod(Admin Permission Required)',value ='Use it like ``mv!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
        embed.add_field(name = 'mv!friend(Admin Permission Required) ',value ='Use it like ``mv!friend @user`` to give anyone Friend of Owner role',inline = False)
        embed.add_field(name = 'mv!role(Manage Roles Permission Required)',value ='Use it like ``mv!role @user <rolename>``.',inline = False)
        embed.add_field(name = 'mv!setnick(Manage nickname permission required)',value ='Use it like ``mv!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
        embed.add_field(name = 'mv!english(Kick members Permission Required)',value ='Use it like ``mv!english @user`` when someone speaks languages other than English.',inline = False)
        embed.add_field(name = 'mv!serverinfo(Kick members Permission Required) ',value ='Use it like ``mv!serverinfo`` to get server info',inline = False)
        embed.add_field(name = 'mv!userinfo(Kick members Permission Required) ',value ='Use it like ``mv!userinfo @user`` to get some basic info of tagged user',inline = False)
        react_message = await client.send_message(user,embed=embed)
        reaction = '⏭'
        await client.add_reaction(react_message, reaction)
      if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use mv!setupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
        embed.add_field(name = 'Setting up AutoPartner Channel(Admin Permission required)',value ='Using ``mv!setuppartner`` command create a channel named multiverse-partner and then you can use mv!partner to partner with other servers.',inline = False)
        embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``mv!help`` and check giveaway commands.',inline = False)
        embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``mv!setreactionverify`` it will automatically add a channel and post information about verification. **__Note__** **Sometimes it does not sends message in channel named #verify-for-chatting when this command is used so reuse that command in such case**',inline = False)
        embed.add_field(name = 'Setting up Multiverse bot log(Admin Permission required) ',value ='Use ``mv!setuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        await client.send_message(user,embed=embed)
	
      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'mv!wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = 'mv!cat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = 'mv!surprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = 'mv!angry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = 'mv!fearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = 'mv!dank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = 'mv!thinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = 'mv!thinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = 'mv!happy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = 'mv!santa',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = 'mv!lol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = 'mv!love',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = 'mv!mad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = 'mv!alien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = 'mv!hi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        await client.send_message(user,embed=embed)    
    
@client.event
async def on_message(message):
	await client.process_commands(message)
  
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/FrRtyS6',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('📨 Check DMs For Information')

client.run('Token')
