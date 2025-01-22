import logging
from random import randint

from asgiref.sync import sync_to_async
from robot.models import TelegramUser, Video
import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from robot.keyboards.inline import choose_tariff
from robot.utils import send_video

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.callback_query_handler(lambda call: call.data.startswith('add_method'), state='*')
async def add_method(call: types.CallbackQuery, state: FSMContext):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(chat_id=call.from_user.id)
    user = await sync_to_async(telegram_user.get_user, thread_sensitive=True)()

    await call.answer()
    await call.message.edit_text(
        text=f"""❌ К сожалению на базовом тарифе редаĸтировать методы оплаты нельзя.
♻ Пожалуйста, смените тариф на Индивидуальный или выше.
🎁 Аĸция для новых пользователей: Индивидуальный тариф за 0.15$!""",
        reply_markup=await choose_tariff()
    )
