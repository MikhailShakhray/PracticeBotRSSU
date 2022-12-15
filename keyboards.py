# import types
#
# import kb as kb
# from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils import executor
#
# from main import dp
#
#
# @dp.message_handler(commands=['start'])
# async  def keyboards(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton('Привет! 👋'),
#             types.KeyboardButton('Предложить пост в канал'),
#             types.KeyboardButton('Вопросы и ответы')
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#     await message.reply('Привет еще раз', reply_markup=keyboard)
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
