from pprint import pprint
from configs import open_weather_token
import datetime
import requests



def get_weather(city, open_weather_token):
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')

        data = response.json()


        city = data['name']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        temp = data['main']['temp']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        # cur_weather = data['weather']['description']
        wind = data['wind']['speed']

        print(f'''***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***
В городе: {city}
Температура: {temp}°C
Влажность: {humidity}%
Атмосферное давление: {pressure} мм.рт.ст
Скорость ветра: {wind} км/ч
Восход солнца в {sunrise}
Закат солнца в {sunset}
---Хорошего дня!---''')





    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input('Введите название города: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
