myTyple = (1,2,3,1.5, "some", "one", [["1"], ["2"]])

print(myTyple)
print(myTyple[0])
print(myTyple[3])

for i in myTyple:
    print(i, end=' ')
print()



#list ot tuple
list1 = [3,4,5,6,7,8]
myTyple1 = tuple(list1)
print(myTyple1)

#----set----
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
Set.add("hello")

Set = set()
Set.add("hello")
print(Set)



#-----
print(5+(-1))


newDic = dict()
newDic["hello"] = 1
newDic[-1] = 1

print(newDic.get("hello0"))
newDic[-1]+=1
newDic[-1]+=1
newDic[-1]+=1

print(newDic[-1])


print(type(None))

