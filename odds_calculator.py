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
    team_1_kelly = ((((team_1_prob - 1) * (float_percent_1 / 100) - (1 - (float_percent_1 / 100))) / (team_1_prob - 1)) * 100) * 0.35
    team_2_kelly = ((((team_2_prob - 1) * (float_percent_2 / 100) - (1 - (float_percent_2 / 100))) / (team_2_prob - 1)) * 100) * 0.35
    return impl_prob_1, impl_prob_2, team_1_kelly, team_2_kelly, team_1_prob, team_2_prob

def odds_calc():
    team_1, team_2, odds_1, odds_2, float_percent_1, float_percent_2 = team_input()
    team_1_odds, team_2_odds, team_1_kelly, team_2_kelly, \
        team_1_prob, team_2_prob = implied_probability(odds_1, odds_2, float_percent_1, float_percent_2)
    return team_1, (team_1_odds * 100), team_1_kelly, team_2, (team_2_odds * 100), team_2_kelly, float_percent_1, float_percent_2, \
        team_1_prob, team_2_prob