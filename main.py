#!/bin/python

'''
Name:           main.py
Version:        0.1
Description:    Main program file for bet calculator project.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         https://github.com/zkotani
'''

import odds_calculator
import bet_calculator

def options_menu():
    print('\nProgram options:')
    print('1. Odds Calculator')
    print('2. Bet Calculator')
    print('3. Quit')

bet_calculator.greeting()
options_menu()
while True:
    try:
        user_option = int(input('\nWhich option would you like to choose?\n> '))
        if user_option not in range(1, 4):
            raise ValueError
    except ValueError:
        print('\nError! Option must be a valid number from 1-3, try again.')
        continue
    break
match user_option:
    case 1:
        pass
    case 2:
        odds_calculator.odds_calc()
    case 3:
        bet_calculator.exit_program('\nAre you sure you would like to exit? [y/n]\n > ')
