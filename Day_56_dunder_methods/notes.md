# Dunder Methods - Double Underscore Methods or Magic methods

Magic methods are special methods that are used to perform certain operations. They are also called as dunder methods because of the double underscores before and after the method name.

* They give us a power to manipulate the behaviour of the objects.

Example:
```python
class Employee:

    def __init__(self,name) -> None:
        self.name = name


    name = "ankit"


    def __len__(self):  # note that we can use any thing insted of self, as first paramert in any method is passed as obj or class
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self) -> str:
        return f"The name of employee is {self.name}"

    def __repr__(self) -> str: # it will represent .....
        return f"employee is {self.name}"

    def __call__(self, *args: any, **kwds: any) -> any:
        return "Hey i am good"


e = Employee("Ankit")
# print(e.name)
# print(len(e))
print(e)  # it will use __str__ magic method
print(repr(e))

print(e()) # with the use of __call__ we can call an object just like a function
```

In abobe code we have overriden the `__len__` method which is called when we use `len()` function on an object.

* `__len__` takes one argument `self` which is the object on which we are using `len()` function.

* `__str__` is called when we use `print()` function on an object.

* `__repr__` is called when we use `repr()` function on an object.

* `__call__` is called when we call an object like a function.

Isnt it cool?

## Some more magic methods

* `__add__` - This method is called when we use `+` operator on two objects.

* `__sub__` - This method is called when we use `-` operator on two objects.

And so on, we will learn them in operator overloading module.