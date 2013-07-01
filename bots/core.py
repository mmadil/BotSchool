#!/usr/bin/python -tt

# Imports 

import settings

import socket
import re
import time

# Helper Functions and global variables.

running = True

regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'

def get_bot_details(bot):
    if bot in settings.bots.keys():
        bot_config = settings.bots.values()[settings.bots.keys().index(bot)]
        return bot_config

def get_modules(bot):
    pass

def regexify(data):
    matchObj = re.match(regex, data, re.M|re.I)
    if matchObj:
        return matchObj.group(), matchObj.group(1), matchObj.group(2), matchObj.group(3), matchObj.group(4), matchObj.group(5), matchObj.group(6)
    else:
        return ''

def get_nick(string):
    return string[0:string.index('!')]


# Classes

class BotType():
    def __init__(self):
        pass

    def __str__(self):
        pass



class BotModules():
    def __init__(self):
        pass

    def __str__(self):
        pass



class Bot():
    def __init__(self, bot):
        self.server = settings.SERVER
        self.port = settings.PORT

        self.bot = bot

        # Will add this part to another class later.
        if self.bot:
            self.type, self.nick, self.ident, self.password, self.channel, self.realname, self.hostname = get_bot_details(self.bot)
        else:
            print "Sorry, Which bot ?"
            exit(1)

    def __str__(self):
        return """Connecting %s to %s:%s. \n\nWith these Details : \n\n Nick: %s \n Ident: %s
 Realname : %s \n Channel : %s \n""" % (self.bot, self.server, self.port,
                                    self.nick, self.ident, self.realname, self.channel)

    def main(self):
        self.run()


    def bot_ai(self, data, timestamp):

        regexed_list = []

        if data.find('PRIVMSG '+ self.nick + ' :!tutor') != -1:
            regexed_list = regexify(data)
            self.msgto = get_nick(regexed_list[2])
            self.irc.send('PRIVMSG ' + self.msgto + ' :Its working !\r\n')


    def run(self):
        while running:
            self.ping_time = int(time.time())
            self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.irc.settimeout(240)
            self.irc.connect((self.server, self.port))

            self.irc.send('USER ' + self.nick + ' host ' + self.hostname + ' :'+ self.realname +'\r\n')
            self.irc.send('NICK ' + self.nick + '\r\n')
            self.connected = True

            while self.connected:
                try:
                    timestamp = int(time.time())
                    data = self.irc.recv(2048)

                    if settings.DEBUG:
                        print data


                    if data.find('PING') != -1:
                        self.irc.send('PONG ' + data.split() [1] + '\r\n')

                    if data.find('Message of the Day') != -1:
                        self.irc.send('JOIN '+ self.channel + '\r\n')

                    if data.find('+iwR') != -1:
                        self.irc.send('PRIVMSG NickServ IDENTIFY '+ self.nick + ' ' + self.password + '\r\n')
                        
                    self.bot_ai(data, timestamp)

                except Exception:
                   pass
