from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def add_method():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text='💳 Добавить метод', callback_data='add_method'),
    )
    return kb