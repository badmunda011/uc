import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py

import pyrogram

# Create a Pyrogram client with a file-based session storage
client = pyrogram.Client(
    "my_session",
    api_id=25742938,
    api_hash="b35b715fe8dc0a58e8048988286fc5b6",
    storage=pyrogram.session.PersistentSession("path/to/session/file")
)

# Start the client
client.start()

print("UserBot Started")
call_py.start()
print("Vc Client Started")
pyidle()
idle()
