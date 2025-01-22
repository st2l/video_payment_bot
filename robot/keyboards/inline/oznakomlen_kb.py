from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def oznakomlen_kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text="✅ Ознаĸомлен", callback_data='oznakomlen'),
    )
    return kb
