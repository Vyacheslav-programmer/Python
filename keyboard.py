from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
kb.insert(KeyboardButton('/help')).insert(KeyboardButton('/description')).insert(KeyboardButton('Random photo'))

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
kb_photo.add(KeyboardButton('Рандом'), KeyboardButton('Главное меню'))