#-------------------------------------------------------------------------------
# Name:        rock.py
# Purpose:     Rock, paper, scissors game
#
# Author:      Sandro Ricardo De Souza
#
# Created:     01/08/2025
# Copyright:   (c) sandr 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

import random

random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

user_choice = input('rock, paper or scissors? ')
print('You chose', user_choice, 'and the computer chose', computer_choice)