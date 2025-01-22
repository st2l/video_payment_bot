import logging
from random import randint

from asgiref.sync import sync_to_async
from robot.models import TelegramUser, Video
import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from robot.keyboards.inline import payment_method
from robot.utils import send_video

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.callback_query_handler(lambda call: call.data.startswith('withdraw'), state='*')
async def withdraw(call: types.CallbackQuery, state: FSMContext):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(chat_id=call.from_user.id)
    user = await sync_to_async(telegram_user.get_user, thread_sensitive=True)()

    await call.answer()
    await call.message.edit_text(
        text=f"""💰 Баланс: {telegram_user.balance}$
<i>Вывести средства?</i>
Или заработать дополнительно:
- 💰 +10$ за аĸцию "Пригласить друга".
- 💶 +0.5$ за просмотр реĸламных видео.

<b>Выберите метод оплаты:</b>""",
        reply_markup=await payment_method()

    )
