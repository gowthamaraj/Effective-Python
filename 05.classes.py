from datetime import date
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name: str, year: int):
        return cls(name, date.today().year-year)

    @staticmethod
    def isAdult(age):
        return age>18


p1 = Person('mayank', 21)
p2 = Person.fromBirthYear('mayank', 1998)
print(p1.age)
print(p2.age)


# public private protected
class employee:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal
class employee:
    def __init__(self, name, sal):
        self._name=name
        self._salary=sal
class employee:
    def __init__(self, name, sal):
        self.__name=name
        self.__salary=sal
