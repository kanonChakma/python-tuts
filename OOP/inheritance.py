class Animal:
    def fly(self):
        print("Able to fly")
    def walk(self):
        print("Able to walk")

class Bird(Animal):
    pass

class Cat(Animal):
    pass


bird = Bird()
bird.fly()

cat = Cat()
cat.walk()
