import requests
from bs4 import BeautifulSoup

html = requests.get('http://127.0.0.1:5500/homework/simple.html')
soup = BeautifulSoup(html.text, 'html.parser')

tbody = soup.find('tbody')
rows = tbody.find_all('tr')

weather_data = []
print("Weather data: ")
for tr in rows:
    tds = tr.find_all('td')
    day = tds[0].text
    temp = tds[1].text 
    condition = tds[2].text
    weather_data.append({'day': day, 'temp': temp, 'condition': condition})
    print(f'day: {day}, temperature: {temp}, condition: {condition}')
print("-"*60)
print('\n')
# print(weather_data)
highest_temp = weather_data[0].copy()
temps = []
for row in weather_data:
    temp_w = int(row['temp'][:2])
    temp_h = int(highest_temp['temp'][:2])
    temps.append(temp_w)
    if temp_w > temp_h: 
        highest_temp['day'] = row['day']
        highest_temp['temp'] = row['temp']
        highest_temp['condition'] = row['condition']
print(f"The highest temperature day: {highest_temp['day'], highest_temp['temp'], highest_temp['condition']}")

sunny_day = []
for row in weather_data:
    if row['condition'] == "Sunny":
        sunny_day.append(row)

print("Sunny days: ")
for day in sunny_day:
    print(f'day: {day['day']}, temp: {day['temp']}, condition: {day['condition']}')

average_temp = sum(temps)/len(temps)
print(f"The average temperature: {average_temp}")