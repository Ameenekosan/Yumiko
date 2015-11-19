#old modules from smircbot re-written in Python2
# coding=utf8
from sopel.module import commands, rule, priority, example

@commands("pleurniche")
def pleurniche(bot, trigger):
    bot.say("arretez de dire que %s !!!!!!! =(=(=(=(=(=(=(=(=(=(=(=(=(=(=(=(=(=(=(=(=(" % trigger.group(2))
