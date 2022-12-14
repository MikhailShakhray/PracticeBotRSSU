import asyncio
from os import listdir
from os.path import isfile, join
from random import randint
from unittest.mock import call
import logging

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode, ChatActions, InputMediaPhoto, InputMediaVideo, InlineKeyboardButton, \
    InputFile, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import pre

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
Photo = InputFile("C:/Users/user/Desktop/бот/icon.jpg")
Voice = InputFile("C:/Users/user/Desktop/ПАПКА/1/Абоба.mp3")


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    me = await bot.get_me()
    kb1 = types.InlineKeyboardMarkup()
    kb1.insert(types.InlineKeyboardButton(text="Бесплатная консультация", callback_data="Konsult"))
    kb1.add(types.InlineKeyboardButton(text="О компании", callback_data="Company"))
    kb1.insert(types.InlineKeyboardButton(text="Собрать 🤖", callback_data="robot"))
    kb1.add(types.InlineKeyboardButton(text="🤖 в коробке", callback_data="robot_box"))
    kb1.insert(types.InlineKeyboardButton(text="🔥Предожение", callback_data="offer"))
    kb1.add(types.InlineKeyboardButton(text="Про бот N.", callback_data="bot_info"))
    kb1.insert(types.InlineKeyboardButton(text="Контакты", callback_data="contacts"))
    kb1.add(types.InlineKeyboardButton(text="Поделится", callback_data="share"))
    await bot.send_photo(message.from_user.id, InputFile("icon.jpg"), reply_markup=kb1, caption=f'''🤖 Автодайлер «Бот N.»
Голосовой робот-помощник для бизнеса

🔥передает голосовые сообщения, распознает ответы Человека, анализирует и умеет вести диалог
🔥 умный секретарь для входящих звонков

✓ оповещение об акциях
✓ приглашение на вебинар/мероприятие
✓ проведение опросов, анкетирование
✓ фильтрация базы номеров
✓ повышение лояльности клиентов
✓ лидогенерация и многое другое…
_____
{message.from_user.first_name}, выберите пункт меню 👇🏻''')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


if __name__ == '__main__':
    executor.start_polling(dp)



