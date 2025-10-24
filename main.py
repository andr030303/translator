import logging
import asyncio
import os
from utils import start
from aiogram import Bot, Dispatcher

TOKEN = os.getenv("BOT_TOKEN")


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(start)

    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

