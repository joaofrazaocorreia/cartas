import random
deck1=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deck2=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
hand1=[]
hand2=[]

game=True

def valuefix(deck): # Converts Letters into values, and reverts the process when called again.

    if "J" in deck or "Q" in deck or "K" in deck or "A" in deck:
        if "J" in deck:
            deck.remove("J")
            deck.append(11)
        if "Q" in deck:
            deck.remove("Q")
            deck.append(12)
        if "K" in deck:
            deck.remove("K")
            deck.append(13)
        if "A" in deck:
            deck.remove("A")
            deck.append(14)
    elif 11 in deck or 12 in deck or 13 in deck or 14 in deck:
        if 11 in deck:
            deck.remove(11)
            deck.append("J")
        if 12 in deck:
            deck.remove(12)
            deck.append("Q")
        if 13 in deck:
            deck.remove(13)
            deck.append("K")
        if 14 in deck:
            deck.remove(14)
            deck.append("A")
    else:
        pass

def discard(x): #Discards x cards
        
    while x!=0:
        x=x-1
        hand1.append(deck1[-2])
        deck1.remove(hand1[-1])
        deck1.append(hand1[0])
        hand1.remove(deck1[-1])

    if x==0:
        pass


def shuffleplayer():  #Shuffles the player's deck
    random.shuffle(deck1)

def showhand(): #Shows the player's hand if they have any
    if len(hand1) == 0:
        print("You have no cards in your hand!")
    else:
        print("Your hand: "+str(hand1))

def gofish(): #Player draws the 2 cards from the bottom of their deck
    if len(deck1) == 0:
        print("There are no more cards left in your deck.")
    else:
        print("You drew " + str(deck1[-1]) + " and " + str(deck1[-2]) + ".")
        if len(hand1)!=0:
            deck1.append(hand1[-1])
            deck1.append(hand1[-2])
            hand1.remove(deck1[-1])
            hand1.remove(deck1[-2])
        hand1.append(deck1[-1])
        hand1.append(deck1[-2])
        deck1.remove(hand1[-1])
        deck1.remove(hand1[-2])

def compare(): #Sums the card values from each hand and returns a value depending on which is higher
    if len(hand1)==0:
        print("You have no cards in your hand!")
        return 2
    else:
        temp=random.sample(deck2, 2)
        hand2.append(temp[-1])
        hand2.append(temp[-2])
        deck2.remove(temp[-1])
        deck2.remove(temp[-2])

        valuefix(hand1)
        valuefix(hand2)

        compvalue=int(hand2[-1])+int(hand2[-2])
        playervalue=int(hand1[-1])+int(hand1[-2])

        valuefix(hand1)
        valuefix(hand2)

        print("Your hand: "+str(hand1))
        print("Their hand: "+str(hand2))

        if playervalue > compvalue:
            return 1
        elif playervalue < compvalue:
            return -1
        elif playervalue == compvalue:
            return 0

while game: #GAME LOOP
    
    print("--------------------------------------")
    print("Game Start!")
    print("--------------------------------------")
    shuffleplayer()
    gofish()
    showhand()

    command=input("How many cards do you want to discard? (0, 1 ,2): ")
    print("--------------------------------------")

    if not command.isdigit:
        print("Please insert numbers only.")

    else:
        command=int(command)

    if command > 2 or command < 0:
        print("Please only insert values between 0 and 2.")
    
    else:
        discard(command)
        print("You discarded "+str(command)+" time(s). Your current hand is:")
        showhand()
        print("")

    result=compare()

    if result==1:
        print("You won!")
    if result==-1:
        print("You lost!")
    if result==0:
        print("It's a draw!")
    if result==2:
        pass

    print("Would you like to play again? YES / NO")
    command=input()

    if command == "YES":
        game = True
        print("--------------------------------------")
        if len(hand1)!=0:
            deck1.append(hand1[-1])       # This part of the code resets both hands
            deck1.append(hand1[-2])
            hand1.remove(deck1[-1])
            hand1.remove(deck1[-2])
        if len(hand2)!=0:
            deck2.append(hand2[-1])      # sorry for being too long
            deck2.append(hand2[-2])
            hand2.remove(deck2[-1])
            hand2.remove(deck2[-2])   # kinda only realized my mistake after i was done
    elif command == "NO":
        game = False
        print("Ending the game...")  # don't kill me please
    else:
        print("I didn't understand '"+str(command)+"'. Ending the game...")
        game = False