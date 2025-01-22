from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def choose_tariff():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text='📊 Выбрать тариф', callback_data='tariffs'),
        InlineKeyboardButton(text='🔙 Назад', callback_data='cancel'),
    )
    return kb