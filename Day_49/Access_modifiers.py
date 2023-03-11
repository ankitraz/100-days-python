# Access modifiers are used to modify the default scope of a variable or a method in a class.
# They determine how other classes can access and use the data members and member functions of a class.

## public access modifier

# class Student:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# s1 = Student("Ankit",20)
# print(s1.name)  # we can see that name and age are by default public and can be accessed without any restriction
# print(s1.age)
# s1.show()


# -------------------------------------------------------------------------------------------------------------
## protected access modifier
# """
# According to Python convention, adding a prefix _ (single underscore) to a variable or a method name makes it protected.
# This means it can be accessed and modified only by the class itself and its subclasses (or derived classes),
# but not by any other class or object. However, this is only a convention and not enforced by Python interpreter.
# """

# class Student:
#     def __init__(self,name,age) -> None:
#         self._name = name   # by adding _ before any variable makes it protected
#         self._age = age
#     def _show(self):  # protected method
#         print(f"Name: {self._name}")
#         print(f"Age: {self._age}")


# class Graduate(Student):
#     def __init__(self, name, age, degree) -> None:
#         super().__init__(name, age)  # calling parent class constructor
#         self.degree = degree
#     def show(self):
#         super()._show()  # accessing protected method from parent class
#         print(f"Degree: {self.degree}")


# g1 = Graduate("Ankit",20,"Btech")
# g1.show()


#### -------------------------------------------------------------------------------------------------------------

# '''Private access modifier:
# Adding a prefix __ (double underscore) to a variable or a method name makes it private.
# This means it can be accessed and modified only by the class itself, but not by any other class or object.
# Python interpreter enforces this by using name mangling technique which changes the name of the private attribute to _ClassName__AttributeName'''


# class Student:
#     def __init__(self,name,age) -> None:
#         self.__name = name   # private variable
#         self.__age = age
#     def __show(self):  # private method
#         print(f"Name: {self.__name}")
#         print(f"Age: {self.__age}")

# s1 = Student("Ankit",20)
# s1.__show()  # this will give error as the method  we are trying to access is private.
# # However, we can still access and modify private attributes using name mangling technique


#### -------------------------------------------------------------------------------------------------------------

# Name mangling is a technique used in Python to protect instance variables from being accidentally
# overwritten or shadowed by instance variables with the same name in derived classes123.
# Name mangling works by adding a double underscore prefix to the name of an instance variable,
# and replacing any occurrences of the underscore character in the name with an underscore and the class name1


# class Example:
#     def __init__(self) -> None:
#         self.__name = "Example"  # private variable

# class subExample(Example):
#     def __init__(self) -> None:
#         super().__init__()  # calling parent class constructor
#         self.__name = "subexample" # private variable

# s1 = subExample()
# print(s1._subExample__name)  # Accessing subclass private variable
# print(s1._Example__name) # accessing parent class private variable


# -------------------------------------------------------------------------------------------------------
# Name mangling is also used for methods that start with double underscores2. For example:


# class Example:
#     def __init__(self):
#         self.__display()  # calling private method

#     def __display(self):  # private method
#         print("This is an example.")


# class SubExample(Example):
#     def __init__(self):
#         super().__init__()  # calling parent class constructor
#         self.__display()  # calling private method

#     def __display(self):  # private method
#         print("This is a subexample.")


# se = SubExample()
# #When the object se is created, it invokes the constructor of the subclass SubExample.
# # The constructor first calls the constructor of the parent class Example using the super() function.
# # This in turn calls the private method of the parent class _Example__display (after name mangling) and prints “This is an example.”
# # Then, the constructor of the subclass calls its own private method _SubExample__display (after name mangling)
# # and prints “This is a subexample.”


class Example:
    def __init__(self):
        self.__display()  # calling private method

    def __display(self):  # private method
        print("This is an example.")


e = Example()
# e.__display() # this will raise an AttributeError as __display is private
e._Example__display()  # this will work as _Example__display is mangled name
