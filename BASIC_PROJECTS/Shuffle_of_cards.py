# Shuffle of cards...

#Solution:-
import random
import itertools


face_cards = list(itertools.product(range(1, 5), ["A", "K", "Q", "J"]))
deck = list(itertools.product(range(2, 11), ["spade", "club", "diamond", "heart"]))

random.shuffle(deck)
random.shuffle(face_cards)
suits = {1: "spade", 2: "club", 3: "diamond", 4: "heart"}

print("Number Cards:")
for i in range(4):
    value = deck[i][0]
    suit = deck[i][1]

    if value == 1:
        name = "Ace"
    elif value == 11:
        name = "Jack"
    elif value == 12:
        name = "Queen"
    elif value == 13:
        name = "King"
    else:
        name = str(value)


    if suit == "spade":
        suit_name = "Spade"
    elif suit == "club":
        suit_name = "Club"
    elif suit == "diamond":
        suit_name = "Diamond"
    elif suit == "heart":
        suit_name = "Heart"

    print(name + " of " + suit_name)

print("\nFace Cards:")
for j in range(4):
    suit_num = face_cards[j][0]
    face = face_cards[j][1]


    if suit_num == 1:
        suit_name = "Spade"
    elif suit_num == 2:
        suit_name = "Club"
    elif suit_num == 3:
        suit_name = "Diamond"
    elif suit_num == 4:
        suit_name = "Heart"

    print(face + " of " + suit_name)
    print("let's the game begins...")
