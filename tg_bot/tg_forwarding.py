from telethon import TelegramClient, events

INPUT_CHANNEL = 'https://t.me/+UvW3pfFNzZ8yNmJi' # куда
OUTPUT_CHANNEL = 'https://t.me/kanal33467784' # откуда

# 1. Заходим на сайт https://my.telegram.org/apps
# 2. Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.

api_id = 26700140
api_hash = 'a685eedb87b25a1c1543f25d087c6bc4'

client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):
    await client.send_message(OUTPUT_CHANNEL, event.message)


client.start()
client.run_until_disconnected()
