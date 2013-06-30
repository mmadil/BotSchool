#!/usr/bin/python -tt

# needs network, port, nick, ident, channel, realname

import settings

import socket
import re

class BotBehavior():
    def __init__(self):
        self.port = settings.PORT

    def __str__(self):
        return self.port

    def connect(self):
        pass
