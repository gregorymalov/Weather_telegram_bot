import requests
from config import token, bot_api
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from main import get_weather

bot = Bot(token=bot_api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler(commands=['help'])

async def send_help(message: types.Message):
    await message.reply("Помоги себе сам! =)!")

@dp.message_handler()
async def weather_get(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&units=metric"
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        await message.reply(f"Погода в городе {city}:\nтемпература: {cur_weather}С\nвлажность: {humidity}%\nощущается как: {feels_like}C")

    except:
        await message.reply('Проверте название города')

if __name__ == '__main__':
    executor.start_polling(dp)