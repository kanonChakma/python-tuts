#parent class
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber


#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def display(self):
        print(self.name, self.idnumber, self.post,  self.salary)    



e1 = Employee("titon", 1241424,234234,"Intern")
e1.display()



#------------------------------













