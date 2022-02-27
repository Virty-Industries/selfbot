#!/usr/bin/env python
# -*- coding: utf-8 -*-


# IMPORTS

from asyncio.tasks import sleep, wait
from colorama.ansi import clear_screen
import discord, json, ctypes, os, random, asyncio, requests, aiohttp, asyncio, time, datetime, re, httpx, contextlib, base64, urllib, urllib.request, sys, threading
from discord import channel
import PIL
from discord import guild
from discord.ext import commands
import json
import os
from typing import IO
import asyncio
from faker import Faker
from discord import Webhook, AsyncWebhookAdapter, Spotify
import ctypes
from colorama import Fore, Back, Style
from colorama import init
import random
import io
import requests
import threading
import subprocess
import asyncio
import random
import string
import sys
import time
import psutil
import getpass
import base64
from plyer import notification
from plyer import *
from plyer import platforms
import urllib
import re
from discord.ext.commands import *
from art import *
import playsound
from datetime import datetime
import jwt

# HARDWAREID
def GetUUID():
    if sys.platform == "win32":
        cmd = 'wmic csproduct get uuid'
        uuid = str(subprocess.check_output(cmd))
        pos1 = uuid.find("\\n")+2
        uuid = uuid[pos1:-15]
    else:
        try:
            uuid = os.popen("lscpu | grep -E 'family|cache|Model|Hypervisor|Core|CPU(s)|Architecture|op-mode|Socket|Vendor|Virtualization|Flags'").read()
        except:
            print("Please install util-linux")
    return uuid

# SECURITY
for proc in psutil.process_iter():
    try:
        processName = proc.name()
        if processName == "HTTPDebuggerUI.exe":
            proc.terminate()
        if processName == "HTTPDebuggerSvc.exe":
            proc.terminate()
    except:
        pass



m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:",       
    ":six:"
]

# COLORS
class color:
    black = "\u001b[0m"+"\u001b[30m"
    gray = "\u001b[0m"+"\u001b[38;5;244m"
    darkgray = "\u001b[0m"+"\u001b[38;5;237m"
    red = "\u001b[0m"+"\u001b[31m"
    green = "\u001b[0m"+"\u001b[38;5;46m"
    yellow = "\u001b[0m"+"\u001b[38;5;226m"
    blue = "\u001b[0m"+"\u001b[38;5;26m"
    blue1 = "\u001b[0m"+"\u001b[38;5;69m"
    magenta = "\u001b[0m"+"\u001b[35m"
    cyan = "\u001b[0m"+"\u001b[36m"
    white = "\u001b[0m"+"\u001b[37m"
    reset = "\u001b[0m"+"\u001b[0m"

class bright:
    black = "\u001b[30;1m"
    red = "\u001b[38;5;9m"
    blue = "\u001b[38;5;26m"
    yellow = "\u001b[33;1m"
    blue = "\u001b[34;1m"
    magenta = "\u001b[35;1m"
    cyan = "\u001b[36;1m"
    white = "\u001b[37;1m"

class theme:
    logomaincolor = color.blue1
    logoshadowcolor = color.blue1
    color1 = color.blue1
    color2 = color.white
    color3 = color.darkgray

# DEF
apidomain = "virty.xyz/panel/"

# MOTD 
motd = requests.get(f'https://{apidomain}api/info.php').json()['motd']

# VERSION
version = requests.get(f'https://{apidomain}api/info.php').json()['version']

if not os.path.exists('auth.json'):
    print(color.red+'[AUTH]'+color.reset+' You are not logged in!')
    username = input('[AUTH] Username >> ')
    password = getpass.getpass('[AUTH] Password >> ')
    hwid = GetUUID()
    auth = requests.get(f'https://virty.xyz/panel/api/auth.php?user={username}&pass={password}&hwid={hwid}')
    authdata = json.loads(auth.text)
    token = authdata['token']
    if auth.content == b"User not found":
        print(color.red+'[AUTH]'+color.reset+' User not found!')
        sys.exit()
    if auth.content == b"Wrong password":
        print(color.red+'[AUTH]'+color.reset+' Wrong password!')
        sys.exit()
    if auth.content == b"Wrong hwid":
        print(color.red+'[AUTH]'+color.reset+' Wrong hwid!')
        sys.exit()
    if auth.content == b"User banned":
        print(color.red+'[AUTH]'+color.reset+' You are banned!')
        sys.exit()
    decode = jwt.decode(token, 'password', algorithms=['HS512'])
    data = {}
    data = ({
        "username": decode['username'],
        "password": decode['password'],
        "hwid": decode['hwid'],
    })
    with open('auth.json', 'w') as f:
        json.dump(data, f)
        print(color.green+'[AUTH]'+color.reset+' You are logged in!')
else:
    with open('auth.json') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']
        hwid = data['hwid']
        auth = requests.get(f'https://virty.xyz/panel/api/auth.php?user={username}&pass={password}&hwid={hwid}')
        authdata = json.loads(auth.text)
        token = authdata['token']
        decode = jwt.decode(token, 'password', algorithms=['HS512'])
        if decode['username'] != username:
            print(color.red+'[AUTH]'+color.reset+' Username or Password are wrong!')
            sys.exit()
        if decode['password'] != password:
            print(color.red+'[AUTH]'+color.reset+' Username or Password are wrong!')
            sys.exit()
        if decode['hwid'] != hwid:
            print(color.red+'[AUTH]'+color.reset+' Hwid is wrong!')
            sys.exit()


# CONFIG
if not os.path.exists('config.json'):
    print('\n')    
    print(color.magenta + f'██╗   ██╗██╗██████╗ ████████╗██╗   ██╗'.center(os.get_terminal_size().columns))
    print(color.magenta + f'██║   ██║██║██╔══██╗╚══██╔══╝╚██╗ ██╔╝'.center(os.get_terminal_size().columns))
    print(color.magenta + f'██║   ██║██║██████╔╝   ██║    ╚████╔╝'.center(os.get_terminal_size().columns))
    print(color.magenta + f'╚██╗ ██╔╝██║██╔══██╗   ██║     ╚██╔╝'.center(os.get_terminal_size().columns))
    print(color.magenta + f' ╚████╔╝ ██║██║  ██║   ██║      ██║ '.center(os.get_terminal_size().columns))
    print(color.magenta + f'  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝ \n'.center(os.get_terminal_size().columns))
    print('[CONFIG] Creating config file!')
    token = input('[CONFIG] Token >> ')
    prefix = input('[CONFIG] Prefix >> ')
    embed_delete = 30
    theme = 'virty.json'
    nitro_redeem_notify = input('[CONFIG] Nitro redeem notify (y/n) >> ')
    if nitro_redeem_notify == 'y':
        nitro_redeem_notify = True
    else:
        nitro_redeem_notify = False

    giveaway_win_notify = input('[CONFIG] Giveaway win notify (y/n) >> ')
    if giveaway_win_notify == 'y':
        giveaway_win_notify = True
    else:
        giveaway_win_notify = False

    ghost_mode = input('[CONFIG] Ghost mode (y/n) >> ')
    if ghost_mode == 'y':
        ghost_mode = True
    else:
        ghost_mode = False

    safe_mode = input('[CONFIG] Embed mode (y/n) >> ')
    if safe_mode == 'y':
        safe_mode = True
    else:
        safe_mode = False

    nitro_sniper = input('[CONFIG] Nitro sniper (y/n) >> ')
    if nitro_sniper == 'y':
        nitro_sniper = True
    else:
        nitro_sniper = False

    nitro_sound = input('[CONFIG] Nitro sound (y/n) >> ')
    if nitro_sound == 'y':
        nitro_sound = True
    else:
        nitro_sound = False

    giveaway_sniper = input('[CONFIG] Giveaway sniper (y/n) >> ')
    if giveaway_sniper == 'y':
        giveaway_sniper = True
    else:
        giveaway_sniper = False

    giveaway_sound = input('[CONFIG] Giveaway sound (y/n) >> ')
    if giveaway_sound == 'y':
        giveaway_sound = True
    else:
        giveaway_sound = False

    dm_logs = input('[CONFIG] DM logs (y/n) >> ')
    if dm_logs == 'y':
        dm_logs = True
    else:
        dm_logs = False

    new_friend_notify = input('[CONFIG] New friend notify (y/n) >> ')
    if new_friend_notify == 'y':
        new_friend_notify = True
    else:
        new_friend_notify = False

    with open('config.json', 'w') as f:
        data = {}
        data = ({
            'token' : token,
            'prefix' : prefix,
            'embed_delete' : embed_delete,
            'theme' : theme,
            'nitro_redeem_notify' : nitro_redeem_notify,
            'giveaway_win_notify' : giveaway_win_notify,
            'ghost_mode' : ghost_mode,
            'safe_mode' : safe_mode,
            'nitro_sniper' : nitro_sniper,
            'nitro_sound' : nitro_sound,
            'giveaway_sniper' : giveaway_sniper,
            'giveaway_sound' : giveaway_sound,
            'dm_logs' : dm_logs,
            'new_friend_notify' : new_friend_notify
        })
        json.dump(data, f)
else:
    with open('config.json', 'r') as f:
        data = json.load(f)
    token = data['token']
    prefix = data['prefix']
    embed_delete = data['embed_delete']
    nitro_redeem_notify = data['nitro_redeem_notify']
    giveaway_win_notify = data['giveaway_win_notify']
    ghost_mode = data['ghost_mode']
    safe_mode = data['safe_mode']
    nitro_sniper = data['nitro_sniper']
    nitro_sound = data['nitro_sound']
    giveaway_sniper = data['giveaway_sniper']
    giveaway_sound = data['giveaway_sound']
    dm_logs = data['dm_logs']

virty = '''{
  "embed_title": "Virty | Selfbot",
  "embed_color": "#4100b3",
  "embed_thumbnail": "https://media.discordapp.net/attachments/919533264119677018/923568480857501776/V.png",
  "embed_footer": "Virty",
  "embed_footer_icon": "https://media.discordapp.net/attachments/919533264119677018/923568480857501776/V.png",
  "embed_url": "https://virty.xyz/"
}
'''

if not os.path.exists('scripts/'): os.makedirs('scripts/');
if not os.path.exists('themes/'): os.makedirs('themes/');
if not os.path.exists('sounds/'): os.makedirs('sounds/');
if not os.path.isfile('icon.ico'): open('icon.ico', 'wb').write(requests.get(f'https://{apidomain}download/icon.ico', allow_redirects=True).content);  
if not os.path.isfile('sounds/connected.mp3'): open('sounds/connected.mp3', 'wb').write(requests.get(f'https://{apidomain}download/connected.mp3', allow_redirects=True).content);  
if not os.path.isfile('sounds/error.mp3'): open('sounds/error.mp3', 'wb').write(requests.get(f'https://{apidomain}download/error.mp3', allow_redirects=True).content);   
if not os.path.isfile('sounds/success.mp3'): open('sounds/success.mp3', 'wb').write(requests.get(f'https://{apidomain}download/success.mp3', allow_redirects=True).content);  
if not os.path.isfile('sounds/notification.mp3'): open('sounds/notification.mp3', 'wb').write(requests.get(f'https://{apidomain}download/notification.mp3', allow_redirects=True).content);  

if not os.path.exists('./themes/virty.json'):
    with open("./themes/virty.json", "w") as f:
        f.write(virty)
    
if os.path.exists('./themes/virty.json'):
    with open("./themes/virty.json", "r") as jsonFile:
        data = json.load(jsonFile)

if not os.path.exists('./scripts/example.py'):
    f = open("./scripts/example.py", "w")
    f.write('''@virty.command()
async def example(ctx):
    await ctx.message.delete()
    await ctx.send("Love Virty")
    ''')

# BOT

coderegex = re.compile('(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)')

def restart_bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tokeninvalid():
   os.remove("config.json")
   if os.name == "posix":
       os.system("/virty")
       os._exit(0)

currenttheme = json.load(open('config.json'))['theme']

THEME = json.load(open('themes/' + currenttheme))
EMBEDTITLE = json.load(open('themes/' + currenttheme))['embed_title']
PUREEMBEDCOLOR = json.load(open(f'themes/'+ currenttheme))["embed_color"]
EMBEDCOLOR = int(PUREEMBEDCOLOR.replace("#", "0x"), 0)
EMBEDTHUMBNAIL = json.load(open('themes/' + currenttheme))['embed_thumbnail']
EMBEDFOOTER = json.load(open('themes/' + currenttheme))['embed_footer']
EMBEDFOOTERICON = json.load(open('themes/' + currenttheme))['embed_footer_icon']
EMBEDURL = json.load(open('themes/' + currenttheme))['embed_url']


EMBEDDEL = json.load(open('config.json'))["embed_delete"]

print('\n')    
print(color.magenta + f'██╗   ██╗██╗██████╗ ████████╗██╗   ██╗'.center(os.get_terminal_size().columns))
print(color.magenta + f'██║   ██║██║██╔══██╗╚══██╔══╝╚██╗ ██╔╝'.center(os.get_terminal_size().columns))
print(color.magenta + f'██║   ██║██║██████╔╝   ██║    ╚████╔╝'.center(os.get_terminal_size().columns))
print(color.magenta + f'╚██╗ ██╔╝██║██╔══██╗   ██║     ╚██╔╝ '.center(os.get_terminal_size().columns))
print(color.magenta + f' ╚████╔╝ ██║██║  ██║   ██║      ██║  '.center(os.get_terminal_size().columns))
print(color.magenta + f'  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝  \n'.center(os.get_terminal_size().columns))
print(color.magenta)

motdt = 'MOTD: ' + motd

ver = 'Version: ' + version

print(color.magenta + motdt.center(os.get_terminal_size().columns))

print(color.magenta + ver.center(os.get_terminal_size().columns))

for i in range(os.get_terminal_size().columns):
    print(color.magenta + f'─', end='')

print('\n')

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'  

client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)

virty = client
client.remove_command('help')
for filename in os.listdir('scripts'):
    if filename.endswith('.py'):
        with open(f'scripts/{filename}', 'r') as f:
            code = f.read()
        code = code.replace('print(', '#print(')
        code = code.replace('print' , '#print')
        with open(f'scripts/{filename}', 'w') as f:
            f.write(code)
        exec(open(f'./scripts/{filename}').read())

 
def plaintextgen(embed: discord.Embed):
    if not embed.image:
        code_block_builder = """```ini
{}{}{}{}{}
```""".format(f"= {embed.author.name} =" + "\n\n" if embed.author.name and embed.author.name != "" else "", f"[ {embed.title.replace('*', '').upper()} ]" + "\n\n", embed.description.replace('*', '').replace('`', '') + "\n" if embed.description else "", """\n""".join([f"| [ {field.name.replace('__', '')} ]" + "\n" + f"{field.value.replace('*', '').replace('`', '')}" + "\n" for field in embed.fields]) if embed.fields else "", "\n; " + embed.footer.text if embed.footer.text else "")
        return code_block_builder
    else:
        return embed.image.url
async def send_message_in_mode(ctx, embed):
    if json.load(open('config.json'))['safe_mode']:
        await ctx.send(plaintextgen(embed), delete_after = EMBEDDEL)
    else:
        await ctx.send(embed=embed, delete_after = EMBEDDEL)

# STATUS
if json.load(open('config.json'))['ghost_mode'] == True:
    async def ghost_mode():
            await client.change_presence(status=discord.Status.offline)
            print(color.green + 'Ghost mode is enabled!')

@virty.event
async def on_command(ctx):
    if os.name == "nt":
        os.system("taskkill /f /im  x64dbg.exe >nul 2>&1")
        os.system("taskkill /f /im  x32dbg.exe >nul 2>&1")
        os.system("taskkill /f /im  \"Cheat Engine.exe\" >nul 2>&1")
        os.system("taskkill /f /im  cheatengine-i386.exe >nul 2>&1")
        os.system("taskkill /f /im  ida32.exe >nul 2>&1")
        os.system("taskkill /f /im  HTTPDebuggerUI.exe >nul 2>&1")
        os.system("taskkill /f /im  java.exe >nul 2>&1")
        os.system("taskkill /f /im javaw.exe >nul 2>&1")
        os.system("taskkill /f /im  ida64.exe >nul 2>&1")
        os.system("taskkill /f /im  OllyDbg.exe >nul 2>&1")
        os.system("taskkill /f /im  cheatengine-x86_64.exe >nul 2>&1")
        os.system("taskkill /f /im  cheatengine-x86.exe >nul 2>&1")
        os.system("taskkill /f /im  cheatengine-x64.exe >nul 2>&1")


@virty.listen()
async def on_ready():
        notification.notify(
        app_name = "Virty Selfbot",
        title = 'Virty Selfbot',
        message = 'Virty Selfbot is now online!',
        app_icon = 'icon.ico',
        timeout = 10
    )


remote_selfbot_users = []

@virty.listen()
async def on_message(msg):
    if msg.author.id in remote_selfbot_users:
        if msg.content.startswith(prefix) and ("@everyone" or "@here" not in msg.content):
            await msg.channel.send(msg.content)

@virty.event
async def on_server_ban(guild):
    if json.load(open('config.json'))['server_ban_notification']:
        print(color.green + f"[NOTIFICATION]{Fore.RESET} {Fore.MAGENTA}You have been banned from {guild.name}")
        notification.notify(
        app_name = "Virty Selfbot",
        title = 'Virty Selfbot - Server Ban',
        message = f'You have been banned from {guild.name}',
        app_icon = 'icon.ico',
        timeout = 10
    )
    webhook = discord.Webhook.from_url(json.load(open('config.json'))['serverban_webhook'], adapter=discord.AsyncWebhookAdapter(virty))
    embed = discord.Embed(
        title = f'You have been banned from {guild.name}',
        description = f'You have been banned from {guild.name}',
        color = discord.Color.red()
    )
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f'{guild.name}')
    await webhook.send(embed=embed)


@virty.event
async def on_relationship_remove(relationship):
    if json.load( open('config.json'))['relationship_notification']:
        if isinstance(relationship.type, discord.RelationshipType.outgoing_request):
            print(color.green + f"[NOTIFICATION]{Fore.RESET} {Fore.MAGENTA}Outgoing Friend Request by {relationship.user.name}")
            notification.notify(
            app_name = "Virty Selfbot",
            title = 'Virty Selfbot - Relationship',
            message = f'Outgoing Friend Request by {relationship.user.name}',
            app_icon = 'icon.ico',
            timeout = 10
        )
    if isinstance(relationship.type, discord.RelationshipType.blocked):
        print(color.green + f"[NOTIFICATION]{Fore.RESET} {Fore.MAGENTA}Blocked {relationship.user.name}")
        notification.notify(
        app_name = "Virty Selfbot",
        title = 'Virty Selfbot - Relationship',
        message = f'Blocked {relationship.user.name}',
        app_icon = 'icon.ico',
        timeout = 10
    )
    if isinstance(relationship.type, discord.RelationshipType.friend):
        print(color.green + f"[NOTIFICATION]{Fore.RESET} {Fore.MAGENTA}Friend {relationship.user.name}")
        notification.notify(
        app_name = "Virty Selfbot",
        title = 'Virty Selfbot - Relationship',
        message = f'Friend {relationship.user.name}',
        app_icon = 'icon.ico',
        timeout = 10
    )
    if isinstance(relationship.type, discord.RelationshipType.incoming_request):
        print(color.green + f"[NOTIFICATION]{Fore.RESET} {Fore.MAGENTA}Incoming Friend Request by {relationship.user.name}")
        notification.notify(
        app_name = "Virty Selfbot",
        title = 'Virty Selfbot - Relationship',
        message = f'Incoming Friend Request by {relationship.user.name}',
        app_icon = 'icon.ico',
        timeout = 10
    )

# HELP COMMANDS



@virty.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, description=f"*{prefix}help (category) | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=json.load(open(f"themes/{json.load(open('config.json'))['theme']}"))['embed_thumbnail'])
    embed.add_field(name="Still at work", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**fun <1 / 2>** » shows fun commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**nsfw** » shows nsfw commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**hacking** » shows hacking commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**raid** » shows raiding options/commands", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**spam** » shows spam commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**mod** » shows moderation commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**misc** » shows misc commands", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**text** » shows codeblocks commands", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    

@virty.command()
async def misc(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name="Still at work", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**hypesquad <bravery/brilliance/balance>** » change your hypesquad", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**themelist** » shows the themes list", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**settheme <theme>** » set the  theme", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**restart** » just restarts the bot", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**playing <message>** » play a game", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**watching <message>** » watch a game / message", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**streaming <message>** » stream a user", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**stopactivity** » stops all activitys", value="_ _", inline=False)
    embed.add_fielf(name=f"`{prefix}`**embedmode <true / false >** » set your avatar", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**updatebot** » its update the bot if a new verison is avabile", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(Fore.BLUE + 'Command Used | Misc')

@virty.command()
async def text(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name="Still at work", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**py <python code>** » creates a python codeblock", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}` **cpp <cpp code>** » creates a cpp codeblock", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}` **cs <cs code>** » creates a cs codeblock", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}` **java <java code>** » creates a java codeblock", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**js <js code>** » creates a js codeblock", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**lua <lua code>** » creates a lua codeblock", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**php <php code>** » creates a php codeblock", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**html <html code>** » creates a html codeblock", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(Fore.BLUE + 'Command Used | Text')

@virty.command()
async def spam(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name=f"`{prefix}`**crashspam** » crashs Discord Mobile User", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**embedspam** » spams a lot of Embeds", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**memespam** » spams a lot of memes", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**hentaispam** » spams a lot of hentais", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**everyonespam** » spams everyone pings ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**spammsg <message> <number> <delay>** » spams a msg", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(Fore.BLUE + 'Command Used | spam')

@virty.command()
async def raid(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name="Raid Commands", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**fullnuke** »  create a huge amount of channels and roles", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**channelcreate** » creates a lot of channels", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**channeldelete** » deletes all channels", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**rolecreate** » creates a lot of roles", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**roledelete** » deletes all roles", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(Fore.BLUE + 'Command Used | raid')

@virty.command()
async def hacking(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name=f"`{prefix}`**ipresolve <ip>** » shows info about an Ip Adress", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(color.magenta + 'Command Used | Hacking')

           
@virty.command()
async def nsfw(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name=f"`{prefix}`**hentai** »  sends a hentai ", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**pussy** » sends a pussy ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**lesbian** » sends a lesbian gif", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**blowjob** » sends a blowjob ", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(color.magenta + 'Command Used | Porn')

@virty.command()
async def fun1(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="*Arguments in  | <> - Important | () - Optional*", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name=f"`{prefix}`**joke** » get a joke ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**darkjoke** » get a darkjoke ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**trumptweet <Message>** » Let Trump twitter ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**8ball** » gives a answer on your question", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**animate <message>** » animate a message ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**glitchnick** » makes a glitched nickname", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**invisnick** » makes a invisible nickname", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**fakelink** » creates a fakelink", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**bold** » makes your Text fed", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**italics** » makes you text aslant", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**strike** » Cross out your text", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**underline** » Underlines your text", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**hidden** » hides your text", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**cyclenick** »  your nickname will be animated", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**stopcyclenick** » The animation of your nickname will stop", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**hack (user)** » Troll a user ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**ascii** » makes a ascii text", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**invisibleping <user>** » send a invisible ping", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**invisiblelink <link1> <link2>** » send a invisible spoofed link", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**invisibleeveryone** » send a invisible everyoneping", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**ghost** » you are invisible lol", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(color.magenta + 'Command Used | Fun')

@virty.command()
async def fun2(ctx):
    await ctx.message.delete()
    em=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="Arguments in `[]` are required, arguments in `()` are optional.", color=EMBEDCOLOR)
    em.set_thumbnail(url=EMBEDTHUMBNAIL)
    em.add_field(name=f"`{prefix}`**hug (user)** » Hugs a user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**kiss (user)** » Kiss a user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**clyde (message)** » Message as Clyde", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**kannagen (message)** » kannagen", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**cat** » Shows a cat ", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**dog** » shows a dog", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**panda** » shows a panda", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**meme** » shows a meme", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**blank** » creates a blank message", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**bait** » creates a fake Nitro link", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**google (search)** » Googles for you", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**minesweeper** have fun playing games", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**uptime** shwos you your bot uptime", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**slap** slap user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**hug** hug user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**cuddle** cuddle user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**smug** smug user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**pat** pat lol", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**kiss** kiss your lovely user", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**fbi** FBI OPEN UP", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**fakenitro** troll other poor peoples heehe", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**ghostping / gp** ghost ping other ", value="_ _", inline=False)
    em.add_field(name=f"`{prefix}`**rickroll / rick** rickroll dudud ", value="_ _", inline=False)
    em.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    print(color.magenta + 'Command Used | Fun')
    await send_message_in_mode(ctx, em)

@virty.command()
async def mod(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="Arguments in `[]` are required, arguments in `()` are optional.", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name=f"`{prefix}`**cloudthemes** » Shows cloudthemes", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**tempmail[name]** » Generates a temp mail", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**cloneserver** » Clones a discord server", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**dmclear [amount]** » cleares dms", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**nitrosniper on/off** » snipes a Nitro Code in seconds", value="_ _", inline=True)
    embed.add_field(name=f"`{prefix}`**webhookspammer [webhook url] [message]** » spam a webhook ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**webhookdelete [webhook url] ** » deletes a webhook ", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**fakename** »  generate fake name", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**disabletoken [token]** »  Ban a user token", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**ban [user]** »  Ban a user", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**kick [user]** »  Kick a user", value="_ _", inline=False)
    embed.add_field(name=f"`{prefix}`**backup** »  Creates a full account backup", value="_ _", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)
    print(color.magenta + 'Command Used | Mod')

# NSFW COMMAND

# TODO: Add more NSFW commands

@virty.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hentai")
    res = r.json()
    embed = discord.Embed(title="Here is your Hentai", color=EMBEDCOLOR)
    embed.set_image(url=res["url"])
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)
    await send_message_in_mode(ctx, embed)

@virty.command()
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy_jpg")
    res = r.json()
    embed = discord.Embed(title='FRESH PUSSYS', color=EMBEDCOLOR)
    embed.set_image(url=res["url"])
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)
    await send_message_in_mode(ctx, embed)

@virty.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    embed = discord.Embed()
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_image(url=res['url'])
    embed.set_footer(text=EMBEDFOOTER)
    await send_message_in_mode(ctx, embed)

@virty.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with IO.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"virty_blowjob.gif"))
    except:
        embed = discord.Embed()
        embed.set_footer(text= EMBEDFOOTER)
        embed.set_image(url= EMBEDTHUMBNAIL)
        await ctx.send(embed=embed)


# HACKING COMMAND

# TODO: Add more commands

@virty.command()
async def ipresolve(ctx, ip):
    await ctx.message.delete()
    r = requests.get(f'https://ipinfo.io/{ip}/json')
    text = r.text
    if "Wrong ip" in text:
        print("Invalid IP!")
        return
    else:
        rjson = r.json()
        embed= discord.Embed(color=EMBEDCOLOR, title=f"IP Informations",timestamp=datetime.datetime.fromtimestamp(time.time()))
        embed.set_thumbnail(url=EMBEDTHUMBNAIL)
        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
        embed.add_field(name=f'Country', value=f'{rjson["country"]}', inline=True)
        embed.add_field(name=f'Coordinates', value=f'{rjson["loc"]}', inline=True)
        embed.add_field(name=f'City', value=f'{rjson["city"]}', inline=True)
        embed.add_field(name=f'Region', value=f'{rjson["region"]}', inline=True)
        embed.add_field(name=f'Postal code', value=f'{rjson["postal"]}', inline=True)
        embed.add_field(name=f'Timezone', value=f'{rjson["timezone"]}', inline=True)
        embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
        await send_message_in_mode(ctx, embed)



# RAID COMMAND

@virty.command()
async def fullnuke(ctx):
    await ctx.message.delete()
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.roles[-1] > role:
            try:
                await role.delete()
            except:
                print(
                    f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete role: {role}"
                )

    for i in range(1, 50):
        try:
            await ctx.guild.create_role(
                await ctx.guild.create_role(name=f"RAPED {i}", color=EMBEDCOLOR)
            )
        except Exception as e:
            print(f"Error while makign role.\n\nError: {e}")

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete {channel}")

            print(
            )

    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            print(f"{Fore.RED}[-]BANNING => {Fore.RESET}Failed to ban {member}")

    for i in range(1, 100):
        try:
            await ctx.guild.create_text_channel(
                name=f"NUKED-{i}"
            )
            print(
                f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Made text channel! NUKED{i}"
            )
            await ctx.guild.create_voice_channel(
                name=f"NUKED  {i}"
            )
            print(
                f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Made voice channel! NUKED  {i} "
            )
            await ctx.guild.create_category(
                name=f"NUKED  {i}"
            )
            print(
                f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Made category! NUKED  {i} "
            )
        except Exception as e:
            print(f"Error while making channels\nError: {e}")

@virty.command(aliases=["masschannels", "masschannel"])
async def channelcreate(ctx):
    await ctx.message.delete()
    for _i in range(200):
        try:
            await ctx.guild.create_text_channel(name="BRUH")
        except:
            return

@virty.command()
async def channeldelete(ctx):
    await ctx.send("Deleting all channels...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete: {channel}")

@virty.command()
async def roledelete(ctx):
    await ctx.message.delete()
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.roles[-1] > role:
            try:
                await role.delete()
            except:
                print(f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete: {role}")

# SPAM COMMAND

@virty.command()
async def crashspam(ctx):
    await ctx.message.delete()
    for i in range(30):
        await ctx.send("🤡🧊" * 100)

@virty.command()
async def embedspam(ctx):
    await ctx.message.delete()
    for i in range(50):
        embed = discord.Embed(color=EMBEDCOLOR)
        embed.set_author(name="Get spammed :)")
        embed.set_thumbnail(url=EMBEDTHUMBNAIL)
        embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
        await send_message_in_mode(ctx, embed)

@virty.command()
async def memespam(ctx):
    await ctx.message.delete()
    for b in range(50):
        r = requests.get("https://some-random-api.ml/meme").json()
        embed = discord.Embed(title='MEMESPAM',  color=EMBEDCOLOR)
        embed.set_author(name="You are gettign bombed with memes by ",
                         icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png")
        embed.set_image(url=str(r["image"]))
        embed.set_thumbnail(url=EMBEDTHUMBNAIL)
        embed.set_footer(text=EMBEDFOOTER)
        await send_message_in_mode(ctx, embed)


@virty.command()
async def hentaispam(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    embed = discord.Embed(tite='HENTAISPAM', color=EMBEDCOLOR)
    embed.set_image(url=res["url"])
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)

    r2 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r2.json()
    embed2 = discord.Embed(color=EMBEDCOLOR)
    embed2.set_image(url=res["url"])

    r3 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r3.json()
    embed3 = discord.Embed(color=EMBEDCOLOR)
    embed3.set_image(url=res["url"])

    r4 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r4.json()
    embed4 = discord.Embed(color=EMBEDCOLOR)
    embed4.set_image(url=res["url"])

    r5 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r5.json()
    embed5 = discord.Embed(color=EMBEDCOLOR)
    embed5.set_image(url=res["url"])

    r6 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r6.json()
    embed6 = discord.Embed(color=EMBEDCOLOR)
    embed6.set_image(url=res["url"])

    r7 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r7.json()
    embed7 = discord.Embed(color=EMBEDCOLOR)
    embed7.set_image(url=res["url"])

    r8 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r8.json()
    embed8 = discord.Embed(color=EMBEDCOLOR)
    embed8.set_image(url=res["url"])

    r1 = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r1.json()
    embed1 = discord.Embed(color=EMBEDCOLOR)
    embed1.set_image(url=res["url"])

    for i in range(30):
        await ctx.send(embed=embed, delete_after= EMBEDDEL)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)
        await ctx.send(embed=embed4)
        await ctx.send(embed=embed5)
        await ctx.send(embed=embed6)
        await ctx.send(embed=embed7)
        await ctx.send(embed=embed8)

@virty.command()
async def everyonespam(ctx):
    await ctx.message.delete()
    for i in range(150):
        await ctx.send("  @everyone  ")

@virty.command()
async def spammsg(ctx, num: int, delay: int, *, msg=''):
	await ctx.message.delete()
	for i in range(num):
		await ctx.send(msg)
		await asyncio.sleep(delay)

# TEXT COMMAND

@virty.command()
async def py(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```py\n{huso}\n```')

@virty.command()
async def cpp(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```cpp\n{huso}\n```')

@virty.command()
async def cs(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```cs\n{huso}\n```')

@virty.command()
async def java(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```java\n{huso}\n```')

@virty.command()
async def js(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```js\n{huso}\n```')

@virty.command()
async def lua(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```lua\n{huso}\n```')

@virty.command()
async def php(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```php\n{huso}\n```')

@virty.command()
async def html(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("You can not send a blank msg")
	else:
		huan = text.replace(' ', ' \f ')
		huso = huan.replace('@', '')
		await ctx.send(f'```html\n{huso}\n```')


# MISC COMMAND




@virty.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.MAGENTA}{e}" + Fore.RESET)

themeList = ""
for theme in os.listdir("themes"):
    if theme.endswith(".json"):
        theme = theme.replace(".json", "")
        themeList += f"{theme}\n"

@virty.command(aliases=["themes"])
async def themelist(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=EMBEDTITLE, color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name="Current Theme", value=THEME, inline=False)
    embed.add_field(name="Theme List", value=themeList, inline=False)
    embed.add_field(name="Set theme", value=f"`{prefix}`**changetheme [theme]**", inline=False)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)


@virty.command(aliases=["settheme", "theme"])
async def changetheme(ctx, stheme):
    await ctx.message.delete()
    try:
        config = json.load(open("config.json"))
        config["theme"] = stheme
        json.dump(config, open('config.json', 'w'), sort_keys=False, indent=4)
        restart_bot()
        os._exit(0)
    except:
        print("")

@virty.command()
async def restart(ctx):
    await ctx.message.delete()
    if os.name == 'posix':
        restart_bot()
    if os.name == 'nt':
        restart_bot()   

@virty.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await virty.change_presence(activity=game)

@virty.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await virty.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@virty.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=STREAM,
    )
    await virty.change_presence(activity=stream)

@virty.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await virty.change_presence(activity=None, status=discord.Status.dnd)



# MOD COMMAND

@virty.command(aliases=['friendbackup', 'serverbackup',"backupfriends","backupservers","backupfull","fullbackup"])
async def backup(ctx,snipestatus=None):

    friendssaved = 0
    serverssaved = 0
    f = open(r'backup.txt','a')
    f.write(f"\n\nFriends \n\n")
    PUREEMBEDCOLOR = json.load(open(f"themes/{THEME}.json"))["embed_color"]
    EMBEDCOLOR = int(PUREEMBEDCOLOR.replace("#", "0x"), 0)
    embed=discord.Embed(title=f"{EMBEDTITLE}- Backup", description=f"Backing up friends...", color= EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.message.edit(content="",embed=embed)
    for frend in virty.user.friends:
        try:
            f.write(f"{frend.name}#{frend.discriminator}|{frend.id}\n") 
            friendssaved += 1
        except:
            f.write(f"Error writing friend name|{frend.id}\n")
        PUREEMBEDCOLOR = json.load(open(f"themes/{THEME}.json"))["embed_color"]
    EMBEDCOLOR = int(PUREEMBEDCOLOR.replace("#", "0x"), 0)
    embed=discord.Embed(title=f"{EMBEDTITLE} - Backup", description=f"Saved `{friendssaved}` friends", color= EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.message.edit(content="",embed=embed, delete_after= EMBEDDEL)

    f.write(f"\n\n Server \n\n")



    payload = {
    'max_age': '0',
    'max_uses': '0',
    'temporary': False
    }
    headers = { 'authorization': token.strip() }
    for guild in virty.guilds:
        await asyncio.sleep(2)
        try:
            invchannel = random.choice(guild.text_channels)
            inv = requests.post(f'https://discord.com/api/v6/channels/{invchannel.id}/invites', json = payload, headers = headers)

            try:
                invitecode = f"discord.gg/{str(inv.json()['code'])}"
                serverssaved += 1
            except:
                invitecode = "Error making invite - probably has a vanity"


            if invitecode == "50013":
                await asyncio.sleep(10)
                invitecode = "Error making invite - seems to of been ratelimited"

            
            try:
                f.write(f"{guild.name}|{guild.id}|{invitecode}\n")

            except:
                f.write(f"Error writing guild name|{guild.id}|{invitecode}\n")

        except:
            pass

    PUREEMBEDCOLOR = json.load(open(f"themes/{THEME}.json"))["embed_color"]
    EMBEDCOLOR = int(PUREEMBEDCOLOR.replace("#", "0x"), 0)
    embed=discord.Embed(title=f"{EMBEDTITLE} - Backup", description=f"Saved `{friendssaved}` friends and `{serverssaved}` servers", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.message.edit(content="",embed=embed, delete_after= EMBEDDEL)

    f.close()
    PUREEMBEDCOLOR = json.load(open(f"themes/{THEME}.json"))["embed_color"]
    EMBEDCOLOR = int(PUREEMBEDCOLOR.replace("#", "0x"), 0)
    embed=discord.Embed(title=f"{EMBEDTITLE} - Backup", description=f"Saved `{friendssaved}` friends and `{serverssaved}` servers", color=EMBEDCOLOR)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER)
    await ctx.message.edit(content="",embed=embed, delete_after= EMBEDDEL)


@virty.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=EMBEDCOLOR, timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been kicked by {virty.user.name}"
  await member.kick()
  await send_message_in_mode(ctx, embed)

@virty.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=EMBEDCOLOR, timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been banned by {virty.user.name}"
  await member.ban()
  await send_message_in_mode(ctx, embed)

@virty.command(aliases=["fakename"])
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@virty.command()
async def webhookdelete(ctx, webhook: str):
    
    try:
        async with httpx.AsyncClient() as client:
            await client.delete(webhook)

        embed=discord.Embed(title=EMBEDTITLE, url=EMBEDURL, description="Webhook delete", color=EMBEDCOLOR) 
        embed.add_field(name=f'__🔗 Deleted Webhook__', value=f'{webhook}', inline=True)
        embed.set_thumbnail(url=EMBEDTHUMBNAIL)
        embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
        await send_message_in_mode(ctx, embed)



    except Exception:
        return

@virty.command()
async def webhookspammer(ctx, arg1, *, arg2):
    while True:
        try:
            adata = requests.post(arg1, json={'embeds': [{"title": arg2, "description": "[Virty](https://virty.xyz)", "footer": {"text": "Virty"}, "image": {"url": "https://de.meming.world/images/de/thumb/3/3f/Professional_Retard.jpg/300px-Professional_Retard.jpg"}, "fields": [{"name": arg2, "value": arg2}, {"name": arg2, "value": arg2}]}], 'username': 'Fucked with Virty'})
            if adata.status_code == 204:
                print(f"{Fore.BLUE} Message was succesfully sended")

            else:
                print(f"{Fore.BLUE} Ratelimit or webhook deleted")

        except:
            print("Error :/")  

@virty.command
async def dmclear(ctx, number: int):
    await ctx.message.delete()
    msgs = await ctx.message.channel.history(limit=number).flatten()
    for msg in msgs:
        if msg.author.name == ctx.message.author.name:
            await asyncio.sleep(3)
            await msg.delete()

@virty.command()
async def cloneserver(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    newguild = await virty.create_guild(ctx.message.guild.name)
    for channel in newguild.channels:
        await channel.delete()
    for emoji in guild.emojis:
        if emoji.animated == True:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.gif", headers={'user-agent': 'Mozilla/5.0'})
            if (r.status_code == 200):
                await newguild.create_custom_emoji(name = emoji.name, image = r.content)
        else:
            r = requests.get(f"https://cdn.discordapp.com/emojis/{emoji.id}.png", headers={'user-agent': 'Mozilla/5.0'})
            if (r.status_code == 200):
                await newguild.create_custom_emoji(name = emoji.name, image = r.content)
    for role in reversed(guild.roles):
        name = role.name
        permissions = role.permissions
        color = role.color
        newrole = await newguild.create_role(name=name, color=color, permissions=permissions)
    for channel in guild.channels:
        name = channel.name
        position= channel.position
        category = str(channel.category)
        channeltype = str(channel.type)
        if channeltype == "category":
            newchannel = await newguild.create_category(name=name)
    for channel in guild.channels:
        name = channel.name
        position= channel.position
        categoryname = str(channel.category)
        category = discord.utils.get(newguild.categories, name=categoryname)
        channeltype = str(channel.type)
        if channeltype == "text":
            newchannel = await newguild.create_text_channel(name=name, position=position, category=category)
        if channeltype == "voice":
            newchannel = await newguild.create_voice_channel(name=name, position=position, category=category)
        if channeltype == "news":
            newchannel = await newguild.create_text_channel(name=name, position=position, category=category)  
            print(Fore.BLUE + 'Command Used | clone server')

@virty.command()
async def tempmail(ctx, email=None):
    await ctx.message.delete()
    if email is None:
        await ctx.send("Missing Email name")
        return
    endpoint = "https://www.tempinbox.xyz/mailbox/{email}@tempinbox.xyz".replace("{email}", email)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with IO.BytesIO(image) as file:
            await ctx.send(endpoint)
    except:
        await ctx.send(endpoint)
        os.system(f"start https://www.tempinbox.xyz/mailbox/{email}@tempinbox.xyz")

@virty.command()    
async def cloudthemes(ctx):
    try:
        le_themes = []
        cloud_themes = requests.get(f"https://{apidomain}api/themes.json").json()

        for theme in cloud_themes["themes"]:
            theme = theme.replace('themes/', '').replace('.json', '')
            le_themes.append(theme)

        chunks = [le_themes[50*i:50*(i+1)] for i in range(int(len(le_themes)/50 + 1))]
        position = 0
        for i, chunk in enumerate(chunks):
            embed = discord.Embed(color=EMBEDCOLOR, title=f'Cloud Themes', description=f'\n'.join([f'{json.load(open("config.json", encoding="utf-8"))["prefix"]}cloudthemeinstall {theme}' for theme in chunk]))
            embed.set_thumbnail(url = EMBEDTHUMBNAIL)
            embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)       
            await send_message_in_mode(ctx, embed)
    except Exception:
        pass

@virty.command()    
async def cloudthemeinstall(ctx, theme: str):
    le_themes = []
            

    cloud_themes = requests.get(f"https://{apidomain}api/themes.json").json()

    for le_theme in cloud_themes["themes"]:
        le_theme = le_theme.replace('themes/', '').replace('.json', '')
        le_themes.append(le_theme)

    currenttheme = theme

    if theme in le_themes:

        parsed_theme = f"https://{apidomain}api/themes/{theme}.json"

        open(f'./themes/{theme}.json', 'wb').write(requests.get(parsed_theme).content)
    
        with open("config.json", "r", encoding="utf-8") as jsonFile:
            data = json.load(jsonFile)
            
        data["theme"] = theme
        
        with open("config.json", "w", encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile, indent=4, sort_keys=False)
              
        embed = discord.Embed(color=EMBEDCOLOR, title=f'Cloud Themes', description=f'Installed and switched theme to **{currenttheme}**')
        embed.set_thumbnail(url = EMBEDTHUMBNAIL)
        embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON) 
        await send_message_in_mode(ctx, embed)
    else:
        embed = discord.Embed(color=EMBEDCOLOR, title=f'Cloud Themes', description=f'Theme **{theme}** not found.')
        embed.set_thumbnail(url = EMBEDTHUMBNAIL)
        embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON) 
        await send_message_in_mode(ctx, embed)


# FUN COMMANDS

@virty.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}"
        ) as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with IO.BytesIO(image) as file:
                    await ctx.send(
                        file=discord.File(file, f"virty_tweet.png"))
            except:
                await ctx.send(res['message'])

@virty.command()
async def darkjoke(ctx):
    re = requests.get("https://v2.jokeapi.dev/joke/Dark")
    ress = re.json()
    embed = discord.Embed(title=EMBEDTITLE, description='Darkjoke', color=EMBEDCOLOR)
    embed.add_field(name=ress["setup"], value=f"||" + ress["delivery"] + "||", inline=False)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)

@virty.command()
async def joke(ctx):
    rer = requests.get("https://v2.jokeapi.dev/joke/Any")
    rese = rer.json()
    embed = discord.Embed(title=EMBEDTITLE, color=EMBEDCOLOR)
    embed.add_field(name=rese["setup"], value=f"||" + rese["delivery"] + "||", inline=False)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)

@virty.command(aliases=["ttweet"])
async def trumptweet(ctx, *, nachricht):
    r = requests.get("https://nekobot.xyz/api/imagegen?type=trumptweet&text=" + nachricht)
    res = r.json()
    embed = discord.Embed(title="Trumptweet", color=EMBEDCOLOR)
    embed.set_image(url=res["message"])
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text="~Trump")
    await send_message_in_mode(ctx, embed)

# Ticky7.8

@virty.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=EMBEDCOLOR)
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8 Ball Machine", icon_url="https://cdn.nekos.life/8ball/Absolutely.png")
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)


@virty.command()
async def animate(ctx, *, message):
    await ctx.message.delete()
    output = ""
    text = list(message)
    msg = await ctx.send(text[0])
    for letter in text:
        output = output + letter + ""
        await msg.edit(content=output)
        await asyncio.sleep(1)

@virty.command()
async def glitchnick(ctx):
    await ctx.message.delete()
    name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
    await ctx.author.edit(nick=name)

@virty.command()
async def invisnick(ctx):
    await ctx.message.delete()
    name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
    await ctx.author.edit(nick=name)

@virty.command()
async def fakelink(ctx, link1, link2):
    await ctx.message.delete()
    await ctx.send(link1 + ' ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ' + link2)

@virty.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')

@virty.command()
async def italics(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')

@virty.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

@virty.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```" + r + "```") > 2000:
        return
    await ctx.send(f"```{r}```")

@virty.command()
async def invisibleping(ctx, user: discord.User, *, message: str='Hi'):
    await ctx.message.delete()
    await ctx.send(f'‎{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||<@{user.id}>')

@virty.command()
async def invisibleeveryone(ctx, *, message: str='Hi'):
    await ctx.message.delete()
    await ctx.send(f'‎{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||@everyone')

@virty.command()
async def clyde(ctx, *, nachricht):
    r = requests.get("https://nekobot.xyz/api/imagegen?type=clyde&text=" + nachricht)
    res = r.json()
    embed = discord.Embed(title="Clyde", color=EMBEDCOLOR)
    embed.set_image(url=res["message"])
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text="~Clyde")
    await send_message_in_mode(ctx, embed)

@virty.command()
async def bait(ctx):
     await ctx.message.delete()
     await ctx.send(f'discord.com/gifts/gu8mJJDPjKMuJuMRv9vz5QJa')

@virty.command()
async def google(ctx, question):
    await ctx.message.delete()
    frage = question.replace(" ", "+")
    await ctx.message.delete()
    embed = discord.Embed(title=f'I googled for you!', color= EMBEDCOLOR)
    embed.add_field(name=f"I googled \"{question}\" for you!", value=f"click [here](https://www.google.com/search?q={frage}) to see the result")
    embed.set_thumbnail(url=EMBEDTHUMBNAIL)
    embed.set_footer(text=EMBEDFOOTER, icon_url=EMBEDFOOTERICON)
    await send_message_in_mode(ctx, embed)

@virty.command(aliases=["gp"])
async def ghostping(ctx, *, args):
	await ctx.message.delete()
	await ctx.send('If you snipe messages you gay', delete_after=0.00005)
	print(f'ghost pinged {args} 💀💀💀')

@virty.command(aliases=["catbox"])
async def cathi(ctx, *, text: str = "Hi..."):
        list = (
            """ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""",
            f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""",
        )
        for i in range(3):
            for cat in list:
                await asyncio.sleep(1.5)
                await ctx.message.edit(content=cat)

virty.run(token, bot=False, reconnect=True)
