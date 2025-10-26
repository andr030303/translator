from aiogram import Router, types
from keyboards import main_menu

router = Router()

# В памяти (demo). Формат: history[user_id] = [ "оригинал -> перевод", ... ]
history = {}

@router.message(lambda msg: msg.text == "🧠 Последние переводы")
async def show_history(message: types.Message):
    user_id = message.from_user.id
    user_history = history.get(user_id, [])
    if not user_history:
        await message.answer("🕳 История пуста. Переведи что-нибудь!")
    else:
        # покажем последние 5 переводов в читаемом виде
        last = user_history[-5:]
        text = "\n\n".join([f"🔹 {h}" for h in last])
        await message.answer(f"🧠 Твои последние переводы:\n\n{text}")

def add_to_history(user_id: int, record: str):
    """
    Добавляем запись в историю пользователя.
    record: строка вида "оригинал -> перевод"
    """
    if user_id not in history:
        history[user_id] = []
    history[user_id].append(record)
