from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def prosmotreno_kb(dt: str):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text="✅ Просмотрено", callback_data=dt),
    )
    return kb