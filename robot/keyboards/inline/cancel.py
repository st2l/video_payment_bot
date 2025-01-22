from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def cancel():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔙 Назад",
                    callback_data="cancel"
                )
            ]
        ]
    )
    return keyboard