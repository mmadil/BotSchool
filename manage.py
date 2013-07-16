#!/usr/bin/python -tt

from settings import BOTS
from bot.core import Bot

import sys

# Helper Functions and Global Variables

def getlist():
    ''' This function gets the list of every bot
    present in settings.py
    '''
    string = ''

    if len(BOTS) == 1:
        return 'We have 1 bot. \n 1. ' + BOTS.keys()[0]
    else:
        count = 1
        for e in BOTS.keys():
            string += str(count)+'. '
            string += str(e) + '\n'
            string += ' Type : ' + str( BOTS.values()[BOTS.keys().index(e)][0]) + '\n'
            string += ' Nick : ' + str( BOTS.values()[BOTS.keys().index(e)][1]) + ' \n\n '
            count += 1
        return 'We have '+str(len(BOTS))+' bots. \n\n '+string


class Initializer():
    ''' This class is responsible for managing the
    bot and running the program.
    '''
    def __init__(self, arg):
        self.arg = arg[1:]

    def __str__(self):
        return 'Arguments that have been passed were : ' + str(self.arg)

    def arguments(self):

        if 'run' in self.arg:
            print getlist()
            bot = raw_input("Choose any botname : ")

            if bot in BOTS:
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

