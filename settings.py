# Main IRC server settings
SERVER = '127.0.0.1'
PORT = 6667

# Other settings
DEBUG = True

# Register every bot here.

bots = {
        'helperbot': [
            'HelperBot',      # Nick
            'helperbot',      # Ident
            'password',       # Password
            '#help',          # Channel alloted to this bot
            'IRC Helper Bot', # Real name of this bot
            'hostname',       # Hostname
            ],
        }

