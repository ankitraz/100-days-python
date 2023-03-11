# Class Methods as alternative constructor -
1. Class methods can be used as alternative constructors.
2.  For example, let’s say you have a class Person with an __init__() method that takes a first name and last name as arguments. 
3. You could create an alternative constructor using a class method that takes a full name as an argument and splits it into first and last name before creating an instance of the Person class.

Here’s an example:

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split(' ')
        return cls(first_name, last_name)


p1 = Person('John', 'Doe')
p2 = Person.from_full_name('Jane Doe')
```
* In this example, we have defined an alternative constructor from_full_name that takes a full name as an argument and creates an instance of the Person class using the first_name and last_name extracted from the full name.


## Difference between class method and a static method
The main difference between a class method and a static method is that a class method takes `cls` as its first parameter while a static method needs no specific parameters¹. A class method can access or modify the class state while a static method can't access or modify it.

A class method is bound to the class but not the object of that class. For class methods, we need to specify `@classmethod` decorator². A static method is a general utility method that performs a task in isolation. For static methods, we need to specify `@staticmethod` decorator².
