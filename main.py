import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6251993066:AAFG0CJmZsLUqOYDIvRsEK1Js7wrN-7Oucs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler(text="soqqa")
async def echo(message: types.Message):
    # Making our request
    url = 'https://v6.exchangerate-api.com/v6/API_KEY/pair/USD/UZS'
    response = requests.get(url)
    data = response.json()['conversion_rate']
    await message.answer(float(f"1 dollar = {data}so'm")
)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)