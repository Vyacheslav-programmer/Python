from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
import random
import asyncio

from config import TOKEN_API

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN_API)
dp = Dispatcher()

# Клавиатуры
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/help"), KeyboardButton(text="/description"), KeyboardButton(text="Random photo")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_photo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рандом"), KeyboardButton(text="Главное меню")],
    ],
    resize_keyboard=True,
)

# Команды
HELP_COMMAND = """
/start - запуск бота
/help - команды бота
/description - описание бота
"""

photos = [
    "https://lyc1537.mskobr.ru/files/mgtu_logo1.png",
    "https://sun9-23.userapi.com/c4738/g36950/a_e66d070e.jpg",
    "https://sun9-30.userapi.com/impg/5zX5w8X9nZAG9S9w-r-oXY482BTvUJo6Era8QQ/agXJox5Z2fg.jpg?size=2560x1707&quality=95&sign=764d5fcef562a3e1c43dee679edb6cf4&type=album",
]


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет, дорогой друг!", reply_markup=kb)


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(HELP_COMMAND)


@dp.message(Command("description"))
async def description_command(message: Message):
    await message.answer("Наш бот умеет много чего")
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgIAAxkBAAEIq_hkQqSNRRrn1VF5XCXmi-uh4Y8PswACDBMAAoiEyEsOauMaYVUKKy8E",
    )


@dp.message(lambda message: message.text == "Random photo")
async def send_kb_photo(message: Message):
    await message.answer(
        'Чтобы отправить рандомную фотографию нажми на кнопку "Рандом"', reply_markup=kb_photo
    )


@dp.message(lambda message: message.text == "Главное меню")
async def open_kb(message: Message):
    await message.answer("Добро пожаловать в главное меню", reply_markup=kb)


@dp.message(lambda message: message.text == "Рандом")
async def send_photo(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=random.choice(photos))


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())