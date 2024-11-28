from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Определим состояния
START, STATE1, STATE2 = range(3)

# Хранилище для отслеживания состояния пользователя
user_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_state[update.effective_user.id] = START
    await update.message.reply_text(
        "Привет! Вы находитесь в начальном состоянии. Напишите '/state1', чтобы перейти в состояние 1."
    )

async def to_state1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_state[update.effective_user.id] = STATE1
    await update.message.reply_text(
        "Вы перешли в состояние 1. Напишите '/state2', чтобы перейти в состояние 2, или '/start', чтобы вернуться в начальное состояние."
    )

async def to_state2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_state[update.effective_user.id] = STATE2
    await update.message.reply_text(
        "Вы перешли в состояние 2. Напишите '/start', чтобы вернуться в начальное состояние, или '/state1', чтобы вернуться в состояние 1."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_state = user_state.get(update.effective_user.id, START)
    if current_state == START:
        await update.message.reply_text(
            "Вы в начальном состоянии. Используйте команды для перехода между состояниями."
        )
    elif current_state == STATE1:
        await update.message.reply_text(
            "Вы в состоянии 1. Используйте команды для изменения состояния."
        )
    elif current_state == STATE2:
        await update.message.reply_text(
            "Вы в состоянии 2. Используйте команды для изменения состояния."
        )

def main() -> None:
    application = Application.builder().token("7683628759:AAGdy5YjJH_2uhGXpguX5PXKqnLRmACzhWs").build()

    # Команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("state1", to_state1))
    application.add_handler(CommandHandler("state2", to_state2))
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
