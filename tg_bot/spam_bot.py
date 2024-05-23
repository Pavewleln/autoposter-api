from aiogram import Bot, Dispatcher, types
import asyncio
import sqlite3

API_TOKEN = '7159553101:AAHOpPtyFy7y-rDVHLSmc4e1G0LpYsRPa8Q'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, loop=asyncio.new_event_loop())

@dp.message_handler(commands=["send"])
async def send_message_to_all_users(message: types.Message):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT user_id FROM users")
    user_ids = c.fetchall()
    conn.close()
    text = message.text.replace("/send", "")

    for user_id in user_ids:
        await bot.send_message(chat_id=user_id[0], text=text)

if __name__ == '__main__':
    asyncio.run(dp.start_polling())
