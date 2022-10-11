#!/bin/python

'''
Name:           main.py
Version:        0.9
Description:    Main program file for bet calculator project.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         https://github.com/zkotani
'''

import odds_calculator
import bet_calculator
import re

def options_menu():
    print('\nProgram options:')
    print('1. Odds Calculator')
    # print('2. Bet Calculator')
    print('2. Quit')

bet_calculator.greeting('# Welcome to Bet Calculator v1.1! #')
while True:
    options_menu()
    try:
        user_option = int(input('\nWhich option would you like to choose?\n> '))
        if user_option not in range(1, 3):
            raise ValueError
    except ValueError:
        print('\nError! Option must be a valid number from 1-3, try again.')
        continue
    match user_option:
        case 1:
            write_file = input('\nEnter the name of the file you want to write output to.\n> ')
            for i in write_file:
                # if the character is '\'
                if i == '\\':
                    # change it to '/' so python can parse it
                    i = '/'
            # split the string into a list from the right
            # using '.' as the delimiter
            split_file_1 = write_file.rsplit('.', maxsplit=1)
            try:
                # if the last element of the split list is not 'txt'
                if split_file_1[1] != 'txt':
                    # change it to 'txt'
                    split_file_1[1] = 'txt'
            # if there is only 1 item in the split list
            except IndexError:
            # append 'txt' to the list
                split_file_1.append('txt')
            # join the elements together with a '.'
            # file becomes 'filename.txt'
            write_file = '.'.join(split_file_1)
            # open user inputted output file in write+ mode
            # use name as 'chk_empty' to work with file
            with open(write_file, mode='w+', encoding='utf-8') as chk_empty:
                try:
                # try to read the lines in the file
                    chk_empty.readlines()
                except IOError:
                    # if the file does not exist, write an empty file
                    chk_empty.write('')
            bet_pool = bet_calculator.collect_pool()
            number_of_games = bet_calculator.number_of_bets()
            for i in range(int(number_of_games)):
                bet_calculator.greeting(f'# GAME #{i + 1 } #')
                team_1, team_1_odds, team_1_kelly, team_2, team_2_odds, team_2_kelly, \
                    proj_percent_1, proj_percent_2, team_1_prob, team_2_prob = odds_calculator.odds_calc()
                team_1_bet = round(((team_1_kelly / 100) * bet_pool), 2)
                team_2_bet = round(((team_2_kelly / 100) * bet_pool), 2)
                print(f'\n{team_1} has a {team_1_odds}% implied winning probability.')
                print(f'{team_1} has a projected winning probability of {proj_percent_1}%')
                print(f'{team_1}\'s Kelly % is: {team_1_kelly}%')
                print(f'A suggested bet on {team_1} would be: ${team_1_bet} for a return of: ${round(team_1_bet * team_1_prob, 2)}')
                print(f'\n{team_2} has a {team_2_odds}% implied winning probability.')
                print(f'{team_2} has a projected winning probability of {proj_percent_2}%')
                print(f'{team_2}\'s Kelly % is: {team_2_kelly}%')
                print(f'A suggested bet on {team_2} would be: ${team_2_bet} for a return of: ${round(team_2_bet * team_2_prob, 2)}')
                try:
                    # open user inputted output file in read mode
                    with open(write_file, mode='r', encoding='utf-8') as read_file:
                        try:
                            # create a list of all lines in the file
                            read_lines = [i for i in read_file]
                            # copy the last element to variable last_line
                            last_line = read_lines[-1]
                            # copy the last character in the string to variable last_char
                            last_char = list(last_line[-1])
                        except IndexError:
                            # if the file is empty make last_char a newline
                            last_char = '\n'
                        # if the last character is a newline or file is empty
                    if '\n' in last_char:
                        # open the user inputted output file in append mode
                        # use the name write_odds to work with the file
                        with open(write_file, mode='a', encoding='utf-8') as write_odds:
                            write_odds.write(f'\n{team_1} has a {team_1_odds}% implied winning probability.')
                            write_odds.write(f'\n{team_1} has a projected winning probability of {proj_percent_1}%')
                            write_odds.write(f'\n{team_1}\'s Kelly % is: {team_1_kelly}%')
                            write_odds.write(f'\nA suggested bet on {team_1} would be: ${team_1_bet} for a return of: ${round(team_1_bet * team_1_prob, 2)}')
                            write_odds.write(f'\n\n{team_2} has a {team_2_odds}% implied winning probability.')
                            write_odds.write(f'\n{team_2} has a projected winning probability of {proj_percent_2}%')
                            write_odds.write(f'\n{team_2}\'s Kelly % is: {team_2_kelly}%')
                            write_odds.write(f'\nA suggested bet on {team_2} would be: ${team_2_bet} for a return of: ${round(team_2_bet * team_2_prob, 2)}')
                    # if the last character is not a newline
                    else:
                    # open the user inputted output file in append mode
                    # use the name write_odds to work with the file
                        with open(write_file, mode='a', encoding='utf-8') as write_odds:
                            write_odds.write(f'\n{team_1} has a {team_1_odds}% implied winning probability.')
                            write_odds.write(f'\n{team_1} has a projected winning probability of {proj_percent_1}%')
                            write_odds.write(f'\n{team_1}\'s Kelly % is: {team_1_kelly}%')
                            write_odds.write(f'\nA suggested bet on {team_1} would be: ${team_1_bet} for a return of: ${round(team_1_bet * team_1_prob, 2)}')
                            write_odds.write(f'\n\n{team_2} has a {team_2_odds}% implied winning probability.')
                            write_odds.write(f'\n{team_2} has a projected winning probability of {proj_percent_2}%')
                            write_odds.write(f'\n{team_2}\'s Kelly % is: {team_2_kelly}%')
                            write_odds.write(f'\nA suggested bet on {team_2} would be: ${team_2_bet} for a return of: ${round(team_2_bet * team_2_prob, 2)}')
                    # inform the user where the username and password have been saved
                    print(f'\nThe file has been saved been saved in \'{write_file}\'')
                except IOError:
                    # if there is an IOError, output the message and exit the function
                    print('\nUh-oh! There has been an error. Let\'s try again.')
            continue
        # case 2:
        #     bet_calculator.bet_calc()
        #     continue
        case 2:
            bet_calculator.exit_program('\nAre you sure you would like to exit? [y/n]\n > ')