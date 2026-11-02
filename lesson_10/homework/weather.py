import json
import requests

with open("config.json", 'rt') as file:
    reader = json.load(file)
    API_key = reader["api_key_weather"]

city = "Tashkent"
# API_key = "6c53eb6c3bc3b8e93a8d15a636d61f8f"

base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
res = requests.get(base_url)
data = res.json()
temp = data['main']['temp']
feels_like = data['main']['feels_like']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

print(f"The temperature of {city} is {temp} C")
print(f"The weather feels like {feels_like} C")
print(f"The humidity of {city} is {humidity}%")
print(f"The weather description of {city} is {description}")
