from aiogram import Router, types
from deep_translator import GoogleTranslator
from keyboards import main_menu, language_menu

# относительный импорт функции добавления в историю
from .extras import add_to_history

router = Router()

# словарь выбранных языков пользователей
user_lang = {}

@router.message(lambda msg: msg.text in ["🇬🇧 Английский", "🇪🇸 Испанский", "🇩🇪 Немецкий", "🇫🇷 Французский"])
async def set_language(message: types.Message):
    langs = {
        "🇬🇧 Английский": "en",
        "🇪🇸 Испанский": "es",
        "🇩🇪 Немецкий": "de",
        "🇫🇷 Французский": "fr"
    }
    user_lang[message.from_user.id] = langs[message.text]
    await message.answer(f"✅ Язык перевода установлен: {message.text}", reply_markup=main_menu())

@router.message(lambda msg: msg.text == "⚙️ Выбрать язык перевода")
async def choose_language(message: types.Message):
    await message.answer("Выбери язык перевода:", reply_markup=language_menu())

@router.message(lambda msg: msg.text == "⬅️ Назад в меню")
async def back_to_menu(message: types.Message):
    await message.answer("Главное меню:", reply_markup=main_menu())

# Основной обработчик перевода — проверяем, что это текст
@router.message(lambda msg: msg.text is not None and not msg.text.startswith('/') and msg.text not in ["🌍 Перевести текст", "🧠 Последние переводы"])
async def translate_text(message: types.Message):
    # убедимся что это текст
    if not message.text:
        return

    lang = user_lang.get(message.from_user.id, 'en')
    text = message.text.strip()

    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
        # добавляем в историю: "оригинал -> перевод"
        add_to_history(message.from_user.id, f"{text} -> {translated}")
        await message.answer(f"🌐 Перевод ({lang}):\n<b>{translated}</b>")
    except Exception:
        await message.answer("⚠️ Ошибка при переводе. Попробуй снова.")
