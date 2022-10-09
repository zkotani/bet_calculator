#!/bin/python

'''
Name:           odds_calculator.py
Version:        0.1
Description:    Determine the implied probability based on betting odds.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         http://github.com/zkotani
'''

import re # Regular expression support

def implied_probability(team_1: str, team_2: str, odds_1: str, odds_2: str):
    if odds_1[0] == '-':
        favourite = int(odds_1[1:])
        underdog = int(odds_2[1:])
        favourite_prob = (favourite/(favourite+100)) * 100
        underdog_prob = (100/(underdog+100)) * 100
        return round(favourite_prob, 2), round(underdog_prob, 2)
    else:
        favourite = int(odds_2[1:])
        underdog = int(odds_1[1:])
        favourite_prob = (favourite/(favourite+100)) * 100
        underdog_prob = (100/(underdog+100)) * 100
        return round(underdog_prob, 2), round(favourite_prob, 2)


def team_input():
    while True:
        team_1 = input('\nEnter the name of the first team: ')
        while True:
            team_1_ok = input(f'\nTeam #1:{team_1}? [y/n]')
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
        team_2 = input('\nEnter the name of the second team: ')
        while True:
            team_2_ok = input(f'\nTeam #1:{team_2}? [y/n]')
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
                int(odds_2[1:])
            except ValueError:
                print('\nError! Make sure you\'re entering a valid number!')
                continue
            break
        else:
            print('\nError! Odds must be in American format [-/+100].')
            continue
    return team_1, team_2, odds_1, odds_2

def odds_calc():
    team_1, team_2, odds_1, odds_2 = team_input()
    team_1_odds, team_2_odds = implied_probability(team_1, team_2, odds_1, odds_2)
    print(f'\n{team_1} has a {team_1_odds}% implied winning probability.')
    print(f'\n{team_2} has a {team_2_odds}% implied winning probability.')