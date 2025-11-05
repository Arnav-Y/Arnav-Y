# This is number guessing game where the user inputs the limits of the number to guess the number


import random

glu = int(input('Enter the upper value for the guess limit : '))   # Taking the upper limit from the User
gll = int(input('Enter the lower value for the guess limit : '))   # Taking the lower limit from the User

num = random.randint(gll,glu)  # Using 'random' to make the number to guess from the limits


def f1():                                                
    a = int(input('Enter your guess :'))           # Terminating condition for the recursion used to help user guess
    if a == num:
        print('You guessed correctly')
    elif a <num:     
        print('the number is lower than guess')
        f1()
    else:
        print('the number is higher than guess')
        f1()
f1()