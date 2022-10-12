#!/bin/python

'''
Name:           main.py
Version:        0.9
Description:    Main program file for bet calculator project.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         https://github.com/zkotani
'''

import re
import functions

import odds_calculator
import bet_calculator


functions.greeting('# Welcome to Bet Calculator v1.0! #')
while True:
    functions.options_menu()
    try:
        user_option = int(input('\nWhich option would you like to choose?\n> '))
        if user_option not in range(1, 4):
            raise ValueError
    except ValueError:
        print('\nError! Option must be a valid number from 1-3, try again.')
        continue
    match user_option:
        case 1:
            new_file = functions.create_file()
            print(f'\nYour file will be saved as: \'{new_file}\'')
            bet_float = functions.collect_pool()
            num_bets = functions.number_of_bets('games')
            bets_dict = functions.bet_info(num_bets, bet_float, 'games')
            for key, val in bets_dict.items():
                team_name = key
                team_info = val
                functions.save_to_file(
                    new_file,
                    team_name,
                    team_info
                )
            print(f'\nYour bets have been saved to: \'{new_file}\'')
        case 2:
            print('\nnot working yet')
            continue
        case 3:
            functions.exit_program('\nAre you sure you would like to exit? [y/n]\n > ')