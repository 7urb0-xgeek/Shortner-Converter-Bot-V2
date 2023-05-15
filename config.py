# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "21166181"))
API_HASH = os.environ.get("API_HASH", "8c3a80939d1a3ca93acfee34ae66e267")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6156012315:AAFCDVC5crr8bhM8nYhYrRM8WLlrqh1ImL8")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5226253251")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Turbox")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://turbo07:GTqWzJVuLiSbST40@cluster0.bmz24ks.mongodb.net/?retryWrites=true&w=majority
                         ") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5226253251")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001903351383/4")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Turboshortner") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
