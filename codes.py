import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp
from discord.utils import get
from random import choice, shuffle


commandprefix = "alexa "

client = commands.Bot(command_prefix=commandprefix)
client.remove_command('help')

   
async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='with ' + str(len(set(client.get_all_members())))+' members'))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name='in ' + str(len(client.servers))+' servers'))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="Fortnite"))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="for alexa help"))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="So thankful to DarkLegend"))
        await asyncio.sleep(3)
@client.event
async def on_ready():
    ...
    client.loop.create_task(status_task())   
  


@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)
print('tweet online')

@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to change nickname. Example- ``alexa setnick @user/all <new nickname>``')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)

@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def resetnick(ctx, user: discord.Member=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to reset nickname. Example- ``alexa resetnick @user/all``')
      return
    else:
      nick = user.name
      await client.change_nickname(user, nick)
      await client.delete_message(ctx.message)           
 	
@client.command(pass_context=True)
async def hack(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-Starting Hacking Tool.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-Starting Hacking Tool..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-Hacking Tool Started...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-Starting to hack.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-Searching fb password..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-Searching discord password.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-Killing Whole System...``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Showing Results {}- Discord Hacker``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Downloading File  |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Downloading File..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Files Downloaded... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Showing Results....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`I Found This:-\n FB password-fuckingking333 \n Discord password- MegaNigga2277 \n '.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. Change your passwords now.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You are hacked. Change your passwords right now.``'.format(hack))

@client.command(pass_context = True)
async def deletechannel(ctx, channel: discord.Channel=None):
    if channel is None:
        await client.delete_channel(ctx.message.channel)
        await client.send_message(ctx.message.author, "{} channel has been deleted in {}".format(ctx.message.channel.name, ctx.message.server.name))
    else:
        if ctx.message.author.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            await client.delete_channel(channel)
            await client.say("{} channel has been deleted.".format(channel.name))
@client.command(pass_context = True)
async def rainbow(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Rainbow')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.edit_role(ctx.message.server, role, color = discord.Color((r << 16) + (g << 8) + b))            
@client.command(pass_context=True)
async def play(ctx):
    await client.say("Sorry dude! This Command is not available.")         
@client.command(pass_context=True)
async def hi(ctx):
    await client.say("Hello There!")
    print ("reply Posted")
    
@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Pong: {}ms".format(round((t2-t1)*1000)))
@client.command(pass_context = True)
async def roll(ctx):
    choices = ['1', '2', '3', '4', '5', '6', 'Nothing']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='You Rolled', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)
@client.command(pass_context = True)
async def charliecharlie(ctx):
    choices = ['Yes!', 'No!', 'No!', 'Yes!']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Its Charlie Here', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)    
@client.command(pass_context = True)
async def howgay(ctx):
    choices = ['50%', '20%', '30%', '40%', '10%', '60%', '70%','80%', '90%', '100%', 'You Are Not Gay!']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Gay Percentage', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)    
@client.command(pass_context = True)
async def toss(ctx):
    choices = ['Head', 'Tail', 'Nothing']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)
@client.command(pass_context = True)
async def addchannel(ctx, channel: str=None):
    server = ctx.message.server
    if channel is None:
        await client.say("Please specify a channel name")
    else:
        if ctx.message.author.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            everyone_perms = discord.PermissionOverwrite(send_messages=None, read_messages=None)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            await client.create_channel(server, channel, everyone)
            await client.say("{} channel has been created.".format(channel))
@client.command(pass_context = True)
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))
    else:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("Channel was locked by: {}".format(ctx.message.author))
@client.command(pass_context = True)
async def setupwelcome(ctx):
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.administrator == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★彡-welcome-bye彡★',everyone)	
@client.command(pass_context = True)
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("Channel was unlocked by: {}".format(ctx.message.author))
    else:
        if ctx.message.author.server_permissions.kick_members == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("Channel was unlocked by: {}".format(ctx.message.author))
@client.command(pass_context = True)
async def say(ctx, *args):
    message = ' '.join(args)
    return await client.say(message)
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.add_field(name = 'Commands Of Dynamic Anion',value ='**coins (Note:- Coins depends upon your level. Level 1=1 coin & level 2=2 coins.)**\n**purge <1-100>**\n** botinfo**\n** ban**\n**clearwarn**\n**warn**\n** kick**\n**mute**\n**mvjoin**\n** unmute**\n**charliecharlie**\n**poll**\n**userinfo**\n**meme**\n**ping**\n**toss**\n**roll**\n**howgay**\n**hack**\n**virus**\n**addrole**\n**deleterole**\n**addchannel**\n**tweet**\n**deletechannel**\n**setnick**\n**resetnick**\n**marklink**\n**serverinvite**',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      await client.say('📨 Check DMs For Information')
      await asyncio.sleep(30)
      await client.delete_message(dmmessage)
@client.command(pass_context = True)
async def announce(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if channel is None or msg is None:
        await client.say('Invalid args. Use this command like ``alexa announce #channel text here``')
        return
    else:
        if member.server_permissions.administrator == False:
            await client.say('**You do not have permission to use this command**')
            return
        else:
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
            await client.send_message(channel, embed=embed)
            await client.delete_message(ctx.message)
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-bye彡★':
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check #rules and never try to break any one of them. Thank You.', color = 0x36393E)
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await asyncio.sleep(0.4)
            await client.send_message(channel, embed=embed) 
@client.command(pass_context = True)
async def addrole(ctx,*, role:str=None):
    user = ctx.message.author
    if user.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await client.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await client.say("{} role has been added.".format(role))
        return
    else:
        await client.say("{} role is already exists".format(role))
@client.command(pass_context = True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("No such role found")
        return
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="{}'s info".format(role.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = ctx.message.server.icon_url)
        embed.add_field(name="Name", value=role.name, inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="Color", value=role.color)
        embed.add_field(name="Created", value=role.created_at.strftime("%d %b %Y %H:%M"))
        await client.say(embed=embed)
@client.command(pass_context = True)
async def deleterole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("There is no role with this name in this server")
    if ctx.message.author.server_permissions.manage_roles == False:
        await client.say('**You do not have permission to use this command**')
        return
    else:
        await client.delete_role(ctx.message.server, role)
        await client.say(f"{role} role has been deleted")                            
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-bye彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await client.send_message(channel, embed=embed)        
@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))

@client.command(pass_context = True)
async def marklink(ctx):
        embed=discord.Embed(title="**GLAD TO JOIN YOUR SERVER**", description="https://discordapp.com/oauth2/authorize?client_id=538276094004953089&permissions=2146958591&scope=bot".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed) 

@client.command(pass_context = True)
async def serverinvite(ctx):
        embed=discord.Embed(title="**Link Of Anion's Server:-**", description="https://discord.gg/psaVdQH".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed) 
@client.command(pass_context = True)
async def mvjoin(ctx):
        embed=discord.Embed(title="**Link Of MV Official Server:-**", description="https://discord.gg/zctquWb".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed) 
@client.command(pass_context = True)
async def anionyt(ctx):
        embed=discord.Embed(title="**HERE IS THE LINK OF ANIMATION ANION**", description="https://www.youtube.com/channel/UCR8wChQMAAlTvJu3vNX_vMA".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)         

  
@client.command(pass_context = True)
async def botinfo(ctx):
        embed=discord.Embed(title="**INFORMATIONS OF ANION BOT**", description="**Name- Dynamic Anion**\n**Creator- Allipsters Gaming**\n**Official Server- Anion States**\n**Bot Type- Private**\n**Discord.py**".format(member, ctx.message.author), color=0x7289da)
        await client.say(embed=embed)
        print ("helped")        
@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.kick(userName)
        embed=discord.Embed(title="**User Kicked Successfully!**", description="**The User was successfully Kicked!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="**User unmuted!**", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member=None, mutetime=None):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="**User muted!**", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
      await client.say('Please tag a user to get user information. Example- ``alexa userinfo @user``')
    if ctx.message.author.bot:
      return
    if ctx.message.author.server_permissions.kick_members == False:
      await client.say('**You do not have permission to use this command**')
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find about the user.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.mention, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Color", value=user.color)
      embed.add_field(name="Playing", value=user.game)
      embed.add_field(name="Nickname", value=user.nick)
      embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))
      embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)        
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} was kissed by {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None): 
    if userName is None:
      await client.say('Please tag a person to warn user. Example- ``alexa warn @user <reason>``')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say("***Alright! {0} Has Been Warned for {1}.*** ".format(userName,message))
      for channel in userName.server.channels:
        if channel.name == 'action-logs':
            embed=discord.Embed(title="User Warned!", description="{0} warned by {1} for {2}".format(userName, ctx.message.author, message), color=0x0521F6)
            await client.send_message(channel, embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def clearwarn(ctx, userName: discord.User=None,*, message:str=None):  
  if userName is None:
      await client.say('Please tag a person to warn user. Example- ``alexa clearwarn @user``')
      return
  else: 
      await client.say("***Warnings of {0} Has Been Cleared.*** ".format(userName,message))           
@client.command(pass_context = True)
async def dms(ctx, user: discord.Member, *, msg: str):
   if user is None or msg is None:
       await client.say('Invalid args. Use this command like: ``alexa dms @user message``')
   if ctx.message.author.server_permissions.kick_members == False:
       await client.say('**You do not have permission to use this command**')
       return
   else:
       await client.send_message(user, msg)
       await client.delete_message(ctx.message)          
       await client.say("Success! Your DMS is done! :white_check_mark: ")
@client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.ban(userName)
        embed=discord.Embed(title="**User Banned Successfully!**", description="**The User was successfully Banned!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx, identification:str):
    user = await client.get_user_info(identification)
    await client.unban(ctx.message.server, user)
    try:
        await client.say(f'`{user}` has been unbanned from the server.')
        for channel in ctx.message.server.channels:
          if channel.name == 'action-logs':
              embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(user, ctx.message.author), color=0x38761D)
              await client.send_message(channel, embed=embed)
    except:
        await client.say(f'Unable to unban `{user}`')
        pass
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
	
@client.command(pass_context = True)
async def meme(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title='Random Meme', description='Random meme :joy:', color = discord.Color((r << 16) + (g << 8) + b))
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'This meme was requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)
@client.command(pass_context=True)
async def invites(ctx, user:discord.Member=None):
    if ctx.message.server.id == '538244278824992778':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        if user is None:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == ctx.message.author:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter I')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter II')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter III')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter IV')
                if role in ctx.message.author.roles:
                    return
                else:
                    await client.add_roles(ctx.message.author, role)
                    await client.say('Congrats! You have got Inviter IV role')
        else:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == user:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(user.server.roles, name='Inviter I')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name}, You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(user.server.roles, name='Inviter II')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(user.server.roles, name='Inviter III')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(user.server.roles, name='Inviter IV')
                if role in user.roles:
                    return
                else:
                    await client.add_roles(user, role)
                    await client.say(f'Congrats! {user.name} You have got Inviter IV role')
    else:
        await client.say('You are not allowed to use this command in this server')
        return 
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def totalbans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "Here Is The List of The Banned Members/Bots Of This Server", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.event
async def on_message(message):
    user_add_xp(message.author.id, 2)
    await client.process_commands(message)
    if message.content.lower().startswith('alexa rank'):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        level=int(get_xp(message.author.id)/100)
        msgs=int(get_xp(message.author.id)/2)
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Dynamic Rank')
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.add_field(name = '**__XP__**'.format(message.author),value ='``{}``'.format(get_xp(message.author.id)),inline = False)
        embed.add_field(name = '**__Level__**'.format(message.author),value ='``{}``'.format(level),inline = False)
        embed.add_field(name = '**__Total Messages Sent__**'.format(message.author),value ='``{}`` Messages'.format(msgs),inline = False)
        embed.add_field(name='All I Have To Say Is:-',value='Please Make This Server Alive And Get More Ranks.')
	embed.add_field(name='Note:',value='DYNAMIC ANION will show only daily ranks.')
        await client.send_message(message.channel, embed=embed)
    if message.content.lower().startswith('alexa coins'):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        level=int(get_xp(message.author.id)/100)
        msgs=int(get_xp(message.author.id)/2)
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Daily Coins')
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.add_field(name = '**__Coins__**'.format(message.author),value ='``{}``'.format(level),inline = False)
        embed.add_field(name='At Last:',value='All I have to say is, You are doing good.')
        await client.send_message(message.channel, embed=embed)
def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0



@client.command(pass_context=True)
async def ytsearch(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await client.say(url)        


@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def stats(ctx, *args):
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Server Stats")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)	

client.run(os.getenv('bottoken'))
