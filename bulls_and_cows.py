"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN #4503
"""

import random
import time

SEPARATOR = "-" * 47

print("Hi there!")
print(SEPARATOR)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(SEPARATOR)

def playing_game():
    while True:
        start_time = time.time()
        players_number = input("Enter a number: ")
        if not players_number.isnumeric():
            print("Given input is not number. Try again.")
        elif int(players_number) < 1000 or int(players_number) > 9999:
            print("Enter only 4 digit number. Try again.")
        end_time = time.time()
        break
    return players_number

def control_numbers():
    players_numbers = playing_game()
    generated_numbers = generate_numbers()
    for number in players_numbers:
        if int(number) in generated_numbers:
            pass

def generate_numbers():
    all_numbers = random.sample(range(10), 4)
    while all_numbers[0] == 0 and all_numbers[0] in all_numbers:
        all_numbers[0] = random.randint(1, 9)
    return all_numbers

control_numbers()
playing_game()
print(generate_numbers())
