#old modules from smircbot re-written in Python2
# coding=utf8
from sopel.module import commands, rule, priority, example
import random
#<3
@rule('.*<3.*')
@priority('high')
def lilheart(bot, trigger):
    if trigger.nick == "Ameenekosan":
        bot.say("<3")
    else:
        bot.say("#nohomo")

#beke
@commands("beke")
@example("&beke")
def kwame_beke(bot, trigger):
    bot.write(("NICK",), "KwameBeke")
    bot.say("hé hé hé...")
    bot.write(("NICK",), bot.nick)

#lucario
@commands("lucario")
@example("&lucario")
def kwame_beke(bot, trigger):
    bot.say("The bot cannot do Lucario. Lucario is way too sexy (#not)")

#trollolol
@rule('.*:\^\).*')
@priority('high')
def trololo(bot,trigger):
    bot.say("THE TROLL STRUCK AGAIN")
    if random.randint(0, 1) == 0:
        if random.randint(0, 4) == 0:
            bot.say("False story")
        else:
            bot.say("True story")
    if random.randint(0, 1) == 0:
        bot.say("TROLOLO")
