# Flip a coin 10 time

import random

# Track the number of simulations
# 1 = head 0 = tails

simNum = 0
flip = random.randint(0,1)

while simNum<10:
    print(flip)
    flip = random.randint(0,1)
    if flip == 0:
        print('tails')
    elif flip == 1:
        print('head')
    simNum = simNum+1
    
print("10 tries done") 
