# Game of Rock Paper Scissors

import random

c = ['r','p','s']      # Values For random fucntion to pick from
C = {'r':'rock','p':'paper','s':'scissors'}
print('Rock = r','Paper = p','Scissors = s',sep ='\n')


def f1():
    a = input('Enter Your Choice : ')
    b = random.choice(c)                          # Chooses a random value for list c
    l1 = [C[a],C[b]]                              # Converts input variables into readable form via dict C
    if a == b:
        print(l1,'Its A Tie')
        f1()
    elif a == 'r' and b == 'p':
        print(l1,'You Lose')
        f1()
    elif a == 'p' and b == 'r':
        print(l1,'You Win')
    elif a == 'p'and b == 's':
        print(l1,'You Lose')
        f1()
    elif a == 's' and b == 'p':
        print(l1,'You Win')
    elif a == 's' and b == 'r':
        print(l1,'You Lose')
        f1()
    elif a == 'r' and b == 's':
        print(l1,'You Win')
f1()