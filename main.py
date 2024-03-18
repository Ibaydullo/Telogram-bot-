from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello
from core.handlers.contact import get_true_contact
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command, CommandStart
from aiogram import F
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot ishlayabdi')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot ishlamaypdi')





async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')



    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_hello, F.text == 'salom')
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_true_contact, F.contact)
    # dp.message.register(get_start, CommandStart)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__ == "__main__":
    asyncio.run(start())