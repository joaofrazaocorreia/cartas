import random
deck1=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deck2=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
hand=[]

game=True

def shuffleplayer():
    print("Your deck was shuffled.")
    random.shuffle(deck1)

def shufflecomp():
    print("The opponent's deck was suffled.")
    random.shuffle(deck2)

def shuffleboth():
    print("Both decks were shuffled.")
    random.shuffle(deck1)
    random.shuffle(deck2)

def showdeck():
    print("Your deck: "+str(deck1))

def showhand():
    if len(hand) == 0:
        print("You have no cards in your hand!")
    else:
        print("Your hand: "+str(hand))

def gofish():
    if len(deck1) == 0:
        print("There are no more cards left in your deck.")
    else:
        print("You drew " + str(deck1[-1]) + " and " + str(deck1[-2]) + ".")
        hand.append(deck1[-1])
        hand.append(deck1[-2])
        deck1.remove(hand[-1])
        deck1.remove(hand[-2])

def help():
    
    print("--------------------------------------")
    print("'DECK' - shows your deck.")
    print("'HAND' - shows your hand.")
    print("'SHUFFLE' - shuffles your deck.")
    print("'FISH' - draw the last two cards in your deck.")
    print("'HELP' - displays the commands.")
    print("'EXIT' - ends the program.")
    print("--------------------------------------")



help()
while game:
    
    print("What do you want to do now?")
    command=input("Your input: ")

    print("--------------------------------------")
    if command == "DECK":
        showdeck()

    elif command == "HAND":
        showhand()
    
    elif command == "SHUFFLE":
        shuffleplayer()

    elif command == "FISH":
        gofish()

    elif command == "EXIT":
        break

    else:
        print("Sorry, I didn't get that. Did you write in all caps?")

    print("--------------------------------------")