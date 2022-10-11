#!/bin/python

'''
Name:           odds_calculator.py
Version:        0.9
Description:    Determine the implied probability based on betting odds.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         http://github.com/zkotani
'''

import re # Regular expression support

def implied_probability(odds_1: str, odds_2: str, float_percent_1: float, float_percent_2: float):
    int_odds_1 = int(odds_1[1:])
    int_odds_2 = int(odds_2[1:])
    match odds_1[0]:
        case '-':
            team_1_prob = 1 - (100 / -(int(odds_1[1:])))
            impl_prob_1 = (int_odds_1 / (100 + int_odds_1))
        case '+':
            team_1_prob = (int(odds_1[1:]) / 100) + 1
            impl_prob_1 = (100 / (int_odds_1 + 100))
    match odds_2[0]:
        case '-':
            team_2_prob = 1 - (100 / -(int(odds_2[1:])))
            impl_prob_2 = (int_odds_2 / (100 + int_odds_2))
        case '+':
            team_2_prob = (int(odds_2[1:]) / 100) + 1
            impl_prob_2 = (100 / (int_odds_2 + 100))
    team_1_kelly = ((team_1_prob * (float_percent_1 / 100)) - (0.35 - (float_percent_1 / 100)) / team_2_prob) #* 0.35
    team_2_kelly = ((team_1_prob * (float_percent_2 / 100)) - (0.35 - (float_percent_2 / 100)) / team_2_prob) #* 0.35
    return round(impl_prob_1, 2), round(impl_prob_2, 2), round(team_1_kelly, 2), round(team_2_kelly, 2), team_1_prob, team_2_prob


def team_input():
    while True:
        team_1 = input('\nEnter the name of the first team.\n> ')
        while True:
            team_1_ok = input(f'\nTeam #1: {team_1}? [y/n]\n> ')
            if re.fullmatch('(y|Y|n|N)', team_1_ok):
                break
            else:
                print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
                continue
        if re.fullmatch('(n|N)', team_1_ok):
            continue
        else:
            break
    while True:
        odds_1 = input(f'\nEnter {team_1}\'s odds [American]: ')
        if re.fullmatch('(-|\+)\d{3}', odds_1):
            try:
                int(odds_1[1:])
            except ValueError:
                print('\nError! Make sure you\'re entering a valid number!')
                continue
            break
        else:
            print('\nError! Odds must be in American format [-/+100].')
            continue
    while True:
        win_percent_1 = input(f'Enter {team_1}\'s winning percent.\n> %')
        if re.fullmatch('(\d*(\.\d{1,})?)', win_percent_1):
        # Make sure the number entered can be used as a float
            try:
                float_percent_1 = float(win_percent_1)
            # If a ValueError is raised, let the user know
            except ValueError:
                print('\nError! Make sure you\'re entering a valid number!')
                continue
            # If the input doesn't match the pattern, tell the user what to enter
        else:
            print('\nError! Make sure you\'re entering a number between 0-100.')
            continue
            # Make sure input is more than 0
        if float_percent_1 <= 0:
            print('\nError! Win percentage can\'t be 0% or less.\n> ')
            continue
        # Make sure input is not over 100
        elif float_percent_1 > 100:
            print('\nError! Win percentage can\'t be over 100%\n> ')
            print
        break
    while True:
        team_2 = input('\nEnter the name of the second team.\n> ')
        while True:
            team_2_ok = input(f'\nTeam #1: {team_2}? [y/n]\n> ')
            if re.fullmatch('(y|Y|n|N)', team_2_ok):
                break
            else:
                print('\nError! Make sure you\'re entering \'y\' or \'n\'.')
                continue
        if re.fullmatch('(n|N)', team_2_ok):
            continue
        else:
            break
    while True:
        odds_2 = input(f'\nEnter {team_2}\'s odds [American]: ')
        if re.fullmatch('(-|\+)\d{3}', odds_2):
            try:
                int(odds_1[1:])
            except ValueError:
                print('\nError! Make sure you\'re entering a valid number!')
                continue
            break
        else:
            print('\nError! Odds must be in American format [-/+100].')
            continue
    while True:
        win_percent_2 = input(f'Enter {team_2}\'s winning percent.\n> %')
        if re.fullmatch('(\d*(\.\d{1,})?)', win_percent_2):
        # Make sure the number entered can be used as a float
            try:
                float_percent_2 = float(win_percent_2)
            # If a ValueError is raised, let the user know
            except ValueError:
                print('\nError! Make sure you\'re entering a valid number!')
                continue
            # If the input doesn't match the pattern, tell the user what to enter
        else:
            print('\nError! Make sure you\'re entering a number between 0-100.')
            continue
            # Make sure input is more than 0
        if float_percent_2 <= 0:
            print('\nError! Win percentage can\'t be 0% or less.\n> ')
            continue
        # Make sure input is not over 100
        elif float_percent_2 > 100:
            print('\nError! Win percentage can\'t be over 100%\n> ')
            print
        break
    return team_1, team_2, odds_1, odds_2, float_percent_1, float_percent_2

def odds_calc():
    team_1, team_2, odds_1, odds_2, float_percent_1, float_percent_2 = team_input()
    team_1_odds, team_2_odds, team_1_kelly, team_2_kelly, \
        team_1_prob, team_2_prob = implied_probability(odds_1, odds_2, float_percent_1, float_percent_2)
    return team_1, (team_1_odds * 100), team_1_kelly, team_2, (team_2_odds * 100), team_2_kelly, float_percent_1, float_percent_2, \
        team_1_prob, team_2_prob