# Main IRC server settings

# Specify the server bots will connect to
SERVER = '127.0.0.1'

# Specify that servers port
PORT = 6667


# If you are developing, you can use it in DEBUG mode.
DEBUG = True



# Register every bot here.

# To register a bot you can use the following data structure
# You can add more than one bot.

# BOTS = {
#         'botname':[
#             'Bot Type',                           # Teacher or Speaker
#             'Nick name of the bot',
#             'Ident of the bot',
#             'Password if any',
#             'Channel that a bot will join',
#             'Realname of the bot',
#             'hostname',
#             ],
#         and so on....
#         }


BOTS = {
        'teacherbot': [
            'Teacher',
            'TeacherBot',
            'teacherbot',
            'password',
            '#tutorials',
            'IRC Teacher Bot',
            'hostname',
            ],
        'speakerbot': [
            'Speaker',
            'Steve',
            'Steve',
            '',
            '',
            'Teacher Bot',
            '',
            ],
        }


# Enable every modules here 

# When you find that a module is complete
# You can add them here.

# Make sure that the name of a module is same
# as the its directory name

MODULES = (
    'irc',
)
