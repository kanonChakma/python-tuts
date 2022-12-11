class Person:
    def __init__(self, name: str, age: int, village: str, education:int = None):
        self._name = name
        self.__age = age
        self.__village = village
        self.__education = education

    def set_info(self, name, age, edu):
        self._name = name
        self.__age = age
        self.__education = edu

    def get_person_info(self):
        return f"Name: {self._name},age: {self.__age} village : {self.__village},education: {self.__education if self.__education is not None else 'noValue'}"

person_lists = [Person("k1", 24, "d1", "bsc"),
Person("k2", 25,"d2","csc")
]
print(person_lists[0].get_person_info)

p1 = Person("kanon", "25", "dajarpara", "bsc")
print(p1.get_person_info())
print(p1._name)

        