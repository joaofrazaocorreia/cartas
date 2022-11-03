import random
deck1=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deck2=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
hand1=[]
hand2=[]

game=True


def valuefix(deck):

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
        print("Something went wrong. Stealing your credit card info...")

    


def shuffleplayer():
    print("Your deck was shuffled.")
    random.shuffle(deck1)

def showdeck():
    print("Your deck: "+str(deck1))

def showhand():
    if len(hand1) == 0:
        print("You have no cards in your hand!")
    else:
        print("Your hand: "+str(hand1))

def gofish():
    if len(deck1) == 0:
        print("There are no more cards left in your deck.")
    else:
        print("You drew " + str(deck1[-1]) + " and " + str(deck1[-2]) + ".")
        if len(hand1)!=0:
            deck1.append(hand1[-1])
            deck2.append(hand1[-2])
            hand1.remove(deck1[-1])
            hand1.remove(deck1[-2])
        hand1.append(deck1[-1])
        hand1.append(deck1[-2])
        deck1.remove(hand1[-1])
        deck1.remove(hand1[-2])

def compare():
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




def help():
    
    print("--------------------------------------")
    print("'DECK' - shows your deck.")
    print("'HAND' - shows your hand.")
    print("'SHUFFLE' - shuffles your deck.")
    print("'FISH' - draw the last two cards in your deck.")
    print("'HELP' - displays the commands.")
    print("'EXIT' - ends the program.")
    print("'COMPARE' - compares the highest value in both hands.")
    print("--------------------------------------")


while game:
    
    print("--------------------------------------")
    print("Game Start!")

    help()

    shuffleplayer()
    gofish()
    print("Your hand:")
    showhand()

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

    elif command == "COMPARE":

        result=compare()
        
        if result==1:
            print("You won!")
        if result==-1:
            print("You lost!")
        if result==0:
            print("It's a draw!")
        if result==2:
            pass

    elif command == "EXIT":
        break

    else:
        print("Sorry, I didn't get that. Did you write in all caps?")

    print("--------------------------------------")