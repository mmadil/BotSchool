#!/usr/bin/python -tt

# Imports 

import settings
from bot.behavior import ai

import socket
import time

# Global variables.

running = True

# Helper functions

def get_bot_details(bot):
    if bot in settings.bots.keys():
        bot_config = settings.bots.values()[settings.bots.keys().index(bot)]
        return bot_config

# Main Bot Class

class Bot():
    def __init__(self, bot):
        self.server = settings.SERVER
        self.port = settings.PORT

        self.bot = bot

        if self.bot:
            self.bot_type, self.nick, self.ident, self.password, self.channel, self.realname,\
                    self.hostname = self.bot_details = get_bot_details(self.bot)
        else:
            print "Sorry, Which bot ?"
            exit(1)


    def __str__(self):
        return """Connecting %s to %s:%s. \n\nWith these Details : \n\n Nick: %s \n Ident: %s
 Realname : %s \n Channel : %s \n""" % (self.bot, self.server, self.port,
                                    self.nick, self.ident, self.realname, self.channel)

    def main(self):
        self.run()


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

                    ai(data, self.bot_details, self.irc)

                except Exception, err:
                   import traceback, os.path
                   traceback.print_exc(err)
                   self.connected = False
                   print err
                   pass
