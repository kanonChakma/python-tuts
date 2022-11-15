class Mother(object):
    fage = ""
    def __init__(self, mname):
        self.__myMom = mname

    def mother(self):
        print("mom name is: ",self.__myMom)
        print("mom age is: ", self.fage) 


class Father(object):
    mage = ""

    def __init__(self, fname):
        self.__myfather = fname
        
    def father(self):
        print("father name", self.__myfather)
        print("father age", self.mage)


class Son(Mother, Father):
    def __init__(self, sname, fname, mname):
        self.sname = sname
        Father.__init__(self, fname)
        Mother.__init__(self, mname)

son1 = Son("kanon","kalasona", "padmasoval")
son1.fage =45
son1.mage = 35
son1.father()
son1.mother()
#---------------------
class Base1(object):
    def __init__(self, name):
        self.first_name = name


class Base2(object):
    def __init__(self, name):
        self.middle_name = name

class Base3(Base1, Base2):
    def __init__(self, fname,mname,lname):
        self.last_name = lname
        Base1.__init__(self,fname)
        Base2.__init__(self,mname)
    
    def display(self):
        print(self.first_name,self.middle_name,self.last_name)

b3 = Base3("rohit", "molla", "sumon")
b3.display()

#--------------------------------
class Mammal():
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)    

class canFly(Mammal):
    def __init__(self, name1,name2):
        self.name1 = name1
        super().__init__(name2)

class Animal(canFly):
    def __init__(self, name1, name2):
        super().__init__(name1, name2)
    
    def display(self):
        print(self.name, self.name1)

animal1 = Animal("dog", "alsdfj")
animal1.display()




