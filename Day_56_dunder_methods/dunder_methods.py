# dunder - double underscore

# magic methods are special methods that we can define in our classes
# and when invoked, they give us a powerful way to manipulated objects and behaviour

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

