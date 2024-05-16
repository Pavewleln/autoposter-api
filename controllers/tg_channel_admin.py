import asyncio
import contextlib
import asyncio
from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging

API_TOKEN = '7159553101:AAHOpPtyFy7y-rDVHLSmc4e1G0LpYsRPa8Q'
admin_id = 1042652647
channel_id = -1002134206250

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    user_id = chat_join.from_user.id
    msg = "Привет, ваш запрос на вступление одобрен!"
    await bot.send_message(chat_id=user_id, text=msg)
    await chat_join.approve()

async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    bot: Bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == channel_id)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f'{ex}', exc_info=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())


