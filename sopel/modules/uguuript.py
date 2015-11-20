#coding=utf-8
#plugins thats worked on Uguubot

from sopel.module import commands, rule, priority, example
import random
from random import randint
import json
color_codes = {
    "<r>": "\x02\x0305",
    "<g>": "\x02\x0303",
    "<y>": "\x02"
}
#hack
@commands("hack")
@example("&hack nickname")
def hacking(bot, trigger):
    if trigger.group(2):
        nickname = trigger.group(2)
        bot.action("is hacking %s" % nickname)
    else :
        bot.say("Hacking everyone...")

#8ball
with open("/home/ameenekosan/code/Yumiko/sopel/modules/data/8ball_responses.txt") as f:
    responses = [line.strip() for line in f.readlines() if not line.startswith("//")]
@commands("8ball")
def heightball(bot,trigger):
    if trigger.group(2):
        bot.action("shakes the magic ball")
        bot.say(random.choice(responses))
