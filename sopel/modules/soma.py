#old modules from smircbot re-written in Python2
# coding=utf8
from sopel.module import commands, rule, priority, example
import requests

@commands("somafm")
def somafm(bot,trigger):
    r = requests.get('http://somafm.com/channels.xml')
    if r.status_code == 200:
        bot.say("")
