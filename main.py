from config import token
import requests
from pprint import pprint

def get_weather(city, token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f"Погода в городе {city}:\nтемпература: {cur_weather}С\nвлажность: {humidity}%\nощущается как: {feels_like}C")

        if cur_weather <= 0:
            print("Дубак")
        else: 
            print("Отличная погода!")

    except Exception as ex:
        print(ex)
        print('Проверте название города')

def main():
    city = input("Введите город: ")
    get_weather(city, token)

if __name__ == '__main__':
    main()