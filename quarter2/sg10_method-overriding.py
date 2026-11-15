class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats")

class Lion(Animal):
    def eat(self):
        print(f"{self.name} eats fresh meat.")
    def make_sound(self):
        print(f"{self.name} roars loudly")

class Elephant(Animal):
    def eat(self):
        print(f"{self.name} eats grass and fruits.")
    def make_sound(self):
        print(f"{self.name} trumphets")

class Monkey(Animal):
    def eat(self):
        print(f"{self.name} eats bananas")
    def make_sound(self):
        print(f"{self.name} chatters")

lion1 = Lion("Simba")
ele1 = Elephant("Dumbo")
mon1 = Monkey("George")

print("----------------------------")

lion1.make_sound()
lion1.eat()
print("----------------------------")

ele1.make_sound()
ele1.eat()
print("----------------------------")

mon1.make_sound()
mon1.eat()
print("----------------------------")
