import math
#Queues(double ended queue)
from collections import deque

#-----Queue---
queue = deque()
queue.append(20)
queue.append(30)
queue.appendleft(10)
print(queue)

#pop right
queue.pop()
#pop leff
queue.popleft()
print(queue)
print("-----------------------------------")

#-------HashSet-------
mySet = set()
mySet.add(10)

#-----Queue---
queue = deque()
queue.append(20)
queue = deque()
queue.append(20)
queue.append(30)
queue.appendleft(10)
print(queue)

mySet.add(20)
print(mySet)
print(len(mySet))
print(20 in mySet)
print(40 in mySet)
mySet.remove(20)
print(mySet)

#list to set
print(set[1,2,3,4,5])

#set comprehension
mySet = {i for i in range(5)}
print(mySet)


#Hash map (Dictonary are hash map in python)
history={"year" :1000, "name":"history"}

myMap = {}
myMap["age"] = 23
myMap["name"] = "supon"
print(myMap)
print(len(myMap))

#modify value
myMap["name"] = "titon"
myMap["age"] = 25
print(myMap)

print("name" in myMap)

if "rahul" in myMap:
    print(myMap["rahul"])
else:
    myMap["rahul"] = 34

print(myMap)
myMap.pop("rahul")
print(myMap)

#Dict comprehension
myMap1 = {i: 2*i for i in range(5)}
print(myMap1)

#Looping through maps
newMap = {"name":"sahid", "roll": 34,"village":"vuiasara"}
#m1
for key in newMap:
    print(key, newMap[key])
#m2
for val in newMap.values():
    print(val)
#m3    
for key, val in newMap.items():
    print(key, val)
print("-----------------------------------")


#tuples are immutable
myTyple = (1,2,3,4,5)
#tuple can be used as key for hash map/set
tupleMap = {(1,2): 3}
print(tupleMap)

tupleSet = set()
tupleSet.add((1,2))
print((1,2) in tupleSet)
print(tupleSet)

#-----Queue---
queue = deque()
queue.append(20)
queue.append(30)
queue.appendleft(10)
print(queue)#-----Queue---
queue = deque()
queue.append(20)
queue.append(30)
queue.appendleft(10)
print(queue)



#Lists cannot be keys

print("-----------------------------------")
#string
#valid numeric string to int
add = int('123') + int('123')
print(add)

#int are converted to string
convert = str(123) + str(123)
print(convert)

#for ASCII value
print(ord("a"))
print(ord("z"))

#combine a list of string
#delimeter
strings = ["ka","non","chak","ma"]
print("".join(strings))
print("-----------------------------------")


#Loop through Array
nums = [4,5,6,7,8]
names = ["hi", "hello", "abc", "sometimes", "cute"]

#"Using Index"
for i in range(len(nums)):
    print(nums[i])

# Without Index
for n in nums:
    print(n)

# With index and Value
for i, n in enumerate(nums):
    print(i,n)

#Loop through multiple arrays simultaneously
#with uppacking
nums1 = [1,3,5]
nums2= [2,4,6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

#sorting
nums.sort()
nums.sort(reverse=True)

#sort by alphabatically order
names.sort()
print(names)
print("-----------------------")

#sort by length
names.sort(key=lambda x: len(x))
print(names)
print("-----------------------")

#List comprehension
allNums = [i for i in range(5)]
print(allNums)
print("-----------------------")

#Arrays(called list in phyton)
#insert middle 0(n)
arr = [1,2,3,4,5]
arr.append(6)    #12,3,4,5,6
arr.pop(5)       #pop 5 index
arr.insert(2,30) #insert 2 index 30
print(arr)       #[1, 2, 30, 3, 4, 5]

print(arr[1:4])  #[2,30,3]
print(arr[-2])   #[4]
print(arr[:])    #[1,2,30,3,4,5]
print(arr[:4])   #[1,2,30,3]
print(arr[1:-1]) #[2,30,3,4]

print("-----------------------")
#initialixe arr of size n with default value of 1
arrr = [1]*5
print(arrr)
print("-----------------------")

#Max/ Min Int
float("inf")
float("-inf")

#python numbers are infinite so they never overflow
print(math.pow(2, 200))
print(math.pow(2, 200) < float("inf"))
print("-------------------------------")

#Division is decimal by default
print(7/3)  #2.333333
print(int(7/3)) #2
print(7//3) #2

print(-3/2)  # -1.5
print(-3//2) # -2
print(int(-3/2)) #-1 

print(10%3) #1
print(-10%3) #2
print("-----------------------")

#math helpers
print(math.fmod(-10,3)) #-1.0
print(math.ceil(3/2)) #2
print(math.floor(3/2)) #1

print(math.sqrt(2)) #
print(math.pow(2,3)) #8
print("-----------------------")

#---------multiple assignment------
n, m = 3,"value"
#increment
n+=1

#None is null(absence of value)
a = 5
a = None
print(a)
print("-----------------------")

#if statement
a=10
if a<6:
    a =10

elif a>6:
    a=50

else:
    a= 100    
print("-----------------------")

#parentheses needed for multiline conditions
j = 4
k = 7
if((j<5 and
   k !=j ) or k==j):
   j+=1

#while  loop
while j<9:
    print(j)
    j+=1
print("-----------------------")

#For loop
for i in range(5,9):
    print(i) #5,6,7,8
print("-----------------------")

for i in range(5, 1, -1):
    print(i) #5,4,3,2


