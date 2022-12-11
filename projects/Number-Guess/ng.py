import random

input_num = input("enter a number Limit ")

if input_num.isdigit():
    input_num = int(input_num)    
    if input_num<0:
        print("please enter a number greater than 0")
        quit()
else:
    print("Enter a number next time..")
    quit()

random_number = random.randint(0, input_num)

while True:
    guess_number = input("enter guess number ")
    if guess_number.isdigit():
        guess_number= int(guess_number)
    else:
        print("enter a valid number")
        continue
    
    if guess_number == random_number:
        print("You are match")
        break
    elif guess_number < random_number:
        print("guess_number are less than random number")
    else:
        print("guess_number are greather than random number")
    
        