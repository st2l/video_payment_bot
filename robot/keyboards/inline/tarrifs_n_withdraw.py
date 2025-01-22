from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def tarrifs_n_withdraw():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text='📊 Тарифы', callback_data='tariffs'),
        InlineKeyboardButton(text='💰 Вывод', callback_data='withdraw'),
    )
    return kb