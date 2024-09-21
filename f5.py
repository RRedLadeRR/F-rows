#Timofey
def weather_report(city, temperature, humidity, weather_description):
  return f"Погода в місті {city}:\nТемпература: {temperature}°C\nВологість: {humidity}%\n{weather_description}"

city = input("Введіть назву міста: ")
temperature = float(input("Введіть температуру: "))
humidity = int(input("Введіть вологість: "))
weather_description = input("Введіть опис погоди: ")

print(weather_report(city, temperature, humidity, weather_description))