# Program Simulating one or more dice thrown 


import random
from tabulate import tabulate

a = int(input('Enter number of times to roll the Die : '))
b = int(input('Enter how many Dice to roll per turn : '))

l1 = []
l3 = []
h = ['S.No.']                   # Header For table

for i in range(0,a):
    val = ['value',i+1]
    h.append(val)
    l2 = []
    l2.append(i)
    for j in range(0,b):                   
        rand = random.randint(1,6)
        l3.append(rand)
        l2.append(rand)
    l1.append(l2)


print(tabulate(l1,headers=h,tablefmt = 'grid'))               # Creates A table


