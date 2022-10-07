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

# Functions

def greeting():
    # Prints greeting strings
    greeting_string = '# Welcome to the Bet Calculator v1.1! #' # Welcome string
    greeting_hash = ''
    for char in greeting_string:
        # Creates a string the same number of characters as
        # `greeting_string` made up of `#`
        greeting_hash += '#'
    # Print the greeting to the console
    print(f'\n{greeting_hash}\n{greeting_string}\n{greeting_hash}')

def pool_and_games():
    # Collect the total betting pool & number of games to bet on
    while True:
        try:
            # Ask user for amount in betting pool -- make sure it can be converted to a float
            bet_pool = input('\nHow much money is currently in your betting pool?\n> $')
            float(bet_pool)
        except ValueError:
            # If the entered value raises a ValueError, let the user know
            print(f'\nError! Please make sure you\'re entering a number.\n')
            continue
        # Check to make sure the user has entered the betting pool as:
            # > $1000
            # > $1,000
            # > 1000.00
            # > 1,000.00
        if re.match('(\d*(,\d{3})*(\.\d{1,2})?)', bet_pool):
            if (',') in bet_pool:
                split_pool = bet_pool.split(',')
                bet_float = ''
                for i in split_pool:
                    bet_pool += split_pool[i]
                bet_float = float(bet_float)
            else:
                bet_float = float(bet_pool)

        else:
            break
        # Make sure user is entering a value greater than 0
        if bet_pool <= 0:
            while True:
                # Does the user wish to exit the program?
                exit = input('\nYou can\'t bet with $0 or less! Exit? [y/n]\n> ')
                if re.match(('y|Y|n|N'), exit):
                    break
                else:
                    # Make sure user is entering `y` or `n`
                    print('\nError! Please answer using \'y\' or \'n\'.')
                    continue
            # Exit if the user has selected yes
            if re.match('y|Y', exit):
                break
            else:
                continue


greeting()
pool_and_games()
