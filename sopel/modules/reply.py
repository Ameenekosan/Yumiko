#old modules from smircbot re-written in Python2
# coding=utf8
from sopel.module import commands, rule, priority, example

@rule("$nickname[,:]?")
def reply(bot,trigger):
    bot.say(trigger.nick + "?")
