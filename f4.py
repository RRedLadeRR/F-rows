#Timofey
import random

def generate_ticket(last_name, destination, departure_time):
  ticket_number = random.randint(100000, 999999)
  return f"Квиток №{ticket_number}\nПрізвище: {last_name}\nПункт призначення: {destination}\nЧас відправлення: {departure_time}"

last_name = input("Введіть ваше прізвище: ")
destination = input("Введіть пункт призначення: ")
departure_time = input("Введіть час відправлення: ")

print(generate_ticket(last_name, destination, departure_time))