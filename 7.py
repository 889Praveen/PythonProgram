#to read a card as input and output if the card is lucky or not.
cards=['ace of spade','heart','queen of diamond','king of diamond',7]

card=input("enter any card like:king of spade:").lower()
if(card in cards):
    print("You are lucky!")
elif('heart' in card or '7' in card):
    print("You are lucky!")
else:
    print("better luck next time!")