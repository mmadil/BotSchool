#!/usr/bin/python -tt

# Imports 

import settings

import socket
import re
import time

# Helper Functions and global variables.

running = True

def get_bot_details(bot):
    if bot in settings.bots.keys():
        bot_config = settings.bots.values()[settings.bots.keys().index(bot)]
        return bot_config

def get_modulest(bot):
    pass

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



class BotBehavior():
    def __init__(self, bot):
        self.server = settings.SERVER
        self.port = settings.PORT

        self.bot = bot

        # Will add this part to another class later.
        if self.bot:
            self.nick, self.ident, self.password, self.channel, self.realname, self.hostname = get_bot_details(self.bot)
        else:
            print "Sorry, Which bot ?"
            exit(1)

    def __str__(self):
        return """Connecting %s to %s:%s. \n\nWith these Details : \n\n Nick: %s \n Ident: %s
 Realname : %s \n Channel : %s \n""" % (self.bot, self.server, self.port,
                                    self.nick, self.ident, self.realname, self.channel)

    def main(self):
        self.run()

    def bot_ai(self, data):
        pass

    def regexify_data(self, data):
        regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'
        matchObj = re.match(regex, data, re.M|re.I)
        if matchObj:
            return matchObj.group(), matchObj(1), matchObj(2), matchObj(3), matchObj(4), matchObj(5), matchObj(6)

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

                    if data.find('Message of the Day'):
                        self.irc.send('JOIN '+ self.channel + '\r\n')

                    if data.find('+iwR') != -1:
                        self.irc.send('PRIVMSG NickServ IDENTIFY '+ self.nick + ' ' + self.password + '\r\n')

                    if data.find('!tutor') != -1:
                        self.regexify(data)
                        self.irc.send('PRIVMSG ' + self.to + ' Its working !')


                except Exception:
                   pass
