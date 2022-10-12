#!/bin/python

'''
Name:           bet_calculator.py
Version:        1.1
Description:    Simple python script used to automate sports betting.
                    Calculates amount for individual bets based on percentages of a main pool.
Developer:      Zyphlen Kotani [zkotani@gmail.com]
Github:         http://github.com/zkotani
'''



# def bet_math(total_pool: float, all_bets: dict):
#     calculated_bets = {} # Empty dictionary to be poplulated procedurally
#     # Iterate through the keys & values in all_bets
#     for k, v in all_bets.items():
#         # Calculate the amount to bet based on total_pool * bet_percent
#         bet_amount = v * total_pool
#         # Add entry to new dictionary
#             # Key: name of team/bet
#             # Value: array containing bet percent and bet amount
#         calculated_bets[k] = [str(v), str(bet_amount)]
#     return calculated_bets

# def output(calculated_bets: dict):
#     for k, v in calculated_bets.items():
#         percent_total = float(v[0]) * 100
#         print(f'\nBet {percent_total}% on {k} for a total of: ${round(float(v[1]), 2)}.')

# def bet_calc():
#     greeting()
#     total_pool = collect_pool()
#     total_bets = number_of_bets()
#     all_bets = bet_info(total_bets)
#     calculated_bets = bet_math(total_pool, all_bets)
#     output(calculated_bets)
