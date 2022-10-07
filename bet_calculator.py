'''
Name -- bet_calculator
Version -- 1.1
Description -- Simple python script used to automate sports betting.
    Calculates amount for individual bets based on percentages of a main pool.
Developer -- Zyphlen Kotani [zkotani@gmail.com]
Github -- http://github.com/zkotani
'''

# Imports

import re # Regular expression support
import sys # Exit function
from time import sleep # Sleep function

# Functions

def exit_program(exit_prompt: str):
    while True:
        # Does the user wish to exit the program?
        exit = input(f'{exit_prompt}')
        if re.fullmatch(('y|Y|n|N'), exit):
            break
        else:
            # Make sure user is entering `y` or `n`
            print('\nError! Please answer using \'y\' or \'n\'.')
            continue
        # Exit if the user has selected yes
    if re.fullmatch('y|Y', exit):
        print('\nThanks for using Bet Calculator!')
        sleep(5)
        print('Bye~')
        sys.exit()

def greeting():
    # Prints greeting strings
    greeting_string = '# Welcome to Bet Calculator v1.1! #' # Welcome string
    greeting_hash = ''
    for char in greeting_string:
        # Creates a string the same number of characters as
        # `greeting_string` made up of `#`
        greeting_hash += '#'
    # Print the greeting to the console
    print(f'\n{greeting_hash}\n{greeting_string}\n{greeting_hash}')

def collect_pool():
    # Collect the total betting pool & number of games to bet on
    while True:
        # Ask user for amount in betting pool
        bet_pool = input('\nHow much money is currently in your betting pool?\n> $')
        # Check to make sure the user has entered the betting pool as:
            # > $1000
            # > $1,000
            # > 1000.00
            # > 1,000.00
        if re.fullmatch("(\d{1,}(,\d{3})*(\.\d{1,2})?)", bet_pool):
            # If the entered value contains commas, remove them
            split_pool = bet_pool.split(',')
            bet_float = ''
            # Add the split strings back together
            for i in range(len(split_pool)):
                bet_float += split_pool[i]
            try:
                # Try to convert the entered value to a float
                bet_float = float(bet_float)
            except ValueError:
                # If the entered value raises a ValueError, let the user know
                print(f'\nError! Please make sure you\'re entering a valid number.')
                continue
        else:
            print('''\nError! Make sure you\'re entering your value in one of the following formats: \
                    \n1. 1000\n2. 1,000\n3. 1000.00\n4. 1,000.00''')
            continue
        # Make sure user is entering a value greater than 0
        if bet_float <= 0:
            # Call exit_program()
            exit_program('\nYou can\'t bet with $0 or less! Exit? [y/n]\n> ')
            continue
        break
    return bet_float

def number_of_bets():
    # Ask the user how many bets will be placed.
    while True:
        try:
            num_bets = int(input('\nHow many bets will be placed?\n> '))
        except ValueError:
            # If there is a value error, let the user know
            print('\nError! Please enter a valid number!')
            continue
        # Make sure user is entering a value greater than 0
        if num_bets <= 0:
            # Call exit_program()
            exit_program('\nError! You can\'t bet on 0 or fewer games! Exit? [y/n]\n> ')
            continue
        break
    return num_bets

def bet_info(total_bets: int):
    all_bets = {}
    for i in range(total_bets):
        while True:
            bet_title = input(f'\nEnter the name of the team or title of bet #{i+1}.\n> ')
            if bet_title in all_bets:
                print('\nError! You\'re already using this name. Try something different.')
                continue
            else:
                while True:
                    title_ok = input(f'\nBet title: {bet_title}? [y/n]\n> ')
                    if re.fullmatch('(y|Y|n|N)', title_ok):
                        break
                    else:
                        print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
                        continue
            if re.fullmatch('(n|N)', title_ok):
                continue
            else:
                break
        while True:
            bet_percent = input(f'\nWhat percentage of your pool is going towards Bet #{i+1}: {bet_title}?\n> %')
            if re.fullmatch('(\d*(\.\d{1,})?)', bet_percent):
                try:
                    float_percent = float(bet_percent)
                except ValueError:
                    print('\nError! Make sure you\'re entering a valid number!')
                    continue
            else:
                print('\nError! Make sure you\'re entering a number between 0-100.')
                continue
            if float_percent <= 0:
                exit_program('\nError! Can\'t bet 0% or less. Exit? [y/n]\n> ')
                continue
            elif float_percent > 100:
                exit_program('\nError! Can\'t bet over 100% Exit? [y/n]\n> ')
                continue                
            while True:
                confirm_bet = input(f'\nYou would like to bet {float_percent}% of your pool on {bet_title}? [y/n]\n> ')
                if re.fullmatch('(y|Y|n|N)', confirm_bet):
                    break
                else:
                    print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
                    continue
            if re.fullmatch('(n|N)', confirm_bet):
                continue
            else:
                break
        all_bets[bet_title] = (float_percent / 100)
    return all_bets

def bet_math(total_pool: float, all_bets: dict):
    calculated_bets = {}
    for k, v in all_bets.items():
        bet_amount = v * total_pool
        calculated_bets[k] = f'{str(v)},{str(bet_amount)}'
    return calculated_bets

greeting()
total_pool = collect_pool()
total_bets = number_of_bets()
all_bets = bet_info(total_bets)
print(all_bets)
calculated_bets = bet_math(total_pool, all_bets)
print(calculated_bets)
