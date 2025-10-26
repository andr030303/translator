from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌍 Перевести текст")],
            [KeyboardButton(text="⚙️ Выбрать язык перевода")],
            [KeyboardButton(text="🧠 Последние переводы")]
        ],
        resize_keyboard=True
    )

def language_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇬🇧 Английский"),
                KeyboardButton(text="🇪🇸 Испанский")
            ],
            [
                KeyboardButton(text="🇩🇪 Немецкий"),
                KeyboardButton(text="🇫🇷 Французский")
            ],
            [KeyboardButton(text="⬅️ Назад в меню")]
        ],
        resize_keyboard=True
    )
