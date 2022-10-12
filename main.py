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
            print(f'Your file will be saved as: \'{new_file}\'')
            bet_float = functions.collect_pool()
            num_bets = functions.number_of_bets(games_or_bets='games')
            test = functions.bet_info(total_bets=num_bets, games_or_bets='games')
            print(test)
            # team_1_bet = round(((team_1_kelly / 100) * bet_pool), 2)
            # team_2_bet = round(((team_2_kelly / 100) * bet_pool), 2)
            # print(f'\n{team_1} has a {round(team_1_odds, 2)}% implied winning probability.')
            # print(f'{team_1} has a projected winning probability of {proj_percent_1}%')
            # print(f'{team_1}\'s Kelly % is: {round(team_1_kelly, 2)}%')
            # print(f'A suggested bet on {team_1} would be: ${team_1_bet} for a return of: ${round(team_1_bet * team_1_prob, 2)}')
            # print(f'\n{team_2} has a {round(team_2_odds, 2)}% implied winning probability.')
            # print(f'{team_2} has a projected winning probability of {proj_percent_2}%')
            # print(f'{team_2}\'s Kelly % is: {round(team_2_kelly, 2)}%')
            # print(f'A suggested bet on {team_2} would be: ${team_2_bet} for a return of: ${round(team_2_bet * team_2_prob, 2)}')
        case 2:
            print('not working yet')
            continue
        case 3:
            functions.exit_program('\nAre you sure you would like to exit? [y/n]\n > ')