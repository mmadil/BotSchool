#!/usr/bin/python -tt

from bots import botlist
from settings import bots
from bots.core import BotBehavior

import sys

class Initializer():
    # This class loads the bot and initiates it.
    def __init__(self, arg):
        self.arg = arg[1:]

    def __str__(self):
        return 'Arguments that have been passed were : ' + str(self.arg)

    def arguments(self):

        if 'run' in self.arg:
            print botlist.getlist()
            bot = raw_input("Choose any botname : ")

            if bot in bots:
                return self.runbot(bot)
            else:
                return "Please choose an appropriate bot !"

        if 'list' in self.arg:
            return botlist.getlist()

        elif self.arg not in ['run','list','more']:
            return """
            Usage : python manage.py [ run | list | more ]

            """

    def runbot(self, bot):
        print '\nLoading bot', bot
        start = BotBehavior(bot)
        print start
        start.main()
        return ''



if __name__ == '__main__':
    init = Initializer(list(sys.argv))
    print init
    print init.arguments()


