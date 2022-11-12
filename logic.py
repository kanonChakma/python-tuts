good_credit = True
amount = 1000000

if good_credit:
    amount = 10/100 * amount
else:
    amount = 20/100 * amount
print(f'have to payment ${amount}')


#Logical Operator
result = True
skill = True

if result and skill:
    print("will be eligible")

if result or skill:
    print("eligible for specific candidate")

if not skill:
    print("have to gain")
elif result and not skill:
    print("have to increase")
else:
    print("will be eligible brother")    

#Comparison 
name = "this is name bro"

if len(name) <= 3:
    print("Name should be greater than 3")

elif len(name) >=50:
    print("Name should less than 50")

else:
    print("Name is good")


