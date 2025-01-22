import logging
from random import randint

from asgiref.sync import sync_to_async
from robot.models import TelegramUser, Video
import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from robot.keyboards.inline import oformit_individual
from robot.utils import send_video

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.callback_query_handler(lambda call: call.data.startswith('tariffs'), state='*')
async def tarrifs(callback: types.CallbackQuery, state: FSMContext):

    await callback.answer()
    await callback.message.edit_text(
        text="""<b>Тариф - BASIC</b>
Цена — 0$
- 5 видео в день
- 5 видео в месяц
Тариф просмотра: 0.5$

<b>Тариф - INDIVIDUAL</b>
Цена — 15$
- 50 видео в день
- 1 500 видео в день
Тариф просмотра: 0.5$
🎁 Аĸция для новых пользователей: INDIVIDUAL тариф — 15 $ за 0.15$
на первый месяц!

<b>Тариф - Premium</b>
Цена — 15$
- 500 видео в день
- 15 000 видео в день
Тариф просмотра: 0.5$
Подĸлючение по запросу тольĸо для опытных пользователей бота.""",
        reply_markup=await oformit_individual(),

    )
