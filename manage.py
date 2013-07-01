#!/usr/bin/python -tt

from settings import bots
from bots.core import Bot

import sys

# Helper Functions and Global Variables

def getlist():
    string = ''

    if len(bots) == 1:
        return 'We have 1 bot. \n 1. ' + bots.keys()[0]
    else:
        count = 1
        for e in bots.keys():
            string += str(count)+'. '
            string += str(e) + '\n '
            count += 1
        return 'We have '+str(len(bots))+' bots. \n '+string


class Initializer():
    # This class loads the bot and initiates it.
    def __init__(self, arg):
        self.arg = arg[1:]

    def __str__(self):
        return 'Arguments that have been passed were : ' + str(self.arg)

    def arguments(self):

        if 'run' in self.arg:
            print getlist()
            bot = raw_input("Choose any botname : ")

            if bot in bots:
                return self.runbot(bot)
            else:
                return "Please choose an appropriate bot !"

        if 'list' in self.arg:
            return getlist()

        elif self.arg not in ['run','list']:
            return """
            Usage : python manage.py [ run | list ]

            """

    def runbot(self, bot):
        print '\nLoading bot', bot
        start = Bot(bot)
        print start
        start.main()
        return ''



if __name__ == '__main__':
    init = Initializer(list(sys.argv))
    print init
    print init.arguments()


