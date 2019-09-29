def printCard():
    shape = ["heart", "spade", "diamond", "club"]
    numbers = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    for a_shape in shape:
        for a_number in numbers:
            print (a_shape + " " + a_number)
            # add this to a list
            
            # shuffle the list (?)
            
printCard()
#%% shuffle card
from random import shuffle
def printcard():
    card = []
    for a_shape in ["heart", "spade", "diamond", "club"] :
        for a_number in ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            card.append((a_shape,a_number))
    return card

card = printcard()
shuffle(card)
print(card)
