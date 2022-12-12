import random

you_win = 0
computer_win = 0

options = ["rock", "paper", "sessiors"]

while True:
    user_input = input("Enter rock/paper/scissors or q for quit ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue
    
    ran = random.randint(0,2)
    computer_pick = options[ran]
    print("computer picked ", computer_pick)

    if user_input == 'rock' and computer_pick == "scissors":
        print("You win! ")
        you_win +=1
    
    elif user_input == 'paper' and computer_pick == "rock":
        print("you win ")
        you_win +=1

    elif user_input == 'scissors' and computer_pick == "paper":
        print("you win ")
        you_win += 1
    
    else:
        print("computer win ")
        computer_win += 1

print("You win", you_win, "comouter win", computer_win)
print("Good Bye")    



