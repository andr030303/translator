from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from keyboards import main_menu, language_menu

router = Router()

# --- /start ---
@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! 🌍\n"
        "Я — бот-переводчик. Отправь мне текст, и я переведу его!\n\n"
        "Используй кнопки ниже 👇",
        reply_markup=main_menu()
    )

# --- /help ---
@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(
        "🆘 <b>Справка по командам:</b>\n\n"
        "/start — начать работу с ботом\n"
        "/help — показать это сообщение\n"
        "/settings — изменить язык перевода\n\n"
        "Также можно просто отправить текст — я переведу его автоматически 🌍",
        reply_markup=main_menu()
    )

# --- /settings ---
@router.message(Command("settings"))
async def settings_handler(message: types.Message):
    await message.answer(
        "⚙️ Выбери язык, на который нужно переводить сообщения:",
        reply_markup=language_menu()
    )
