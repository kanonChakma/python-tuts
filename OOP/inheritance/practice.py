class Animal:
    def __init__(self, name):
        self.animalName = name
        print(name, "is ana animal")

    def display(self):
        print("anmalName is : ", self.animalName)


class Mammal(Animal):
    def __init__(self, name):
        print(name, "is a mammal")
        super().__init__(name)
    
    def mammal_behaviour(self):
        print("The presence of hair or fur")
        print("Sweat glands.")
        print("Specialized teeth, A four-chambered heart.")



class CannotSwim(Mammal):
    def __init__(self, mammalCannotSwim):
        print(mammalCannotSwim, "can not swim")
        super().__init__(mammalCannotSwim)


class CannotFly(Mammal):
    def __init__(self, mammalCannotFly):
        print(mammalCannotFly, "can not fly")
        super().__init__(mammalCannotFly)        


class Cat(CannotFly, CannotSwim):
     def __init__(self, mammalCannotFly):
         super().__init__(mammalCannotFly)

cat = Cat("cat")
cat.mammal_behaviour()

