names = ["some","one", "says", "that", "there", "is", "nothing", "do", "in", "life"]
print(len(names))
print(names[:5])

for name in names:
    print(name)

for i in range(len(names)):
    print(names[i])

for i, name in enumerate(names):
    print(name, i)


nested_names = [["tipon", "chakma"], ["riton", "chakma"], ["sneha", "chakma"]]

for all in nested_names:
    for name in all:
        print(name, end=' ')
    print()


# for i in range(len(nested_names)):
#     print(nested_names[i])

all_nums = [[1, 2, 3, 4], [5, 6], [7, 8, 9], [3,4,5], [6,7,8,9]]

#first way
for i in range(len(all_nums)):
    for j in range(len(all_nums[i])):
        print(all_nums[i][j], end=' ')
    print()

#second way
for row in all_nums:
    for ele in row:
        print(ele, end=' ')
    print()    


#create new two dimensional list(it will take reference [0]*m for each element)
n =3
m = 4
new_list = [[0] * m] * n
new_list[0][0] = 4

for row in new_list:
    for ele in row:
        print(ele, end=' ')
    print()

#Nested list creating(it will ot refernce)
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m

a[0][0]=4
for row in a:
    for ele in row:
        print(ele, end=' ')
    print()

#best way for creating a nested list
new_list1 = [[0]*m for i in range(n)]

for i in range(len(new_list1)):
    for j in range(len(new_list1[i])):
        print(new_list1[i][j], end=' ')
    print()

#convert type this array
"""
1 3 3 3
2 1 3 3
2 2 1 3
2 2 2 1
"""

new_list1 = [[0]*4 for i in range(4)]

for i in range(len(new_list1)):
    for j in range(len(new_list1)):
        if(i==j):
            new_list1[i][j] = 1
        elif(i>j):
            new_list1[i][j] = 2
        else:
            new_list1[i][j] = 3    
    

# for i in range(len(new_list1)):
#     for j in range(len(new_list1[i])):
#         print(new_list1[i][j], end=' ')
#     print()

for row in new_list1:
    print(' '.join([str(elem) for elem in row]))
