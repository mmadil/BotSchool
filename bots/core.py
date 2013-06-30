#!/usr/bin/python -tt

import settings

import socket
import re


class BotBehavior():
    def __init__(self, bot):
        self.server = settings.SERVER
        self.port = settings.PORT

        self.bot = bot

        if self.bot == 'helperbot':
            self.nick = self.bot
            self.ident = self.bot
            self.channel = '#help'
            self.realname = 'IRC Helper Bot'
        else:
            self.nick = self.bot
            self.ident = self.bot
            self.channel = ''
            self.realname = 'Unknown bot'

    def __str__(self):
        return """Connecting %s to %s:%s. \n\nWith these Details : \n\n Nick: %s \n Ident: %s
 Realname : %s \n Channel : %s \n""" % (self.bot, self.server, self.port,
                                    self.nick, self.ident, self.realname, self.channel)


    def connect(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.server, self.port))
        print 'Connected to IRC ..'
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER ' + self.nick + self.nick + self.ident +' :'+ self.realname +'\r\n')

        while True:
            data = self.irc.recv(1024)
            print data



