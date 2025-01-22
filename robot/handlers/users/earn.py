import logging
from random import randint
from datetime import datetime

from asgiref.sync import sync_to_async
from robot.models import TelegramUser, Video
import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from robot.keyboards.inline import oznakomlen_kb, prosmotreno_kb, cancel
from robot.utils import send_video

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


@dp.callback_query_handler(lambda call: call.data == 'earnmoney', state='*')
async def earnmoney(call: types.CallbackQuery, state: FSMContext):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(chat_id=call.from_user.id)
    user = await sync_to_async(telegram_user.get_user, thread_sensitive=True)()

    logging.info(
        f'dtdd: {telegram_user.last_time_wathed - (24*60*60)} and datetime = {datetime.now().timestamp()}')
    if telegram_user.last_time_wathed + (24*60*60) < datetime.now().timestamp():
        telegram_user.can_watch = 5
        await sync_to_async(telegram_user.save, thread_sensitive=True)()

    await call.answer()
    if telegram_user.can_watch < 1:
        await call.message.edit_text('❌ У вас закончились просмотры. Приходите завтра!', reply_markup=await cancel())
    else:
        video = await send_video()
        await call.message.answer_video(
            caption=f"""📱 Тариф просмотра: 0.5$
✅ Выполнено: 0 из 5
💰 Ваш баланс: {telegram_user.balance} $""",
            video=open(str(video), 'rb'),
            reply_markup=await prosmotreno_kb(dt='prosmotreno')
        )

        telegram_user.can_watch -= 1
        telegram_user.last_time_wathed = datetime.now().timestamp()
        await sync_to_async(telegram_user.save, thread_sensitive=True)()


@dp.callback_query_handler(lambda call: call.data == 'prosmotreno')
async def second_prosmotreno(callback: types.CallbackQuery, state: FSMContext):
    telegram_user, _ = await TelegramUser.objects.aget_or_create(chat_id=callback.from_user.id)
    user = await sync_to_async(telegram_user.get_user, thread_sensitive=True)()

    telegram_user.balance = telegram_user.balance + 0.5
    await sync_to_async(telegram_user.save, thread_sensitive=True)()

    await callback.message.answer(f'✅ Видео просмотрено\nБаланс {telegram_user.balance - 0.5}$ -> {telegram_user.balance}$')

    logging.info(
        f'dtdd: {telegram_user.last_time_wathed - (24*60*60)} and datetime = {datetime.now().timestamp()}')
    if telegram_user.last_time_wathed + (24*60*60) < datetime.now().timestamp():
        telegram_user.can_watch = 5
        await sync_to_async(telegram_user.save, thread_sensitive=True)()

    await callback.answer()
    if telegram_user.can_watch < 1:
        await callback.message.answer('❌ У вас закончились просмотры. Приходите завтра!', reply=await cancel())
    else:
        video = await send_video()
        await callback.message.answer_video(
            caption=f"""📱 Тариф просмотра: 0.5$
✅ Выполнено: 0 из 5
💰 Ваш баланс: {telegram_user.balance} $""",
            video=open(str(video), 'rb'),
            reply_markup=await prosmotreno_kb(dt='prosmotreno')
        )

        telegram_user.can_watch -= 1
        telegram_user.last_time_wathed = datetime.now().timestamp()
        await sync_to_async(telegram_user.save, thread_sensitive=True)()
