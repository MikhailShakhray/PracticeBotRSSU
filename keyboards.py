from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_hi = KeyboardButton('Привет! 👋')

button_post = KeyboardButton('Предложить пост в канал')

post_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
                              ).add(button_post)

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True
                               ).add(button_hi)

