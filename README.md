# Bet Calculator

## Description

This is a simple python script that i wrote to help determine which bets are more likely to pay out. using different sources, i try to determine an assumed winning probability for each game. the script takes individual bets (i.e. props, futures, etc.) or a series of games as input.

The script can take odds in either american or decimal form and asks for the assumed winning probability (currently taken from outside sources) and the odds for that event/team and generates a text file with the games which are perceived to be the best value.

## Usage

Run `python3 ./main.py` or create a symlink to main.py somewhere in your PATH to run the script from anywhere (e.g. `sudo ln -s ./main.py /usr/bin/betcalculator`)

## Up Next
- Extra conversion tools
- Cleaner UI
- Implement GUI for application?
- Research and work on developing a model to predict NHL wins
