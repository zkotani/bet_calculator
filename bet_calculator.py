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
        break
    return bet_float


greeting()
total_pool = collect_pool()

