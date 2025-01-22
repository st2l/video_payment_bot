import logging
from random import randint

from asgiref.sync import sync_to_async
from robot.models import TelegramUser, Video
import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from robot.keyboards.inline import main_menu_kb
from robot.utils import send_video

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.callback_query_handler(lambda call: call.data == 'cancel', state='*')
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text='Выберите действие:',
        reply_markup=await main_menu_kb()
    )
