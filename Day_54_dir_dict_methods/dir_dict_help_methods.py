# dir() method returns list of all the attribute and methods
# including(dunder methods) available for an object. It is an useful
# tool for discovering what you can do with an object

l = [1,3,4]

# print(dir(l))  # it will list all the methods and attribute

# we can also get info about a specific methods from that list
# print(l.__add__)
# print(l.append)



#===========================================================
# dict methods returns a dictionary representation of an object's attribute
# It is a useful tool fo introspection.

class Person:
    def __init__(self,name,age,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

p = Person("Ankit", 20,34000)
# print(p.__dict__)

#===========================================================
# help() method is used to get help documentation for an object
# including a description of its attributes and methods.

print(help(str))  # it will give everything about that object
print(help(Person))