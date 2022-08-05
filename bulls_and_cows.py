"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kristýna Novotná
email: tynadanielova@seznam.cz
discord: KristýnaN #4503
"""

import random
import time

SEPARATOR = "-" * 50
GAME_RULES = """
Game goal is guessing the 4 digit number.
Your number must be in range 1000 - 9999
and each digit must be unique.
Right number and position is called Bull/s.
Right number but false position is called Cow/s.""" 

def playing_game(statistics):
    start_time = time.time()
    number = hidden_number()
    count = 1
    while True:
        players_number = players_input()
        bulls, cows = bulls_and_cows_count(number, players_number)
        end_game = guesing_result(bulls, cows)
        if end_game:
            break
        count += 1 
    end_time = time.time()
    total_time = end_time - start_time
    print_results(total_time, count)
    statistics[len(statistics) + 1] = [total_time, count]
    play_again(statistics)
       
def welcome_player():
    print("Hi there!")
    print(SEPARATOR)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)
    show_game_rules = input("Would you like to see Bulls and Cows rules? Y/N ").lower()
    if show_game_rules in ["y", "yes"]:
        print(GAME_RULES)
    print(SEPARATOR)
    statistics = {}
    playing_game(statistics)

def players_input():
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
        no_duplicates = set()
        for number in players_number:
            no_duplicates.add(number)
        if len(no_duplicates) < 4:
            print("Duplicit numbers. Try again.")
            print(SEPARATOR)
        else:
            break
    return players_number        

def play_again(statistics):
    another_game = input("Would you like to play another game? Y/N ").lower()
    print(SEPARATOR)
    if another_game in ["y", "yes"]:
        playing_game(statistics)
    elif another_game in ["n", "no"]:
        print_statistics(statistics)
    else:
        print("Wrong answer, try again.")
        play_again(statistics)

def print_statistics(statistics):
    sum_time = 0
    sum_count = 0
    for game in statistics:
        count = statistics[game][1]
        total_time = statistics[game][0]
        minutes = int(total_time / 60)
        seconds = int(total_time % 60)
        sum_count += count
        sum_time += total_time
        print(f"Game no.{game} ended in {count} guesses & {minutes} min {seconds} s.")
    mean_count = sum_count / len(statistics)
    mean_time = sum_time / len(statistics) 
    minutes = int(mean_time / 60)
    seconds = int(mean_time % 60)
    print(f"Average results: {mean_count} guesses & {minutes} min {seconds} s.")   
        
def print_results(total_time, count):
    minutes = int(total_time / 60)
    seconds = int(total_time % 60)
    if minutes < 1:
        phrase = "Amazing"
    elif minutes < 2:
        phrase = "Quite good"
    elif minutes < 3:
        phrase = "Average"
    elif minutes < 4:
        phrase = "not so good"
    else:
        phrase = "very bad"
    print(SEPARATOR)
    print(f"Correct, you've guessed the right number in {count} \nguesses, {minutes} min & {seconds} s!")
    print(f"That's {phrase}!")
    print(SEPARATOR)
      
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
    bull = "bull"
    cow = "cow"
    if bulls != 1:
        bull += "s"
    if cows != 1:
        cow += "s"
    if bulls < 4:
        print(f"{bulls} {bull}, {cows} {cow}.")
        print(SEPARATOR)
        return False
    return True
     
def hidden_number():
    hidden_number = random.sample(range(10), 4)
    while hidden_number[0] == 0 and hidden_number[0] in hidden_number:
        hidden_number[0] = random.randint(1, 9)
    return hidden_number

welcome_player()