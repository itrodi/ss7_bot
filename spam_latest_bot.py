

!pip install --upgrade pip
!pip install --upgrade telethon

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = 20350775
api_hash = "394f0f01f375e1ebc1ba67d6cb0b932e"

session = StringSession('1BJWap1wBu7BpN-scMC6pfzy-N0wcIhkCzCMBoBJXEhMRHZk-7pizCCwJtlrVgVyQr2I7FFW2RIRwX8HDK4YDKdHTXL6beHxgob1zdVb3DwUrXhoQvUJulQt6dIV5joG7w00si4Hb7aqMaJkMdg7NdjzqQbVhURaaUAuMk-4z2DoYqjawQNZHTtNCcY6n5-VSmCtrI8UuxN1kdhW-3s6V2HiqC_hEtMQiIUOpNwilGZxnX3MT6dfTWfGq9N4f4JbhGnY6XWjWOH7kApEdmB-jnNl5iO224qNJf7g1Q1xy61xkXssQ1WWy4uS_EBjl9hkHSTWPdgu5upN75f9Mk7mgnESGXuvGXm0=')
client = TelegramClient(session, api_id, api_hash)
await client.start()

chat_ids = [-1002066355314, -1001960863412]
message = "why always me"

async def send_message_to_multiple_chats():
    for chat_id in chat_ids:
        await client.send_message(chat_id, message)

await send_message_to_multiple_chats()

