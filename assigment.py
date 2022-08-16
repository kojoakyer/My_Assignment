#Object Oriented Programming in Python Assignment

class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        print(name)

    def get_age(self):
        return self.age

    def bite(self):
        return 'woww'

    def bark(self):
        print('bark')

    def add(self,x):
        return x + 1


d = Dog('scoby', 5)
d.bark()
d.get_age()
print(d.add(5))
print(type(d))