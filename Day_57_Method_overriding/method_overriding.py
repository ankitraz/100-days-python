class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("Animal eating... from animal class")


class Mammal(Animal):
    def __init__(self) -> None:
        self.weight = 2
        super().__init__()
    def walk(self):
        print("walk")
    def eat(self):
        super().eat() # it will call the eat method of parent class
        print("mammal eating")


m = Mammal()
# print(m.age) # it will give error because constructor of mammal class is overriding the constructor of animal class
print(m.weight)
print(m.age) # now it will work after adding super method in mammal class
m.eat()



# Method overriding
