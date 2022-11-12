#By default function return None
#None is an object that represents the absence of a value
#Argument in programming is the value that we supply to a function

"""
parameters are the holes or placeholders  
that we define in our function for receiving 
information
"""

"""
Argument are the actual peices of information that 
we supply to these functions
"""

def print_name():
    print("this is my name")    


print_name()

def salary(firstPerson,secondPerson,thirdPerson):
    print(firstPerson,secondPerson,thirdPerson)


salary(4000,5000,6000)
#keyword argument (specially used when sedn numerical value)
salary(thirdPerson=6000,firstPerson=4000,secondPerson=5000)
salary(6000,4000,thirdPerson=5000)



#excepion

try:
    res = int(input("Enter number: "))
    div =  3000/res
    print(res)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Enter a valid number")








