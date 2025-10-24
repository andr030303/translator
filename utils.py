from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start = Router()


@start.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(f"Привет, {message.from_user.full_name}! Это бот-переводчик.")

