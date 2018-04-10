#Creation task game
import time
import random
playGame=input("Hello! Welcome to Alec Libs free trial version."
      "In this trial version you will only have 3 stories to have fun with."
      "The only way to unlock more stories is to either pay $5.99 or complete a story in less than 10 seconds."
      "So.. wanna play?: ") 

def birthday(holiday, name):
        print("happy", holiday, "to", name)

while playGame != "no" and playGame != "yes":
    print("Invalid command print yes or no")
    playGame = input()
if playGame != "yes":
    print("That sucks :( Come back soon!")
else:
    print("Enjoy the game!")
    name1=input("Type a name: ")
    holiday1=input("Type a holiday: ")
    verb1=input("Type a verb: ")
    animal1=input("Type an animal: ")
    adj1=input("Type an adjective: ") 

    for _ in range(2):
        birthday(holiday1, name1)
    print("You", verb1,  "like a", animal1)
    print("And", verb1, "like one too!") 
          
