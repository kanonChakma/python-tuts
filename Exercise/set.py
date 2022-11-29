myset = set()
myset.add(20)
myset.add(30)
myset.add(40)
myset.add(40)
myset.add(40)
print(myset)

myset.remove(40)
print(myset)

#creating new set with array
names = ["dear", "you", "have", "to"]
new_set = set(names)

print(new_set)
print("dear" in names)
