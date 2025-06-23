# Dice roller game.......
     
# Solution:-
import random
user = input("do yo want to roll the dice: ")
while user == "yes":
    k= random.randint(1, 6)
    if k == 1:
        print("--------")
        print("|      |")
        print("|   *  |")
        print("|      |")
        print("--------")
    if k == 2:
        print("--------")
        print("|     *|")
        print("|      |")
        print("|*     |")
        print("--------")
    if k == 3:
        print("--------")
        print("|     *|")
        print("|  *   |")
        print("|*     |")
        print("--------")
    if k == 4:
        print("--------")
        print("|*    *|")
        print("|      |")
        print("|*    *|")
        print("--------")
    if k == 5:
        print("--------")
        print("|*    *|")
        print("|   *  |")
        print("|*    *|")
        print("--------")
    if k == 6:
        print("--------")
        print("|* * *|")
        print("|* * *|")
        print("|* * *|")
        print("--------")
    user = input("do you want to roll the dice again")



