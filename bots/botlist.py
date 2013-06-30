# This will list every bot that has been listed 
# in settings

from settings import bots

def getlist():
    string = ''

    if len(bots) == 1:
        return 'We have 1 bot. \n 1. '+bots.pop()

    else:
        count = 1
        for e in bots:
            string += str(count)+'. '
            string += str(e) + '\n '
            count += 1
        return 'We have '+str(len(bots))+' bots. \n '+string
