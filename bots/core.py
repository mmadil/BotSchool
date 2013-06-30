#!/usr/bin/python -tt

# needs network, port, nick, ident, channel, realname

import settings

import socket
import re

class BotBehavior():
    def __init__(self, bot):
        self.server = settings.SERVER
        self.port = settings.PORT
        self.nick = settings.NICK
        self.ident = settings.IDENT
        self.channel = settings.CHANNEL
        self.realname = settings.REALNAME

        self.bot = bot

    def __str__(self):
        return "Connecting %s to %s:%s." % (self.bot, self.server, self.port) 

    def connect(self):
        pass
