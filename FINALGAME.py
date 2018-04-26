import random
print("""You have stolen a car to go on the high speed thrill of your life.
The police want to catch you and chasing you down! Survive the pursuit and keep the car.""")
print()

#variables
milesTraveled = 0
thirst = 0
carHeat = 0
policeTraveled = -20
soda = 3
done = False
gasStation = 0


#start main loop
while not done:
    policeBehind = milesTraveled - policeTraveled
    fullSpeed = random.randrange(10, 21)
    moderateSpeed = random.randrange(5, 13)
    print("""
    A. Drink some soda.
    B. Ahead at moderate speed.
    C. Ahead full speed.
    D. Stop to eat some chips.
    E. Status check
    Q. Quit.""")
    print()
    userInput = input("Your choice? ")
    if userInput.lower() == "q":
            done = True

#status
    elif userInput.lower() == "e":
        print("Miles traveled: ",milesTraveled)
        print("Soda remaining: ",soda)
        print("Your car has ",carHeat,"overheating problems.")
        print("The police are ",policeBehind,"miles behind you.")
#stop for night
    elif userInput.lower() == "d":
        carHeat *= 0
        print("Your car is cool and running fine and now has the heating problems: ",carHeat)
        policeTraveled += random.randrange(7, 15)
#move full speed
    elif userInput.lower() == "c":
        print("You traveled ",fullSpeed,"miles!")
        milesTraveled += fullSpeed
        thirst += 1
        carHeat += random.randrange(1, 4)
        policeTraveled += random.randrange(7, 15)
        gasStation = random.randrange 
        (1, 21)

#move moderate speed
    elif userInput.lower() == "b":
        print("You traveled ",moderateSpeed,"miles!")
        milesTraveled += moderateSpeed
        thirst += 1
        carHeat += 1
        policeTraveled += random.randrange(7, 15)
        gasStation = random.randrange(1, 21)

        #drink soda
    elif userInput.lower() == "a":
        if soda == 0:
            print("You're out of water.")
        else:
            soda -= 1
            thirst *= 0
            print("You have ",soda,"drinks left and you are no longer thirsty.")

#not done check
    if gasStation == 20:
        carHeat *= 0
        thirst *= 0
        soda = 3
        print("You found a gas station! After stealing a drink you filled your soda and the car is cooled down.")
    if policeBehind <= 15:
        print("The police are drawing near!")
    if milesTraveled >= 200 and not done:
        print("You escaped the cops, you win!")
        done = True
    if policeTraveled >= milesTraveled:
        print("The police caught and arrested you..")
        print("You're busted!")
        done = True
    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")
    if thirst > 6:
        print("You died of dehydration!")
        done = True
    if carHeat > 5 and carHeat <= 8 and not done:
        print("Your car is overheating.")
    if carHeat > 8:
        print("You car broke down and now you're in jail.")
        done = True
