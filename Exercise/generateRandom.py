import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
       


dice1 = Dice()
print(dice1.roll())

"""
#produce random value between 10 and 20
for num in range(3):
    print(random.randint(10,20))


#choice random person
persons = ["titon", "kiron", "sipon", "bipon"]
for person in persons:
    print(random.choice(persons))


#produce random value between 0 and 1
print(random.random())
print(random.random())
print(random.random())
"""
