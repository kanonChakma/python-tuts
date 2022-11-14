class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("constructor called")
    
    def show_detail(self):
        return self.age, self.name

    def __del__(self):
        print("Destrctor called")


employe1 = Employee("riton", 34)
del employe1
