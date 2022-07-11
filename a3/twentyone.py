#Jonathan 110161272


import random

#Logic of the game
def main():
    gameRound = 1       #the round of the game
    score = 100         #user's starting score
    while gameRound <= 5:       #game ends when round 5 is finished
        cardList = []
        cardList.append(dealCard())     #generates first hand
        cardList.append(dealCard())     #generates second hand
        print(f"\
\n\
\n\
Round {gameRound}\n\
Score: {score}")        #displays the round of the game and the user's score
        userInput = "hit"
        userBust = 1
        while userBust !=0:
            print(f"Your hand: {displayHand(cardList)}  ({sumHand(cardList)})")     #displays the cards and the sum of the cards
            if sumHand(cardList) > 21:          #goes to another round if the sum of the hands is over 21
                print("Bust!")
                score -= 21         #substract 21 points from the user's score
                gameRound += 1
                userBust = 0
                break            
            
            while True:         #if the sum is still below 21, user gets to choose to draw a new card or stop here and go to the next round
                userInput = input("Would you like to 'hit' or 'stand': ")
                
                if userInput == 'hit':
                    cardList.append(dealCard())     #if the user choose to 'hit', a randomly generated card is handed
                    break 
                elif userInput == 'stand':          #if the user choose to 'stand', the round stops here and move onto the next round
                    score -= 21 - sumHand(cardList)     #substract the sum of the hands from the user's score
                    gameRound +=1       
                    userBust=0
                    break
                    
    print(f"\
\n\
\n\
Your final score: {score},  Your rank: {getRank(score)}")       #prints user's final score, and the user's rank


#randomly generates a number between 1 and 13
def dealCard():
    cards = random.randint(1,13)
    return cards

#calculates the sum of the cards
def sumHand(cardList):
    i=0
    userSum=0
    for i in range(0,len(cardList)):
        if cardList[i] > 10:        #so that the cards J, K, Q have the value of 10
            cardList[i] = 10
        userSum += cardList[i]
    for x in cardList:
        if x == 1 and userSum <= 21:    #if the user's sum is below 21, then the card Ace has the value of 11
            userSum +=10
            if userSum > 21:            #if the user's sum is over 21, then the card Ace has the value of 1
                userSum -= 10

    return userSum

#to display the card's face
def displayHand(cardList):
    i=0
    cardLogo = ""
    for i in range(0,len(cardList)):    #assigns the number for 1-13 to its corresponding faces
        if cardList[i] == 11:
            cardLogo += "J "
        elif cardList[i] == 12:
            cardLogo += "Q "
        elif cardList[i] == 13:
            cardLogo += "K "
        elif cardList[i] == 1:
            cardLogo += "A "
        else:
            cardLogo += (str(cardList[i]) + " ")
    return cardLogo

#displays the user's rank depending on the user's final score
def getRank(score):
    if -5<= score <= 24:
        return "Noob"
    elif 25<= score <= 49:
        return "Commoner"
    elif 50<= score <= 74:
        return "Jack"
    elif 75<= score <= 84:
        return "Queen"
    elif 85<= score <= 94:
        return "King"
    else:
        return "Ace!"


main()