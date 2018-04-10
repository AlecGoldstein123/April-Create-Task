# Count the number of Heads

import random

# Traching the number of simulators
'''
simNum=0
flip = random.randint(0,1)
countHeads=0

while simNum<10:
    if flip==1:
        print("Head - ", end="")
        countHeads= countHeads+flip
        print(countHeads)
    print(flip)
    flip=random.randint(0,1)
    simNum= simNum+1
'''
# If count Heads is less than five

'''
simNum=0
flip = random.randint(0,1)
countHeads=0

while simNum<10:
    if flip==1:
        print("Head - ", end="")
        countHeads= countHeads+flip
        print(countHeads)
    print(flip)
    flip=random.randint(0,1)
    simNum= simNum+1
    if countHeads== 5:
            break
            '''

# Other way to do it
'''
simNum=0
countHeads=0
flip=random.randint(0,1)

while countHeads<5:
    flip= random.randint(0,1)
    if flip ==1:
        countHeads=countHeads+flip
    print(flip)
    print("Heads =", countHeads)
    simNum=simNum+1

print("Total flips: ",simNum)
        '''

# Count to 1,000 heads
'''
simNum=0
countHeads=0
flip=random.randint(0,1)

while countHeads<1000:
    flip= random.randint(0,1)
    if flip ==1:
        countHeads=countHeads+flip
    print(flip)
    print("Heads =", countHeads)
    simNum=simNum+1

print("Total flips: ",simNum)

'''

# Streaks of Heads

simNum= 0 #Track # of simulations
countHeads=0 #Tracks how many flips were heads

while simNum<10:
    flip = random.randint(0,1)
    if flip==1:
        countHeads = countHeads+1
    else:
        countHeads=0
    print(flip)
    print("Heads Streak -", simNum)
    simNum = simNum+1
    
print("Total flips: ", simNum)
# How many flips do you need to get 12 streaks in a row
