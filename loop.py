#use for loop to iterate over all the item in a collection
#collection can be string, can be list, can be object
#anything any kind of object that has multiple items
#for loop
"""
for num in [3,4,5,6,7,8,9]:
    print(num)

names = ["karim", "rahim", "sikim"]
for name in names:
    print(name) 


#rang function create special type of object that we can iterate over
#range(start, end, step)
for item in range(2,10):
    print(item)

for item in range(20,40, 5):
    print(item)
"""

#-------nested for loops------ 
persons = [["tipon", 12], ["supon", 20], ["ripon", 34]]
"""
for i in persons:
    for j in persons:
        print(persons[i,j]) 
"""

person_names = ["kanon", "supon", "tipon", "ripon"]
numbers = [5, 2, 5, 2, 2]
for num in numbers:
    count = ''
    for n in range(num):
          count+="#"
    print(count)      

print("*" * 5) #*****   












