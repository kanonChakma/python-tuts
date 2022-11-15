#It represents real-world relationships well.
#It provides the reusability of a code

#Base or Super class
class Animal(object):
    def fly(self):
        print("Able to fly")
    def walk(self):
        print("Able to walk")


#Inherited or Subclass or derived class

class Bird(Animal):
    pass
class Cat(Animal):
    pass


bird = Bird()
bird.fly()

cat = Cat()
cat.walk()
