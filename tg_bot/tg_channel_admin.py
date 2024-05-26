import asyncio
import contextlib
import logging
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import ChatJoinRequest

API_TOKEN = '7159553101:AAHOpPtyFy7y-rDVHLSmc4e1G0LpYsRPa8Q'
admin_ids = [1042652647, 1776053932]
destination_channel_id = -1002134206250

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.chat_join_request.filter(F.chat.id == destination_channel_id)

@dp.chat_join_request()
async def process_join_request(request: ChatJoinRequest):
    await request.approve()
    await request.bot.send_message(request.from_user.id, "Мы приняли Вашу заявку!")

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?)", [request.from_user.id])
    conn.commit()
    conn.close()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("send"))
async def send_message_to_all_users(message: types.Message):
    if message.from_user.id in admin_ids:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT user_id FROM users")
        user_ids = c.fetchall()
        conn.close()
        text = message.text.replace("/send", "").strip()

        for user_id in user_ids:
            await bot.send_message(chat_id=user_id[0], text=text)
        await message.answer("Успешно.")
    else:
        await message.answer("У вас нет прав для выполнения этой команды.")

@dp.message(Command("parse"))
async def parse_channel(message: types.Message):
    if message.from_user.id in admin_ids:
        try:
            message_url = message.text.split()[1]
            logging.info(f"Received message URL: {message_url}")

            # Извлечение username канала и ID сообщения из ссылки
            parts = message_url.split('/')
            channel_username = parts[-2]
            message_id = int(parts[-1])

            logging.info(f"Channel username: {channel_username}, Message ID: {message_id}")

            # Пересылка сообщения в целевой канал
            await bot.forward_message(destination_channel_id, f"@{channel_username}", message_id)
            await message.answer("Сообщение было успешно переслано.")
        except Exception as e:
            logging.error(f"Error while parsing channel: {e}")
            await message.answer(f"Произошла ошибка: {e}")
    else:
        await message.answer("У вас нет прав для выполнения этой команды.")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
