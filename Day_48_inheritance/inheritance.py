class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")


# inheriting dog class from animal
class Dog(Animal):
    # constructor from animal class is also inherited here so does its properties
    def bark(self):
        print(f"{self.name} is barking")



cat = Animal("Taxi")
cat.eat()


dog = Dog("tiger")
dog.eat()
dog.bark()
