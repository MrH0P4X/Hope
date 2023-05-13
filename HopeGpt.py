import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

telegram_token = '6033107776:AAGjmtKUWr_Rur74S8SgRVXc3KqqPlACPIw'
openai.api_key = "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"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a GPT bot Made By Mr Hope. Send me any text and I'll generate a response using OpenAI's GPT-3 model.")

def echo(update, context):
    text = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

def main():
    updater = Updater(token=telegram_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()