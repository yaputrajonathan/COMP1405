#simulates a thief trying to pick a lock

import random

#start the door as locked
doorLocked = True

#ask user if they want to pick the lock
userChoice = input("Do you want to pick the door? (y/n): ")


#until the door opens
while doorLocked and userChoice == "y":


    #try to unlock it
    if random.randint(1,100)<=25:
        print("The door unlocks.")
        doorLocked = False
    elif random.randint(1,100)<=10:       #10% chance of getting caught by security
        print("Security arrives and you are caught")
        userChoice = "n"
    #else, try again
    else:
        print("The lock tumbles but stays locked.")

        #ask the user if they want to try again
        userChoice = input("Do you want to try again? (y/n): ")


print("The end.")