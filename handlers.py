from random import randint
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, InputFile

from main import dp, bot


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Выберите пункт меню!")


@dp.message_handler(commands=['start'])
async  def keyboards(message: types.Message):
    kb = [
        [
            types.KeyboardButton('Привет! 👋'),
            types.KeyboardButton('Предложить пост в канал'),
            types.KeyboardButton('Вопросы и ответы')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply(reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    kb = [
        [
            types.KeyboardButton('Привет! 👋'),
            types.KeyboardButton('Предложить пост в канал'),
            types.KeyboardButton('Вопросы и ответы')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.reply(reply_markup=keyboard)
    me = await bot.get_me()
    kb1 = types.InlineKeyboardMarkup()
    kb1.insert(types.InlineKeyboardButton(text="Бесплатная консультация", callback_data="Konsult"))
    kb1.add(types.InlineKeyboardButton(text="О компании", callback_data="Company"))
    kb1.insert(types.InlineKeyboardButton(text="Собрать 🤖", callback_data="robot"))
    kb1.add(types.InlineKeyboardButton(text="🤖 в коробке", url='https://houston1304.github.io/practiceBot'))
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
 {message.from_user.first_name}, выберите пункт меню 👇🏻''', )

@dp.callback_query_handler(text_contains='')
async def qr_message(call:types.callback_query):
    code = call.data
    match code:
        case "Company":
            await bot.send_message(call.from_user.id, "Все классная компания кста")
        case "contacts":
            await bot.send_message(call.from_user.id, "+79151488228")
        case "robot_box":
            await bot.answer(url='https://houston1304.github.io/practiceBot')


if __name__ == '__main__':
    executor.start_polling(dp)
