# Program to simulate dice rolling and plotting the simulated rolls in a table and its Stats


import random, statistics
from tabulate import tabulate

a = int(input('Enter number of times to roll the Die : '))
l1 = []
l3 = []
h = ['S.No.','Value'] # Header For table

for i in range(1,a+1):
    l2 = []                       # List to Store Values for table
    b = random.randint(1,6)
    l3.append(b)
    l2.append(i)
    l2.append(b)
    l1.append(l2)


print(tabulate(l1,headers=h,tablefmt = 'grid'))               # Creates A table
for i in range(1,7):                                          # Shows Occurance of all values of Dice Roll
    print('Number of times',i,'Occurs is',l3.count(i))
print('Mean of Values Of Dice Rolls is',statistics.mean(l3))




