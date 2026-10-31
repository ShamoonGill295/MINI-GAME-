'''computer = gun    user = gun 
   computer = snake   user = snake
   computer = water   user = water  
     '''
import random 
choices = ["snake" , "gun" , "water"]
computer_choice = random.choice(choices)
my_choice = input("What you want to choose snake, water or gun: ").lower()

if my_choice not in choices:
     print("You enterd invalid choice")
     

if computer_choice == my_choice:
    print("Match is draw!")

elif (computer_choice == "gun" and my_choice == "water") or \
     (computer_choice == "snake" and my_choice == "gun") or \
     (computer_choice == "water" and my_choice == "snake"):
      print("You Won the game. Congratulations ")
else:
     print("Computer wons! YOU LOSS THE MATCH")

print(f"Computer chose: {computer_choice} \nYou chose: {my_choice}")







