from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def payment_method():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(text='💳 Картой', callback_data='payment_method'),
        InlineKeyboardButton(text='💰 Электронные деньги',
                             callback_data='payment_method'),
        InlineKeyboardButton(text='👛 Криптовалюта',
                             callback_data='payment_method'),
        InlineKeyboardButton(text='📞 Телефон', callback_data='payment_method'),
        InlineKeyboardButton(text='🔙 Назад', callback_data='cancel'),
    )
    return kb
