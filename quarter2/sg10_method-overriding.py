class Animal: # creates the class and initializes attributes
  def __init__(self, name):
    self.name = name

  def eat(self): # creates the method eat
    print(f"{self.name} eats.")

class Lion(Animal): # creates the child class Lion and inherits the attributes and methods from animal
  # defines the methods and the outputs
  def eat(self): 
    print(f"{self.name} eats fresh meat.")

  def make_sound(self):
    print(f"{self.name} roars loudly!")

class Elephant(Animal): # creates the child class Elephant and inherits the attributes and methods from animal
  # defines methods and the outputs
  def eat(self):
    print(f"{self.name} eats grass and fruits.")

  def make_sound(self):
    print(f"{self.name} trumphets!")

class Monkey(Animal): # creates the child class Monkey and inherits the attributes and methods from animal
  # defines methods and the outputs
  def eat(self):
    print(f"{self.name} eats bananas.")

  def make_sound(self):
    print(f"{self.name} chatters!")

# assigns the product and the variables and their values
lion = Lion("Simba")
ele = Elephant("Dumbo")
mon = Monkey("George")

# prints the output
print("-----------OUTPUT-----------")

lion.make_sound()
lion.eat()

print("----------------------------")

ele.make_sound()
ele.eat()

print("----------------------------")

mon.make_sound()
mon.eat()

print("----------------------------")




