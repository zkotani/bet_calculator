#!/bin/python

'''
Name:           functions.py
Version:        1.0
Description:    Functions go here.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         https://github.com/zkotani
'''

# Imports

from array import array
import re # Regular expression support
import sys # Exit function
from time import sleep # Sleep function
from typing import Union # Allow multiple types in function paramater

# Functions -- Printing to console

def options_menu():
    ''' display options for the user '''
    print('\nProgram options:')
    print('1. Bets based on games')
    print('2. Individual bets')
    print('3. Quit')

def greeting(
    message_str: str
):
    ''' prints a message bordered with `#` '''
    # Prints greeting strings
    greeting_string = message_str # Welcome string
    greeting_hash = ''
    for char in greeting_string:
        # Creates a string the same number of characters as
        # `greeting_string` made up of `#`
        greeting_hash += '#'
    # Print the greeting to the console
    print(f'\n{greeting_hash}\n{greeting_string}\n{greeting_hash}')

# Functions -- Exit

def exit_program(
    exit_prompt: str
):
    ''' call this function to exit the program '''
    while True:
        # Does the user wish to exit the program?
        exit_str = input(f'{exit_prompt}')
        if re.fullmatch(('y|Y|n|N'), exit):
            break
        # Make sure user is entering `y` or `n`
        print('\nError! Please answer using \'y\' or \'n\'.')
        continue
        # Exit if the user has selected yes
    if re.fullmatch('y|Y', exit_str):
        print('\nThanks for using Bet Calculator!')
        sleep(5)
        print('\nBye~\n')
        sys.exit()

# Functions -- Files

def create_file():
    ''' attempts to open the given filename. if file is not found
        it will be created. all files will have `.txt` appended to the end.'''
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
    with open(write_file, mode='a+', encoding='utf-8') as chk_empty:
        # chk_empty.readlines()
        try:
            # try to read the lines in the file
            chk_empty.readlines()
        except IOError:
            # if the file does not exist, write an empty file
            chk_empty.write('')
    return write_file

def write_to_file(
    write_file: str,
    team_name: str,
    team_info: array,
    new_line: bool
):
    ''' output which is written to saved file '''
    # open the user inputted output file in append mode
    # use the name write_odds to work with the file
    with open(write_file, mode='a', encoding='utf-8') as write_info:
        match new_line:
            case True:
                write_info.write('----------\n')
            case False:
                write_info.write('\n----------\n')
        write_info.write(f'Team: {team_name}\n')
        if team_info[0] > 0:
            write_info.write(f'American odds: +{team_info[0]}\n')
        else:
            write_info.write(f'American odds: {team_info[0]}\n')
        write_info.write(f'Decimal odds: {team_info[1]}\n')
        write_info.write(f'Projected win probability: {team_info[2]}%\n')
        write_info.write(f'Implied win probability: {team_info[3]}%\n')
        write_info.write(f'Kelly: {team_info[4]}%\n')
        write_info.write(f'Bet amount: ${team_info[5]}')

def save_to_file(
    write_file: str,
    team_name: str,
    team_info: array
):
    ''' save the output from the program to the file created earlier '''
    try:
        # open user inputted output file in read mode
        with open(write_file, mode='r', encoding='utf-8') as read_file:
            try:
                # create a list of all lines in the file
                read_lines = list(read_file)
                # copy the last element to variable last_line
                last_line = read_lines[-1]
                # copy the last character in the string to variable last_char
                last_char = list(last_line[-1])
            except IndexError:
                # if the file is empty make last_char a newline
                last_char = '\n'
        # if the last character is a newline or file is empty
        if '\n' in last_char:
            write_to_file(
                write_file,
                team_name,
                team_info,
                True
            )
        # if the last character is not a newline
        else:
            write_to_file(
                write_file,
                team_name,
                team_info,
                False
            )
    except IOError:
        # if there is an IOError, output the message and exit the function
        print('\nError! There has been an error reading or writing the file.')

# Functions -- Math

def calculate_implied_probability(
    odds_type: str,
    team_odds: Union[int, float]
):
    ''' Calculate the implied probability from the given odds '''
    match odds_type:
        case 'AMERICAN':
            if team_odds < 0:
                return round((abs(team_odds) / (abs(team_odds) + 100)) * 100, 2)
            return round((100 / (abs(team_odds) + 100)) * 100, 2)
        case 'DECIMAL':
            return round((1 / team_odds) * 100, 2)

def convert_american(
    team_odds: int
):
    ''' convert american odds to decimal '''
    match team_odds:
        case team_odds if team_odds <= 0:
            return 1 - (100 / team_odds)
        case team_odds if team_odds > 0:
            return (team_odds / 100) + 1

def convert_decimal(
    team_odds: float
):
    ''' convert decimal odds to american '''
    match team_odds:
        case team_odds if team_odds >= 2:
            return round((team_odds - 1) * 100, 2)
        case team_odds if team_odds < 2:
            return round((-100)/(team_odds - 1), 2)

def calculate_kelly(
    odds_type: str,
    team_odds: Union[int, float],
    win_percent: float,
    kelly_multi: float = 0.35
):
    ''' calculate the kelly probability of the bet '''
    if odds_type == 'AMERICAN':
        team_odds = convert_american(team_odds)
    decimal_odds = team_odds - 1
    win_probability = round(win_percent / 100, 2)
    lose_probability = round(1 - win_probability, 2)
    kelly = ((decimal_odds * win_probability) - lose_probability) / decimal_odds
    return round(kelly * (kelly_multi * 100), 2)

# Functions -- Collecting data

def collect_pool():
    ''' Collect total betting pool from the user '''
    # Collect the total betting pool & number of games to bet on
    while True:
        # Ask user for amount in betting pool
        bet_pool = input('\nHow much money is currently in your betting pool?\n> $')
        # Check to make sure the user has entered the betting pool as:
            # > $1000
            # > $1,000
            # > 1000.00
            # > 1,000.00
        if re.fullmatch(r'(\d{1,}(,\d{3})*(\.\d{1,2})?)', bet_pool):
            # If the entered value contains commas, remove them
            split_pool = bet_pool.split(',')
            # Add the split strings back together
            bet_float = ''.join(split_pool)
            try:
                # Try to convert the entered value to a float
                bet_float = float(bet_float)
            except ValueError:
                # If the entered value raises a ValueError, let the user know
                print('\nError! Please make sure you\'re entering a valid number.')
                continue
        else:
            print\
                ('\nError! Make sure you\'re entering your value in one of the following formats: \
                    \n1. 1000\n2. 1,000\n3. 1000.00\n4. 1,000.00')
            continue
        # Make sure user is entering a value greater than 0
        if bet_float <= 0:
            # Call exit_program()
            exit_program('\nYou can\'t bet with $0 or less! Exit? [y/n]\n> ')
            continue
        break
    return bet_float

def number_of_bets(
    games_or_bets: str
):
    ''' Collects number of bets that will be placed '''
    # Ask the user how many bets will be placed.
    match games_or_bets:
        case 'games':
            games_str = 'games'
        case 'indiv':
            games_str = 'bets'
    while True:
        try:
            num_bets = int(input(f'\nHow many {games_str} are being played?\n> '))
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

def get_team_name(
    j: int,
    bets_dict: dict
):
    ''' ask user for the name of the teams being bet on '''
    while True:
        match j:
            case 0:
                team_num = 'first'
            case 1:
                team_num = 'second'
        team_name = input(f'\nEnter the name of the {team_num} team.\n> ').upper()
        if check_name(bets_dict, team_name):
            continue
        while True:
            team_name_ok = input(f'\nTeam #{j + 1}: {team_name}? [y/n]\n> ')
            if re.fullmatch('(y|Y|n|N)', team_name_ok):
                break
            print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
            continue
        if re.fullmatch('(n|N)', team_name_ok):
            continue
        break
    return team_name

def check_name(
    bets_dict: dict,
    check_title: str
):
    ''' checks to see if team name/bet title is already in use '''
    # Check to see if the name has already been used
    if check_title in bets_dict:
    # Dictionary keys need to be distinct, tell the user to try a different name
        print('\nError! You\'re already using this name. Try something different.')
        return True
    # Move to next section if the name is fine
    return False

def get_team_odds(
    team_name: str
):
    ''' collect team odds in american or decimal format '''
    while True:
        odds_type = input\
            ('\nAre you using American or Decimal odds?\n> ').upper()
        if re.fullmatch(r'AMERICAN|DECIMAL', odds_type):
            match odds_type:
                case 'AMERICAN':
                    team_odds = input(f'\nEnter {team_name}\'s odds [American]\n> ')
                    if re.fullmatch(r'(-|\+)\d{3}', team_odds):
                        try:
                            team_odds = int(team_odds)
                        except ValueError:
                            print('\nError! Make sure you\'re\
                                entering a valid number!')
                            continue
                        break
                    print('\nError! Odds must be in American format.')
                    continue
                case 'DECIMAL':
                    team_odds = input(f'\nEnter {team_name}\'s odds [Decimal].\n> ')
                    if re.fullmatch\
                        (r'(\d{0,3}\.\d{1,}?)(\d*(\.\d{1,})?)', team_odds):
                        try:
                            team_odds = float(team_odds)
                        except ValueError:
                            print('\nError! Make sure you\'re\
                                entering a valid number!')
                            continue
                        break
                    print('\nError! Odds must be in Decimal format.')
                    continue
        print('\nError! Make sure you\'re entering `American` or `Decimal`.')
        continue
    return team_odds, odds_type

def projected_win_percent(
    team_name: str
):
    ''' collect projected in percent from user '''
    while True:
        win_percent = input(f'Enter {team_name}\'s winning percent.\n> %')
        if re.fullmatch(r'(\d*(\.\d{1,})?)', win_percent):
        # Make sure the number entered can be used as a float
            try:
                win_percent = float(win_percent)
            # If a ValueError is raised, let the user know
            except ValueError:
                print('\nError! Make sure you\'re entering a valid number!')
                continue
            # If the input doesn't match the pattern, tell the user what to enter
        else:
            print('\nError! Make sure you\'re entering a number between 0-100.')
            continue
        # Make sure input is more than 0
        match win_percent:
            case win_percent if win_percent <= 0:
                print('\nError! Win percentage can\'t be 0% or less.\n> ')
                continue
            # Make sure input is not over 100
            case win_percent if win_percent > 100:
                print('\nError! Win percentage can\'t be over 100%\n> ')
                continue
        break
    return win_percent

def bet_info(
    total_bets: int,
    bet_float: float,
    games_or_bets: str
):
    ''' collect info on bets to be placed '''
    bets_dict = {}
    for i in range(total_bets):
        match games_or_bets:
            case 'games':
                greeting(f'# GAME #{i + 1} #')
                for j in range(2):
                    team_name = get_team_name(j, bets_dict)
                    team_odds, odds_type = get_team_odds(team_name)
                    win_percent = projected_win_percent(team_name)
                    implied_probability = calculate_implied_probability(odds_type, team_odds)
                    kelly = calculate_kelly(odds_type, team_odds, win_percent)
                    bet_amount = round((kelly / bet_float) * 100, 2)
                    match odds_type:
                        case 'AMERICAN':
                            american_odds = team_odds
                            decimal_odds = convert_american(team_odds)
                        case 'DECIMAL':
                            american_odds = convert_decimal(team_odds)
                            decimal_odds = team_odds
                    if kelly > 0:
                        bets_dict[team_name] = [
                            american_odds,
                            decimal_odds,
                            win_percent,
                            implied_probability,
                            kelly,
                            bet_amount
                        ]
            case 'bets':
                pass
    return bets_dict

# # Loop for the total number of bets to be placed
# while True:
#     # Ask user for the team name/title for the bet at current index
#     bet_title = input(f'\nEnter the name of the team or title of bet #{i + 1}.\n> ')
#     # Check to see if the name has already been used
#     if bet_title in all_bets:
#         # Dictionary keys need to be distinct, tell the user to try a different name
#         print('\nError! You\'re already using this name. Try something different.')
#         continue
#     while True:
#         # Confirm the name of the bet
#         title_ok = input(f'\nBet title: {bet_title}? [y/n]\n> ')
#         if re.fullmatch('(y|Y|n|N)', title_ok):
#             break
#         # Make sure the user is entering `y` or `n`
#         print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
#         continue
#     # If the user doesn't like the name, have them start this section over
#     if re.fullmatch('(n|N)', title_ok):
#         continue
#     # Move to next section if the name is fine
#     break
# while True:
#     # Ask user what % of their pool is going toward the bet they've just named
#     bet_percent = input(f'\nWhat percentage of your pool is going towards Bet #{i + 1}: {bet_title}?\n> %')
#     # Make sure the input is in the format:
#         # 100
#         # 100.00
#         # 100.0
#         # .1
#         # .01
#         # etc.
#     if re.fullmatch('(\d*(\.\d{1,})?)', bet_percent):
#         # Make sure the number entered can be used as a float
#         try:
#             float_percent = float(bet_percent)
#         # If a ValueError is raised, let the user know
#         except ValueError:
#             print('\nError! Make sure you\'re entering a valid number!')
#             continue
#     # If the input doesn't match the pattern, tell the user what to enter
#     else:
#         print('\nError! Make sure you\'re entering a number between 0-100.')
#         continue
#     # Make sure input is more than 0
#     if float_percent <= 0:
#         exit_program('\nError! Can\'t bet 0% or less. Exit? [y/n]\n> ')
#         continue
#     # Make sure input is not over 100
#     elif float_percent > 100:
#         exit_program('\nError! Can\'t bet over 100% Exit? [y/n]\n> ')
#         continue
#     # Confirm the user`s input
#     confirm_bet = input(f'\nYou would like to bet {float_percent}% of your pool on {bet_title}? [y/n]\n> ')
#     if re.fullmatch('(y|Y|n|N)', confirm_bet):
#         # If the user isn`t happy with their choice, restart this section
#         if re.fullmatch('(n|N)', confirm_bet):
#             continue
#         # Move to next section if they`re happy with their input
#         else:
#             break
#     # Make sure the user enters `y` or `n`
#     else:
#         print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
#         continue
# # Add an entry to the all_bets dictionary
#     # Key: name of team/bet
#     # Value: bet percent
# all_bets[bet_title] = (float_percent / 100)
# return all_bets
