#A static method is a type of method that belongs to a class but does not bind to a class or instance12. 
# Static methods do not rely on any class or instance data to perform a task13. 
# Static methods are general utility methods that perform a task in isolation23.


# static methods cannot modify variables of a class. Static methods do not have access to any class or instance attributes. They can only use the arguments that are passed to them or the global variables that are defined outside the class.
# If you want to modify variables of a class, you need to use either instance methods or class methods. Instance methods can modify instance attributes using the self parameter.
#  Class methods can modify class attributes using the cls parameter.


class Example:
    def __init__(self,num) -> None:
        self.num = num

    @staticmethod
    def add(a,b):      
        return a+b


# calling a static method without creating an object
print(Example.add(4,5))
