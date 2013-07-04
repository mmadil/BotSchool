#!/usr/bin/python -tt

from settings import BOTS, MODULES

import os
import re
from espeak import espeak

# Global variables

regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'
some_channel = ''

# Helper functions

def regexify(data):
    matchObj = re.match(regex, data, re.M|re.I)
    if matchObj:
        return matchObj.group(), matchObj.group(1), matchObj.group(2),\
                matchObj.group(3), matchObj.group(4), matchObj.group(5),\
                matchObj.group(6)
    else:
        return ''



def get_nick(string):
    return string[0:string.index('!')]



def list_modules():
    string = ' '

    if len(MODULES) == 1:
        return 'We have 1 module : ' + str(MODULES[0])
    else:
        count = 1
        for e in MODULES:
            string += str(e) + ', '
        return 'We have '+str(len(MODULES))+' modules : '+ str(string[:-2])



def capture_information(string):
    return string[string.index('!') + 6:][:-1]


def capture_chapter(string):
    return string[string.index('!') + 9:][:-1]



def get_chapters(module):
    path = '.'
    chapters = []
    for situated_at, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith((".txt")):
                matchObj = re.match('./(\S+)/(\S+)', situated_at, re.M|re.I)
                if module in MODULES:
                    if module == matchObj.group(2):
                        chapters.append(file_name)
                    else:
                        pass
                else:
                    pass

    return chapters



def menu():
    pass

# AI Functions

def ai(data, bot, irc):
    bot_type, nick, ident, password, channel, realname, hostname = bot

    if bot_type == 'Teacher':

        if data.find('PING') != -1:
            irc.send('PONG ' + data.split() [1] + '\r\n')

        if data.find('Message of the Day') != -1:
            irc.send('JOIN ' + str(channel) + '\r\n')

        if data.find('+iwR') != -1:
            irc.send('PRIVMSG NickServ IDENTIFY ' + str(nick) + ' ' + str(password) + '\r\n')

        if data.find('KICK') != -1:
            irc.send('JOIN ' + str(channel) + '\r\n')

        if bot_type == 'Teacher':
            regexed_list = []


            if data.find('PRIVMSG '+ str(nick) + ' :!tutor') != -1:
                regexed_list = regexify(data)
                msgto = get_nick(regexed_list[2])
                string = list_modules()
                irc.send('PRIVMSG ' + str(msgto) + ' :Hi ' + msgto +' ! \r\n')
                irc.send('PRIVMSG ' + str(msgto) + ' :What would you like to learn ?\r\n')
                irc.send('PRIVMSG ' + str(msgto) + ' :You can learn : \r\n')
                irc.send('PRIVMSG ' + str(msgto) + ' :'+ string + '\r\n')
                irc.send('PRIVMSG ' + str(msgto) + ' :List the chapters using !list <modulename>\r\n')


            if data.find('PRIVMSG '+ str(nick) + ' :!list') != -1:
                regexed_list = regexify(data)
                msgto = get_nick(regexed_list[2])
                module = capture_information(regexed_list[6])
                chapters = get_chapters(str(module))
                if len(chapters) != 0:
                    irc.send('PRIVMSG ' + str(msgto) + ' :'+ str(module) +' has the following chapters : \r\n')
                    for e in chapters:
                        irc.send('PRIVMSG ' + str(msgto) + ' :'+ str(e[:-4]) +'\r\n')
                    irc.send('PRIVMSG ' + str(msgto) + ' :==== End ==== \r\n')
                    irc.send('PRIVMSG ' + str(msgto) + ' :Type !teacheme <chapter> to start learning ;) \r\n')
                else:
                    irc.send('PRIVMSG ' + str(msgto) + ' :Sorry you have searched for a wrong module, start again. \r\n')


            if data.find('PRIVMSG '+ str(nick) + ' :!teachme') != -1:
                regexed_list = regexify(data)
                msgto = get_nick(regexed_list[2])
                chapter = capture_chapter(regexed_list[6])
                chapters = get_chapters()
                if chapter in chapters:
                    irc.send('PRIVMSG ' + str(msgto) + ' :Ok, Lets start with ' + str(chapter) + '\r\n')
                else:
                    irc.send('PRIVMSG ' + str(msgto) + ' :Sorry you are searching for a wrong chapter, start again. \r\n')             

    
    # Code for speaker bot starts here. 
    else:
        print 'Commands - !tutor, !list, !teachme'
        espeak.synth('Hi ! I am %s .' % (str(nick)))
        command = raw_input('>')
        running = True

        while running:
            if command == '!tutor':
                string = list_modules()
                espeak.synth('What would you like to learn ?')
                espeak.synth('%s' % string)
                command = raw_input('List the chapters using !list <modulename>')
                espeak.synth('You selected %s' % command)
                

            elif command == '!list ' + str(capture_information(command)):
                print command
            elif command == '!teachme':
                print 'Okay'
            else:
                print 'Get lost!'




