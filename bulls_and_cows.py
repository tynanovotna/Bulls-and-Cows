"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN #4503
"""

import random
import time
from math import floor

SEPARATOR = "-" * 47

def playing_game():
    start_time = time.time()
    number = hidden_number()
    while True:
        players_number = input("Enter a number: ")
        print(SEPARATOR)
        if not players_number.isnumeric():
            print("Given input is not number. Try again.")
        elif int(players_number) < 1000 or int(players_number) > 9999:
            print("Enter only 4 digit number. Try again.")
        bulls, cows = bulls_and_cows_count(number, players_number)
        #bull, cow = guesing_result(bulls, cows)
        print(f"{bulls} bulls, {cows} cows.")
        end_game = check_game_end(bulls)
        if end_game == True:
            break 
    end_time = time.time()
    print(SEPARATOR)
    print("Time played: ", floor(end_time - start_time), "s.")
    print(SEPARATOR)
    play_again()
    return players_number

def welcome_player():
    print("Hi there!")
    print(SEPARATOR)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)
    
def play_again():
    another_game = input("Would you like play another game? Y/N ").lower()
    if another_game == "y" or another_game == "yes":
        print("superb")
    elif another_game == "n" or another_game == "no":
        pass
    else:
        print("Wrong answer, try again.")
        play_again()
            
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
    return bulls, cows

def guesing_result(bulls, cows):
    if bulls == 1 or cows == 1:
        bull = "bull"
        cow = "cow"
    else:
        bull = "bulls"
        cow = "cows"     
    return bull, cow

def check_game_end(bulls):
    if bulls == 4:
        return True
    return False        

def hidden_number():
    all_numbers = random.sample(range(10), 4)
    while all_numbers[0] == 0 and all_numbers[0] in all_numbers:
        all_numbers[0] = random.randint(1, 9)
    return all_numbers

welcome_player()
playing_game()

