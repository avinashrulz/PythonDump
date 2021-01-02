#Author: Avinash Kumar

import random, sys

win = 0
tie = 0
loss = 0

#print("ROCK, PAPER, SCISSORS", end = ' Hua hua')
print("ROCK, PAPER, SCISSORS")
while True:
    print ("%s Wins, %s Losses, %s Ties" %(win, loss, tie))
    while True:
        #sys.exit()
        print("Enter your move: (r)ock (p)aper (s)cissor or (q)uit")
        userChoice = input()
        if userChoice == 'q':
            sys.exit()
        elif userChoice == 'r' or userChoice == 'p' or userChoice == 's':
            break

    computerChance = random.randint(1,3)
    