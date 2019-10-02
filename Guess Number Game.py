import time
import os
import random
num = random.randint (1,10)
life = 5
flag = 0

print("\n\t*** GUESS THE NUMBER GAME ***\n")
player = input("Welcome player!\nEnter your name: \n")

print ("\t\tWelcome ",player,"!")

while (life != 0):
    print("Life Remaining: ",life)
    print("Guess a number between 1 to 10: ")
    inp = int(input())
    if inp != num:
        if inp > num:
            life-=1
            print("Your Guess is High,\nTry again! \n\t Remaining life: ",life)
        else:
            life-=1
            print("Your Guess is Low,\nTry again! \n\t Remaining life: ",life)
    elif inp == num:
        print ("Correct! You win.")
        flag = 1
        break
if flag != 1:
  print ("\nSorry, you ran out of lives!")
  print ("The correct Answer is: ",num)

print("\n\n\t* SCORE CARD *\n")
print("Player's Name: ", player, "\nLife Remaining: ",life)
