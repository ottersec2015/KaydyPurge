# ============================================================================= #
#                                                                               # Special thanks
#                            discord.gg/comunidad                               # to Zen & wRRulos
#                                                                               # for help in that
#                            KaydyPurge Script V1                               # miniproject.
#                        Best Purge Selfbot for Discord                         #
#                               Made by Kaydy                                   #
#                              Kaydy Cain#0001                                  #
#                                                                               #
# ============================================================================= #

# Any error report it to my discord please Kaydy Cain#0001
# Programmed in Python 3.10.1

import os
import discord
import requests
import discord_webhook
import colorama
import aiohttp
import asyncio
import datetime
import ctypes
import time
import signal
import sys

from re import purge
from discord.ext import commands
from colorama import Fore, init
from os import system
from json import load

# kaydyCFG.json - Made by Kaydy Cain#0001

with open('kaydyCFG.json') as f:
    d = load(f)
    token = d["token"]
    prefix = d["prefix"]

# MORE CLEAN CMD - Made by Kaydy Cain#0001

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# COLORES - Made by rulo

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

colorama.init()

token = (token)

ping = False

kaydyPurgeTitle = 'KaydyPurge'

bot = commands.Bot(command_prefix=(prefix), self_bot=True)

loadingKaydy = rf""" 

{reset}      .,;
      ';,.'      ';.,'
              ;,.;'

{reset}          ;.,:   '.,;,                        {lred}Any bug report me in Discord (Kaydy Cain#0001)
{reset}       ',.  .',;;.',;
    {red} ____________  {lblue}                        ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
    {red} \oooooooooo/ {lblue}                         ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
    {red}  \________/ {lblue}                          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗
    {red}   \______/ {lblue}                           ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
    {yellow}     |oo| {lblue}                             ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
    {yellow}     |oo|    _____ {lblue}                    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    {yellow}     |==|   / ___()                                    {lred}discord.gg/comunidad
    {yellow}     |==|  / /
    {yellow}     |oo| / /
    {yellow}     |oo|/ /
    {yellow}     |==/ /                                
    {red}     |='./                                    
    {red}     |oo|                                      
    {red}     |==|                                       
    {red}     |__|                                       
    {red}   ,'____',
    {red} /"________"\
    {red}/____________\{reset}

    """

loadingKaydy2 = rf""" 

{reset}      .,;
      ';,.'      ';.,'
              ;,.;'

{reset}          ;.,:   '.,;,                        {lred}Any bug report me in Discord (Kaydy Cain#0001)
{reset}       ',.  .',;;.',;
    {red} ____________  {lblue}                        ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
    {red} \oooooooooo/ {lblue}                         ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
    {red}  \________/ {lblue}                          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗
    {red}   \______/ {lblue}                           ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
    {yellow}     |oo| {lblue}                             ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
    {yellow}     |oo|    _____ {lblue}                    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    {yellow}     |==|   / ___()                                    {lred}discord.gg/comunidad
    {yellow}     |==|  / /
    {yellow}     |oo| / /
    {yellow}     |oo|/ /
    {yellow}     |==/ /                                   {cyan}[{blue}STATUS{cyan}]{white}: {lblue}kaydyCFG.json Imported Succesfully
    {red}     |='./                                    
    {red}     |oo|                                      
    {red}     |==|                                       
    {red}     |__|                                       
    {red}   ,'____',
    {red} /"________"\
    {red}/____________\{reset}

    """

loadingKaydy3 = rf""" 

{reset}      .,;
      ';,.'      ';.,'
              ;,.;'

{reset}          ;.,:   '.,;,                        {lred}Any bug report me in Discord (Kaydy Cain#0001)
{reset}       ',.  .',;;.',;
    {red} ____________  {lblue}                        ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
    {red} \oooooooooo/ {lblue}                         ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
    {red}  \________/ {lblue}                          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗
    {red}   \______/ {lblue}                           ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
    {yellow}     |oo| {lblue}                             ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
    {yellow}     |oo|    _____ {lblue}                    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    {yellow}     |==|   / ___()                                    {lred}discord.gg/comunidad
    {yellow}     |==|  / /
    {yellow}     |oo| / /
    {yellow}     |oo|/ /
    {yellow}     |==/ /                                   {cyan}[{blue}STATUS{cyan}]{white}: {lblue}kaydyCFG.json Imported Succesfully
    {red}     |='./                                    {cyan}[{blue}STATUS{cyan}]{white}: {lblue}Connected to KaydyPurge API Server
    {red}     |oo|                                      
    {red}     |==|                                       
    {red}     |__|                                       
    {red}   ,'____',
    {red} /"________"\
    {red}/____________\{reset}

    """

loadingKaydy4 = rf""" 

{reset}      .,;
      ';,.'      ';.,'
              ;,.;'

{reset}          ;.,:   '.,;,                        {lred}Any bug report me in Discord (Kaydy Cain#0001)
{reset}       ',.  .',;;.',;
    {red} ____________  {lblue}                        ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
    {red} \oooooooooo/ {lblue}                         ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
    {red}  \________/ {lblue}                          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗
    {red}   \______/ {lblue}                           ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
    {yellow}     |oo| {lblue}                             ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
    {yellow}     |oo|    _____ {lblue}                    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    {yellow}     |==|   / ___()                                    {lred}discord.gg/comunidad
    {yellow}     |==|  / /
    {yellow}     |oo| / /
    {yellow}     |oo|/ /
    {yellow}     |==/ /                                   {cyan}[{blue}STATUS{cyan}]{white}: {lblue}kaydyCFG.json Imported Succesfully
    {red}     |='./                                    {cyan}[{blue}STATUS{cyan}]{white}: {lblue}Connected to KaydyPurge API Server
    {red}     |oo|                                     {cyan}[{blue}STATUS{cyan}]{white}: {lblue}Connected to Discord API
    {red}     |==|                                       
    {red}     |__|                                       
    {red}   ,'____',
    {red} /"________"\
    {red}/____________\{reset}

    """

invalidToken = rf""" 

{reset}      .,;
      ';,.'      ';.,'
              ;,.;'

{reset}          ;.,:   '.,;,                        {lred}Any bug report me in Discord (Kaydy Cain#0001)
{reset}       ',.  .',;;.',;
    {red} ____________  {lred}                              ███████╗██████╗ ██████╗  ██████╗ ██████╗ 
    {red} \oooooooooo/ {lred}                                ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
    {red}  \________/ {lred}                                █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝  
    {red}   \______/ {lred}                                  ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
    {yellow}     |oo| {lred}                                   ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
    {yellow}     |oo|    _____ {lred}                          ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝  
    {yellow}     |==|   / ___()                                    {lred}discord.gg/comunidad
    {yellow}     |==|  / /
    {yellow}     |oo| / /
    {yellow}     |oo|/ /
    {yellow}     |==/ /                                   {red}[{lred}ERROR{red}]{white}:     {lred}TOKEN NOT WORKING OR INVALID
    {red}     |='./                                    {red}[{lred}HOW2FIX{red}]{white}:   {lred}Change the token in kaydyCFG.json
    {red}     |oo|                                      
    {red}     |==|                                       
    {red}     |__|                                       
    {red}   ,'____',
    {red} /"________"\
    {red}/____________\{reset}

    """

def limpiarTerminal():
    os.system('cls')


system("title " + kaydyPurgeTitle)

limpiarTerminal()

print(lgreen + "[KaydyPurgeLoader]", lred + "Loading kaydyCFG.json 57%")
print(loadingKaydy)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Loading kaydyCFG.json 99%")
print(loadingKaydy)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "kaydyCFG.json loaded")
print(loadingKaydy2)
time.sleep(2)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonecting to KaydyPurge Server.")
print(loadingKaydy2)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonecting to KaydyPurge Server..")
print(loadingKaydy2)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonecting to KaydyPurge Server...")
print(loadingKaydy2)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonected to KaydyPurge Server")
print(loadingKaydy3)
time.sleep(2)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonecting to Discord API.")
print(loadingKaydy3)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonecting to Discord API..")
print(loadingKaydy3)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonecting to Discord API...")
print(loadingKaydy3)
time.sleep(1)
limpiarTerminal()
print(lgreen + "[KaydyPurgeLoader]", lred + "Coonected to Discord API")
print(loadingKaydy4)
time.sleep(2)
limpiarTerminal()

@bot.event
async def on_ready():
    panelAscii = rf""" 

      .,;
      ';,.'      ';.,'
              ;,.;'

{reset}          ;.,:   '.,;,                          {lred}Any bug report me in Discord (Kaydy Cain#0001)
{reset}       ',.  .',;;.',;
    {red} ____________  {lgreen}         ██╗  ██╗ █████╗ ██╗   ██╗██████╗ ██╗   ██╗    ██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗
    {red} \oooooooooo/ {lgreen}          ██║ ██╔╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝    ██╔══██╗██║   ██║██╔══██╗██╔════╝ ██╔════╝
    {red}  \________/ {lgreen}           █████╔╝ ███████║ ╚████╔╝ ██║  ██║ ╚████╔╝     ██████╔╝██║   ██║██████╔╝██║  ███╗█████╗  
    {red}   \______/ {lgreen}            ██╔═██╗ ██╔══██║  ╚██╔╝  ██║  ██║  ╚██╔╝      ██╔═══╝ ██║   ██║██╔══██╗██║   ██║██╔══╝  
    {yellow}     |oo| {lgreen}              ██║  ██╗██║  ██║   ██║   ██████╔╝   ██║       ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
    {yellow}     |oo|    _____ {lgreen}     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝    ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
    {yellow}     |==|   / ___()                                      {lred}discord.gg/comunidad
    {yellow}     |==|  / /
    {yellow}     |oo| / /
    {yellow}     |oo|/ /
    {yellow}     |==/ /                                     {cyan}[{lred}INFO{cyan}]{white}:   {green}You can change the settings in kaydyCFG.json
    {red}     |='./
    {red}     |oo|                                       {cyan}[{blue}STATUS{cyan}]{white}: {green}Selfbot Started Succesfully
    {red}     |==|                                       {cyan}[{blue}STATUS{cyan}]{white}: {green}Logged in as {lgreen}{bot.user}
    {red}     |__|                                       {cyan}[{blue}STATUS{cyan}]{white}: {green}Command: {prefix}clear
    {red}   ,'____',
    {red} /"________"\
    {red}/____________\{reset}

    """
    print(panelAscii)

client = discord.Client()


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def clear(message):
    async for msg in message.channel.history(limit=100):
        if msg.author == bot.user:
            try:
                await msg.delete()
            except:
                pass


while True:
    try:
        bot.run(token, bot=False)
    except Exception as e:
        clear()
        input(e)
        quit()
