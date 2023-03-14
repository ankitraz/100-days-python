# Method Overriding

## What is Method Overriding?

It is the process of redefining the method of parent class in child class 
* The implementation in the subclass overrides (replaces) the implementation in the superclass by providing a method that has the same signature as the one in the superclass. 
* A method signature consists of a method name and the number, order, and type of its parameters. The return type of a method is not part of the method signature.

*Example*:

```python
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
```

## Why Method Overriding?

* It is used to provide the specific implementation of a method which is already provided by its parent class.

* It is used for runtime polymorphism.

* It is used to provide the implementation of abstract methods.

## How Method Overriding Works?

* When we create a child class, it inherits all the methods from the parent class.

* When we call a method with the same name as a method in the parent class, the child's method is called instead of the parent's method.

* We can use the super() function to call the parent's method.