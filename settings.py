# Main IRC server settings

SERVER = '127.0.0.1'
PORT = 6667

# Other settings

DEBUG = True

# Register every bot here.

BOTS = {
        'helperbot': [        # How would you recognize this bot ?
            'Helper',         # Bot Type
            'HelperBot',      # Nick
            'helperbot',      # Ident
            'password',       # Password
            '#help',          # Channel alloted to this bot
            'IRC Helper Bot', # Real name of this bot
            'hostname',       # Hostname
            ],
        'teacherbot': [
            'Teacher',
            'TeacherBot',
            'teacherbot',
            'password',
            '#Tutorials',
            'IRC Teacher Bot',
            'hostname',
            ],
        }


# Enable every modules here 

MODULES = (
    'irc',
)
