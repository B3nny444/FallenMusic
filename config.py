from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv(27094161))
API_HASH = getenv("39477b23f5e6abea95fe0f92b7f00de0")

BOT_TOKEN = getenv("BOT_TOKEN", "7008178074:AAHRxTvWF_HBlQ-FXzg5gnYhXzHpmLWEj5A")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv(1513565142))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
