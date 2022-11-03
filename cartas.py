import random
deck1=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deck2=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

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

def gofish():
    print("The last two cards on your deck are: " + str(deck1[-1]) + " and " + str(deck1[-2]) + ".")


while game:
    
    print("What do you want to do now?")
    print("--------------------------------------")
    print("'SHOW' - shows your deck.")
    print("'SHUFFLE' - shuffles your deck.")
    print("'FISH' - fetch the last two cards in your deck.")
    print("--------------------------------------")
    command=input("Your input: ")

    if command == "SHOW":
        showdeck()
    
    elif command == "SHUFFLE":
        shuffleplayer()

    elif command == "FISH":
        gofish()

    else:
        print("Sorry, I didn't get that. Did you write in all caps?")

    input("(Press Enter)")
    print("--------------------------------------")