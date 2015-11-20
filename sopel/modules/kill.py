#coding=utf-8
#plugins thats worked on Uguubot

from sopel.module import commands, rule, priority, example
import random
from random import randint
import json

@commands("kill")
def kill(bot, trigger):
    """kill <user> -- Makes the bot kill <user>."""
    target = trigger.group(2)

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot kill itself, kill them
    if trigger.group(2) == bot.nickname or trigger.group(2) == "itself":
        target = trigger.bot

    variables = {
        "user": target
    }

    with open("modules/data/kills.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    bot.action(generator.generate_string())
    return
