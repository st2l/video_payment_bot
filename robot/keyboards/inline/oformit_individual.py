from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def oformit_individual():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text='✅ Оформить INDIVIDUAL за 0.15$', url='https://google.com'),
        InlineKeyboardButton(text='🔙 Назад', callback_data='cancel'),
    )
    return kb