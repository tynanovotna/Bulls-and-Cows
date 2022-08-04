"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN #4503
"""

import random
import time

SEPARATOR = "-" * 47

def playing_game():
    start_time = time.time()
    number = hidden_number()
    count = 1
    while True:
        players_number = input("Enter a number: ")
        if not players_number.isnumeric():
            print("Given input is not number. Try again.")
            print(SEPARATOR)
            continue
        elif int(players_number) < 1000 or int(players_number) > 9999:
            print("Enter only 4 digit number. Try again.")
            print(SEPARATOR)
            continue
        bulls, cows = bulls_and_cows_count(number, players_number)
        bull, cow = guesing_result(bulls, cows)
        print(f"{bulls} {bull}, {cows} {cow}.")
        print(SEPARATOR)
        end_game = check_game_end(bulls)
        if end_game:
            break
        count += 1 
    end_time = time.time()
    total_time = end_time - start_time
    minutes = int(total_time / 60)
    seconds = int(total_time % 60)
    print(SEPARATOR)
    print(f"Correct, you've guessed the right number in {count} \nguesses, {minutes} minutes & {seconds} seconds!")
    print("That's Amazing!")
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
    another_game = input("Would you like to play another game? Y/N ").lower()
    print(SEPARATOR)
    if another_game == "y" or another_game == "yes":
        playing_game()
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
    if bulls == 1:
        bull = "bull"
    else:
        bull = "bulls"
    if cows == 1:
        cow = "cow"
    else:
        cow = "cows"  
    return bull, cow

def check_game_end(bulls):
    if bulls == 4:
        return True
    return False        

def hidden_number():
    hidden_number = random.sample(range(10), 4)
    while hidden_number[0] == 0 and hidden_number[0] in hidden_number:
        hidden_number[0] = random.randint(1, 9)
    return hidden_number

welcome_player()
playing_game()

