Bot School
====================

## What is Bot School ?

Bot School is one of my projects which uses [IRC][1] and [ESpeak][2] in
order to teach users anything. These may include programming languages,
any academic related stuff or possibly anything.

If you are guessing who runs this school? This school is run
by bots. Yes, Bots!

## Bots

Bots play a very important role in this school.
 
In my version bots will teach you how to code from various programming
languages. 
(Provided I along with other collaborators publish the handbook in
time.)

Other version that I can think of is where teachers / lecturers compile
some notes in a handbook and this bot will teach you verbally.

Bots here are of two types :

1. Teacher bot
2. Speaker

These bots can be used in the following ways :

**Teacher bot - IRC Mode**

In IRC mode bots are made to connect to an IRC server and join a
channel. With a few commands, users can talk to the bot and the bots
will reply with further instructions. At the end the bot will start
teaching with a specified chapter by the user.

**Speaker bot - Local Mode**

In local mode bots do not join any IRC server, instead they run as a
simple python program. Here too users can talk to the bot using few
simple commands and the bot replies with further instructions. At the
end the bot will start teaching the specified chapter verbally.


## There is something about this code

**Speaker bot works perfectly well in Linux, Not tested on Windows OS
yet.**

## Dependencies 

1. [Python 2.7+](http://python.org/)
2. [ESpeak](http://espeak.sourceforge.net/)


[1]: https://en.wikipedia.org/wiki/Irc
[2]: https://en.wikipedia.org/wiki/ESpeak

## Settings 

**Please read settings.py for more information**

## Technologies used while developing

+ Raspberry Pi (as server)
+ IRCd (using UnrealIRCd)
+ Anope Services

## Future of Bot School 

+ Adding GUI to it.
+ Publish it as a more enhanced software.

## Call for help 

This project needs help of those people who would like to help me
building a more comprehensive handbook. 
If you would like to add anything to the handbook please collaborate.
Do so by forking this repository and when you are done just
make a pull request. 
