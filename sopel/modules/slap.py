#coding=utf-8
#plugins thats worked on Uguubot

from sopel.module import commands, rule, priority, example
import random
from random import randint
import json
from sopel.util import textgen, text

def get_generator(_json, variables):
    data = json.loads(_json)
    return textgen.TextGenerator(data["templates"], data["parts"], variables=variables)

@commands("slap")
def slap(bot, trigger):
    """slap <user> -- Makes the bot slap <user>."""
    target = trigger.group(2)

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot slap itself, slap them
    if trigger.group(2) == bot.nick or trigger.group(2) == "itself":
        target = trigger.nick

    variables = {
        "user": target
    }

    with open("/home/ameenekosan/code/Yumiko/sopel/modules/data/slaps.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    bot.action(generator.generate_string())
    return
