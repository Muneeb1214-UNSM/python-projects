"""
#MAKE THE GAME OF ROCK,PAPER,SCISSOR GAME USING PYTHON .
!:input from user(rock,paper,scissor)
2:Computer choice(computer will choose randomly not conditionally.)
3:print result

CASES:
1:ROCK
rock-rock=tie
rock-paper=paper win 
rock-scissor=rock win

2:PAPER
paper-paper=tie
paper-rock=paper win
paper-scissor=scissor win

3:SCISSOR
scissor-scissor=tie
scissor-paper=scissor win
scissor-rock=rock win.

"""

import random
items_list = ["rock","paper","scissor"]
user_choice = input("enter your move=rock,paper,scissor =  ")
comp_choice = random.choice(items_list)

print(f"user choice = {user_choice},computer choice = {comp_choice}")

if(user_choice == comp_choice):
    print("Both chooses same: = Match Tie.")

elif(user_choice == "rock"):
    if(comp_choice == "paper"):
        print("paper covers rock,Computer win.")
    else:
        print("rock smashes scissor, You win.")

elif(user_choice == "paper"):
    if(comp_choice == "rock"):
        print("paper covers rock,computer wins")
    else:
        print("scissor cuts paper,You win.")

elif(user_choice == "scissor"):
    if(comp_choice == "paper"):
        print("scissor cuts paper,computer wins.")
    else:
        print("rock smashes scissor,You win.")


