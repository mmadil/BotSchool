#!/usr/bin/python -tt

from settings import BOTS, MODULES

import os
import re
import sys
import time
import subprocess
import thread

# Global variables

regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'
some_channel = ''

# Helper functions

def regexify(data):
    ''' This function is used to extract the information
    from the data recieved when connected to an IRC server.
    '''
    matchObj = re.match(regex, data, re.M|re.I)
    if matchObj:
        return matchObj.group(), matchObj.group(1), matchObj.group(2),\
                matchObj.group(3), matchObj.group(4), matchObj.group(5),\
                matchObj.group(6)
    else:
        return ''



def get_nick(string):
    ''' This function is used to extract nick name
    '''
    return string[0:string.index('!')]



def list_modules():
    ''' This function is used to list every module
    that has been listed in settings.py
    '''
    string = ' '

    if len(MODULES) == 1:
        return 'We have 1 module : ' + str(MODULES[0])
    else:
        count = 1
        for e in MODULES:
            string += str(e) + ', '
        return 'We have '+str(len(MODULES))+' modules : '+ str(string[:-2])



def capture_information(string):
    ''' This function is used to extract the command
    that has been provided to a bot.
    '''
    return string[string.index('!') + 6:][:-1]


def capture_chapter(string):
    ''' This function is use to extract the chapters
    name that has been provided by the user.
    '''
    return string[string.index('!') + 9:][:-1]



def get_chapters(module):
    ''' This function is returns every chapter that
    is present in a module.
    '''
    path = '.'
    chapters = []
    for situated_at, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith((".txt")):
                matchObj = re.match('./(\S+)/(\S+)', situated_at, re.M|re.I)
                if module in MODULES:
                    if module == matchObj.group(2):
                        chapters.append(file_name[:-4])
                    else:
                        pass
                else:
                    pass

    return chapters



def get_all_chapters():
    ''' This function returns every chapter
    '''
    path = '.'
    chapters = []

    for situated_at, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith((".txt")):
                chapters.append(file_name[:-4])

    return chapters



def read_chapter(irc, chapter, msgto):
    ''' This function reads the chapter from
    the provided handbook and sends a private
    message to its caller with the contents of
    that chapter.

    Used by Teacher type bots.
    '''
    path = '.'
    chapter += '.txt'

    for situated_at, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith(('.txt')):
                if file_name == chapter:
                    for lines in file(situated_at + '/' + chapter):
                        if lines != '\n':
                            irc.send('PRIVMSG ' + str(msgto) + ' :' + str(lines) + '\r\n')
                        else:
                            pass
                    irc.send('PRIVMSG ' + str(msgto) + ' :==== End ===== \r\n')



def speak_chapter(chapter):
    ''' This function uses ESpeak to read the
    chapters with text to speech translation.

    Used by Speaker type bots.
    '''
    path = '.'
    chapter += '.txt'

    for situated_at, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith(('.txt')):
                if file_name == chapter:
                    if sys.platform == 'linux' or sys.platform == 'linux2':
                        subprocess.call('espeak -p 75 -f ' + situated_at + '/' + chapter + '', shell=True)
                    else:
                        subprocess.call('espeak -p 78 -f ' + situated_at + '/' + chapter + '', shell=True)



# AI Functions

def ai(data, bot, irc):
    '''
    This function is responsible for a bots AI 
    capabilities. It works differntly for 
    Speaker type bots and Teacher type bots.

    '''

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
                        irc.send('PRIVMSG ' + str(msgto) + ' :'+ str(e) +'\r\n')
                    irc.send('PRIVMSG ' + str(msgto) + ' :==== End ==== \r\n')
                    irc.send('PRIVMSG ' + str(msgto) + ' :Type !teacheme <chapter> to start learning ;) \r\n')
                else:
                    irc.send('PRIVMSG ' + str(msgto) + ' :Sorry you have searched for a wrong module, start again. \r\n')


            if data.find('PRIVMSG '+ str(nick) + ' :!teachme') != -1:
                regexed_list = regexify(data)
                msgto = get_nick(regexed_list[2])
                chapter = capture_chapter(regexed_list[6])
                chapters = get_all_chapters() # this is a big issue now ! Will work on it later.
                children = []

                if chapter in chapters:
                    irc.send('PRIVMSG ' + str(msgto) + ' :Ok, Lets start with ' + str(chapter) + '\r\n')
                    print "Starting New Thread"
                    thread.start_new_thread(read_chapter, (irc, chapter, msgto))

                else:
                    irc.send('PRIVMSG ' + str(msgto) + ' :Sorry you are searching for a wrong chapter, start again. \r\n')


    # Code for speaker bot starts here. 
    else:
        running = True
        print 'What would you like to learn ? '
        modules = list_modules()
        print modules
        module = raw_input('>')

        if module in MODULES:
            print "In this module we have the following chapters :\n"
            for e in get_chapters(module):
                print " " + e
            chapter = raw_input('Enter the chapters name : ')
            if chapter:
                while running:
                    speak_chapter(chapter)
                    running = False

            else:
                print "Please provide a chapters name"

        else:
            print "Invalid choice!"
            sys.exit(1)


