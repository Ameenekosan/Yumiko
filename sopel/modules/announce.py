
from __future__ import unicode_literals

from sopel.module import commands, example


@commands('announce')
@example('.announce Some important message here')
def announce(bot, trigger):
    """
    Send an announcement to all channels the bot is in
    """
    if not trigger.admin:
        bot.reply('Sorry, I can\'t let you do that')
        return
    for channel in bot.channels:
        bot.msg(channel, '[ANNOUNCEMENT] %s' % trigger.group(2))
