
#Each key should have to unique key in dictonaries
Employee = {
    1: [3,4,5,6,7,8],
    "name": "riton",
    "age": 24,
    "salary": 34000
}


#add
Employee[2] = [3,4,5,6,7]
Employee["value_set"] = 4,5,6,7

#update
Employee["name"] = "titon"

#get
print(Employee["name"])
print(Employee.get("name"))

#print(Employee["Name"]) it will produce Error
print(Employee.get("Name")) # return None

print(Employee)


