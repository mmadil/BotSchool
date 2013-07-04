# Main IRC server settings

SERVER = '127.0.0.1'
PORT = 6667

# Other settings

DEBUG = True

# Register every bot here.

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

MODULES = (
    'irc',
)
