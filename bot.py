import telebot
from telebot import types  # Для указания типов
import config  # Импортируем файл конфигурации с токеном

bot = telebot.TeleBot(config.token)

# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос❓")
    markup.add(btn1, btn2)
    return markup

# Подменю для вопросов
def question_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Как меня зовут?")
    btn2 = types.KeyboardButton("Что я могу?")
    back = types.KeyboardButton("⬅️ Вернуться в главное меню")
    markup.add(btn1, btn2, back)
    return markup

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = main_menu()
    bot.send_message(
        message.chat.id,
        text=f"Здравствуйте, {message.from_user.first_name}! Я тестовый бот для твоей статьи на https://github.com/Vyacheslav-programmer/Python",
        reply_markup=markup
    )

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Поздороваться":
        bot.send_message(message.chat.id, text="Привет.. Спасибо, что читаете статью!)")
    
    elif message.text == "Задать вопрос❓":
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=question_menu())
    
    elif message.text == "Как меня зовут?":
        bot.send_message(message.chat.id, {message.from_user.first_name})
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Я могу поздороваться и ответить на твои вопросы!")
    
    elif message.text == "Какой язык программирования лучше?":
        bot.send_message(message.chat.id, text="Это зависит от ваших нужд! Python, Java и JavaScript популярны в разных сферах.")
        
    elif message.text == "⬅️ Вернуться в главное меню":
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=main_menu())
    
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован..")

bot.polling(none_stop=True)
