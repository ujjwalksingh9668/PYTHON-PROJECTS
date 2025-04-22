# stone Paper Scissor game....

# Solution:-
import random

choice = ("stone","paper","scissor")
player = input("choose any one option from choise: ")

computer = random.choice(choice)
print("computer choose: ",computer)
print("player choose: ",player)

if player == computer:
    print("its a tie")
elif player == "scissor" and computer == "paper":
    print("you win")
elif player == "stone" and computer == "scissor":
    print("you win")
elif player == "paper" and computer == "stone":
    print("you win")
else:
    print("you lost")

print("thank you for playing")



