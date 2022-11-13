numbers = [4,5,6,3,2,1]
print(numbers[0])
print(numbers[3:])

#change numbers
numbers[2] = 20
print(numbers)


#Find the largest numbers
max = numbers[0]
for num in numbers:
    if num>max:
        x = num
print(x)

#--------------2d list------------
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11],
 ]

print(matrix[0][1])
 
for row in matrix:
    for col in row:
        print(col)

#----list methods----
ages =[67,89,12,44,50]

#insert last in list
ages.append(51) 

#insert first index
ages.insert(0,66) 

#remove 89 from list
ages.remove(89) 

# ages.clear it will clear all list 
ages.pop() #remove last item
print(ages) 
  
#check a number exist or not in a list
# ages.index(100) will show error
print(100 in ages) #will return false
ages.append(50)

#count item in list
print(ages.count(50)) #2 
print(ages.count(500)) #0
# index show error when ther isno number but in method will provide boolean value
#None is an object in python that represents the absense of a value 

#Sort item in list
ages.sort()
print(ages) #12, 44, 50, 50, 66, 67

ages.reverse()
print(ages) #67, 66, 50, 50, 44, 12

#Copy item in list
newAges = ages.copy()
newAges[3] = 56
print(f'Newages is {newAges}, oldAges is {ages}')

