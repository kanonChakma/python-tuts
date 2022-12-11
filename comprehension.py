#array Comprehension
#nested array
nestedArray = [[i]*i for i in range(5)]
print(nestedArray)

#array
myArray = [i for i in range(5)]
print(myArray)

arr = [2]*5
print(arr)

#set comprehension
mySet = {i for i in range(10)}
print(mySet)

#Dic comprehension
mayMap1 = {i: 2*i for i in range(5)}
print(mayMap1)
