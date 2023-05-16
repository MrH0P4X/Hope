import os
import openai
import cchardet
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='6226444821:AAFii5yubWZPvAgZwo6p_m9n4bZlBwmYwMw')
dp = Dispatcher(bot)

openai.api_key = os.getenv("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")

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply('Hello! How can I help you?')

@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=message.text,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    await message.reply(response.choices[0].text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)