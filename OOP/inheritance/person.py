class Person:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def display(self):
        return self.name, self.location
    
    def isEmployee(self):
        return False    
    
    def walk(self):
        print("can walk")



#inherited or subclass
class Employee(Person):
    def isEmployee(self):
        return True    

person1 = Person("titon",  "longadu")
print(person1.display())
print(person1.isEmployee())

employee1 = Employee("supon", "khagrachari")
print(employee1.display())
print(employee1.isEmployee())
