#coding=utf-8
#plugins thats worked on Uguubot

from sopel.module import commands, rule, priority, example

#hack
@commands("hack")
@example("&hack nickname")
def hacking(bot, trigger):
    if trigger.group(2):
        nickname = trigger.group(2)
        bot.action("is hacking %s" % nickname)
    else :
        bot.say("Hacking everyone...")
