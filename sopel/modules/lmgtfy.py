
from __future__ import unicode_literals
from sopel.module import commands


@commands('lmgtfy', 'lmgify', 'gify', 'gtfy')
def googleit(bot, trigger):
    """Let me just... google that for you."""
    #No input
    if not trigger.group(2):
        return bot.say('http://google.com/')
    bot.say('http://lmgtfy.com/?q=' + trigger.group(2).replace(' ', '+'))
    bot.say('Was that so hard?')
