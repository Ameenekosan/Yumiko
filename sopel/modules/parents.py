from sopel.module import commands


@commands('parents')
def parents(bot, trigger):
    Mom = "Ameenekosan"
    Dad = "alxgnon"

    if trigger.nick == Mom:
        bot.reply("You're my mommy and %s is my daddy! <3" % Dad)
    elif trigger.nick == Dad:
        bot.reply("%s is my mommy and you're my daddy! <3" % Mom)
    else:
        bot.reply("%s is my mommy and %s is my daddy! <3" % (Mom, Dad))
