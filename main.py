from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
import asyncio

from config import TOKEN
from handlers import start, translate, extras

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

async def set_commands():
    commands = [
        BotCommand(command="start", description="Начать работу"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="settings", description="Настройки перевода"),
    ]
    await bot.set_my_commands(commands)

async def main():
    dp.include_router(start.router)
    dp.include_router(translate.router)
    dp.include_router(extras.router)
    await set_commands()
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

