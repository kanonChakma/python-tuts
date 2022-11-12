#-------problem 1
#take input pound, convert in kilogram

"""
wieght_lbs = input("Enter Your wieght in pound ")
wieght_kg = int(wieght_lbs)*0.45
print(wieght_kg)
"""

#----problem 2
#convert weight

"""
weight = int(input("Enter Your Weight "))
pound_or_kg = input("lbs or kg ")

if pound_or_kg.lower() == 'l':
    weight *=  0.45 
    print(f'Your are {weight} kilos')

elif pound_or_kg.lower() == 'k':
    weight /=  0.45
    print(f'you are {weight} pounds')
else:
    print("Enter valid keyword")    
"""


#problem 3
"""
gusess number 
guess_number = 10
count = 1
while count <= 3:
    number = int(input("Enter Number "))
    count+=1
    if number == guess_number:
        print ("You win!")
        break
else:
     print("sorry you failed!")
"""

#problem 3

command = ""
start = False
stop = False

while True:
    command = input("> ").lower()

    if command == "help":
        print("start-- to start the car")
        print("stop-- to stop the car") 
        print("exit-- to exit") 
        
    elif command =="start":
        if start:
            print("car already started!!!!")
        else:
            stop = False
            start = True
            print("car  started!!!!")

    elif command =="stop":
        if stop:
            print("car already stoped!!!!")
        else:
            start = False
            stop = True
            print("car stoped!!!!")

    elif command == "exit":
        print("exited")    
        break     
    else:
        print("please enter valid command")

