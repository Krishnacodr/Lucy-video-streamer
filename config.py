import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Caden_OP")
ALIVE_NAME = getenv("ALIVE_NAME", "Lucy")
BOT_USERNAME = getenv("BOT_USERNAME", "LUCY_20_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "lucyxplayer")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Caden_world")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Krishnagamerytk")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/cff60c353d1e83d06f7af.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/cff60c353d1e83d06f7af.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/cff60c353d1e83d06f7af.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/cff60c353d1e83d06f7af.jpg")
