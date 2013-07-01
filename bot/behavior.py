#!/usr/bin/python -tt

import re
import settings

# Global variables

regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'


# Helper functions

def regexify(data):
    matchObj = re.match(regex, data, re.M|re.I)
    if matchObj:
        return matchObj.group(), matchObj.group(1), matchObj.group(2), matchObj.group(3), matchObj.group(4), matchObj.group(5), matchObj.group(6)
    else:
        return ''


def get_nick(string):
    return string[0:string.index('!')]



# AI Functions

def ai(data, bot, irc):
    bot_type, nick, ident, password, channel, realname, hostname = bot

    if data.find('PING') != -1:
        irc.send('PONG ' + data.split() [1] + '\r\n')

    if data.find('Message of the Day') != -1:
        irc.send('JOIN ' + channel + '\r\n')

    if data.find('+iwR') != -1:
        irc.send('PRIVMSG NickServ IDENTIFY ' + str(nick) + ' ' + str(password) + '\r\n')

    if bot_type == 'Helper':
        regexed_list = []

        if data.find('PRIVMSG '+ nick + ' :!tutor') != -1:
            regexed_list = regexify(data)
            msgto = get_nick(regexed_list[2])
            irc.send('PRIVMSG ' + msgto + ' :Its working !\r\n')


    if bot_type == 'Teacher':
        pass
