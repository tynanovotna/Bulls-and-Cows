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

def bulls_and_cows_count(hidden_number, players_number):
    bulls = 0
    cows = 0
    for index in range(len(players_number)):
        number = int(players_number[index])
        if number == hidden_number[index]:
            bulls += 1
        else:
            if number in hidden_number:
                cows += 1
    if bulls == 1:
        print(f"{bulls} bull.")
    else:
        print(f"{bulls} bulls.")
    if cows == 1:
        print(f"{cows} cow.")
    else:
        print(f"{cows} cows.") 
    return bulls
            
def game_end(bulls):
    if bulls == 4:
        return True
    return False        

def hidden_number():
    all_numbers = random.sample(range(10), 4)
    while all_numbers[0] == 0 and all_numbers[0] in all_numbers:
        all_numbers[0] = random.randint(1, 9)
    return all_numbers

playing_game()
print(hidden_number())
