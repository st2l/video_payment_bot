import logging
from random import randint

from asgiref.sync import sync_to_async
from robot.models import TelegramUser, Video
import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from robot.keyboards.inline import cancel
from robot.utils import send_video

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.callback_query_handler(lambda call: call.data.startswith('stats'), state='*')
async def stats(call: types.CallbackQuery, state: FSMContext):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(chat_id=call.from_user.id)
    user = await sync_to_async(telegram_user.get_user, thread_sensitive=True)()

    await call.answer()
    await call.message.edit_text(
        text=f"""Имя: {call.from_user.full_name}
Username: {call.from_user.username}
Статус: ✅ Верифицирован
Баланс счета: {telegram_user.balance}$
Просмотров: 5
Друзей приглашено: 0

А вот, чего добились мы 🥇
Статистиĸа за 17.01.2025: аĸтуальная дата сегодняшнего дня
🥇 Пользователей сегодня: {randint(1500, 2000)} человеĸ.
🥇 Заработали: {randint(20000000, 30000000)}$.
🥇 Всего посмотрели: {randint(400100, 600000)} видео.""",
        reply_markup=await cancel()
    )
