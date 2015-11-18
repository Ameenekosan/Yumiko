
from __future__ import unicode_literals

from sopel.module import commands
import datetime


def setup(bot):
    if "uptime" not in bot.memory:
        bot.memory["uptime"] = datetime.datetime.utcnow()


@commands('uptime')
def uptime(bot, trigger):
    """.uptime - Returns the uptime of Sopel."""
    delta = datetime.timedelta(seconds=round((datetime.datetime.utcnow() -
                                              bot.memory["uptime"])
                                             .total_seconds()))
    bot.say("I've been listening to your shit for {} and it doesn't seem to stop!"
        .format(delta))
