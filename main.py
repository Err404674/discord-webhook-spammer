import os
import sys
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import init
init()
from colorama import Fore
from tqdm import tqdm
import time
from time import sleep
# https://www.luya.ml/ [Website]
# https://ko-fi.com/luyadevs [Donate]
# https://t.me/bladetools [Telegram]

os.system("title Luya Webhook Spammer [https://github.com/LuyaTools]")
y = Fore.YELLOW
w = Fore.WHITE

def clear():
    os.system("cls")

title = f"""
                                        {y}██{w}╗     {y}██{w}╗   {y}██{w}╗{y}██{w}╗   {y}██{w}╗ {y}█████{w}╗ 
                                        {y}██{w}║     {y}██{w}║   {y}██{w}║╚{y}██{w}╗ {y}██{w}╔╝{y}██{w}╔══{y}██{w}╗
                                        {y}██{w}║     {y}██{w}║   {y}██{w}║ ╚{y}████{w}╔╝ {y}███████{w}║
                                        {y}██{w}║     {y}██{w}║   {y}██{w}║  ╚{y}██{w}╔╝  {y}██{w}╔══{y}██{w}║
                                        {y}███████{w}╗╚{y}██████{w}╔╝   {y}██{w}║   {y}██{w}║  {y}██{w}║
                                        {w}╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝"""


clear()
print(title)
print("""
                                             Webhook Spammer - v1.0
                                          https://github.com/LuyaTools
                                             https://t.me/bladetools
""")

webh = input(w + "[" + y + "+" + w + "] Webhook: ")
amt = input(w + "[" + y + "+" + w + "] Amount: ")
msg = input(w + "[" + y + "+" + w + "] Message: ")
input(f"{w}Press {y}ENTER{w} to start spamming: ")
clear()
print(title)
for i in tqdm(range(int(amt)), desc ="Spamming"):
    webhook = DiscordWebhook(url=webh, content=msg)
    response = webhook.execute()
time.sleep(2)
print("finished")
os.system("py main.py")
sys.exit()
input()