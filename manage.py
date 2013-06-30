from bots import botlist

import sys

class Initializer():
    # This class loads the bot and initiates it.
    def __init__(self, arg):
        self.arg = arg[1:]
    
    def __str__(self):
        return 'Arguments that have been passed were : ' + str(self.arg)

    def listbots(self):
        pass

    def arguments(self):
        if self.arg == []:
            return """
            Usage : python manage.py --[ load | list | more ] bot1 bot2 bot3
            """

        if '--load' in self.arg:
            return 'loading..'

        if '--list' in self.arg:
            return botlist.getlistofbots()

    def loadbot(self):
        pass

init = Initializer(list(sys.argv))
print init
print init.arguments()
