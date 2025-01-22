from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text='💵 Заработоĸ', callback_data='earnmoney'),
        InlineKeyboardButton(text='📊 Тарифы', callback_data='tariffs'),
        InlineKeyboardButton(text='💰 Вывод', callback_data='withdraw'),
        InlineKeyboardButton(text='👨‍💻 Профиль', callback_data='stats'),
        InlineKeyboardButton(text="Ответы на вопросы", callback_data='faq'),
    )
    return kb
