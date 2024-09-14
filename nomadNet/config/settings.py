import os

LTE_MODEMS = [
    {'id': 'modem1', 'device': '/dev/ttyUSB0'},
    {'id': 'modem2', 'device': '/dev/ttyUSB1'},
    {'id': 'modem3', 'device': '/dev/ttyUSB2'},
    {'id': 'modem4', 'device': '/dev/ttyUSB3'},
]

WIFI_INTERFACE = 'wlan0'
MAX_CONNECTIONS_PER_MODEM = 50
IP_REFRESH_INTERVAL = 3600  # 1 hour
AUTH_TOKEN = os.environ.get('NOMADNET_AUTH_TOKEN', 'default_secret_token')
LOG_FILE = '/var/log/nomadnet.log'

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', 'your-auth0-domain.auth0.com')
AUTH0_API_AUDIENCE = os.environ.get('AUTH0_API_AUDIENCE', 'https://api.nomadnet.example.com')
AUTH0_ALGORITHMS = ['RS256']