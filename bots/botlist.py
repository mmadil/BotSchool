# This will list every bot that has been listed 
# in settings

from settings import bots

def getlist():
    names = ''

    if len(bots) == 1:
        return 'We have 1 bot. \n '+bots.pop()

    else:
        for e in bots:
            names += str(e) + ', '
        return 'We have '+str(len(bots))+' bots. \n '+names
