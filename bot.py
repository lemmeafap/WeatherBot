from aiogram import Bot, Dispatcher, executor, types
from configs import open_weather_token, BOT_TOKEN
import datetime
import requests

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply('👋Привет! Введите город в котором хотите узнать информацию о погоде☔.')

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')

        data = response.json()

        city = data['name']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        temp = data['main']['temp']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        # cur_weather = data['weather']['description']
        wind = data['wind']['speed']

        await message.reply(f'''***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***
В городе: {city}
Температура: {temp}°C
Влажность: {humidity}%
Атмосферное давление: {pressure} мм.рт.ст
Скорость ветра: {wind} км/ч
Восход солнца в {sunrise}
Закат солнца в {sunset}
---Хорошего дня!---''')


    except Exception as ex:
        await message.reply(ex)
        await message.reply('Проверьте название города')


if __name__ == '__main__':
    executor.start_polling(dp)
