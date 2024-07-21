import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
SESSION = "BQGIzloATDrvWzXv7RRD6Ej6fCpW_B3JJhNYB9WFpzkM7U-g1YkBxxLE5F5ygIWKhtI7t1fuWoY65IHmpmIalZ8eWRTJiTCaEjtnxfhDWVbpEVGY-kgMTIb0j-GMNiSyKchdmIK_2Omlo1aUUTNqMZ3ir5-IfYgEA1jVdC1e10dP9TrX-Mxw_WU8qHPM4Yu10WC9MOPXBB-8wg5I1RPXN13NiF0i9KzkvEMM-66113IWF4zqDcVZxEIpt-WOGo-AxVjovHbjd9FJV1-WWpi5Ph4QIECUookVG6ZSGyln8z1JEh18zDvWD_FJhhrDU-9vqwJe0Io2s20-k1bjAYDYHww2IEk27QAAAAF5XDOMAA"
HNDLR = "/"
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AsadAlexaVCBot"))
call_py = PyTgCalls(bot)
