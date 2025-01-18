import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

# Bot information
API_ID = environ.get('API_ID', '21956488')
API_HASH = environ.get('API_HASH', '812529f879f06436925c7d62eb49f5d1')
BOT_TOKEN = environ.get('BOT_TOKEN', "7091587168:AAGpX2rHu-DVYmXUdlxM3vZRnaLBrx8k3-c")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
WORKERS = int(getenv('WORKERS', '4'))
name = str(getenv('name', 'linkstreamrobot'))
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002114619001") 
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002114619001") 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5977931010').split()]

PICS = (environ.get('PICS', 'https://envs.sh/AwV.jpg'))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://aman727587:aman@cluster0.bk39x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")

AUTH_PICS = environ.get('AUTH_PICS', 'https://envs.sh/AwV.jpg')              
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002114619001"))
FSUB = environ.get("FSUB", True)
