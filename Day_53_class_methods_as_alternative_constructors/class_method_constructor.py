class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age


    # additional constructor
    @classmethod
    def fromString(cls,string: str):
        return cls(string.split('-')[0],string.split('-')[1])


# p1 = Person("Ankit", 23)
# print(p1.name)
# print(p1.age)


# what if we pass name and age as a string containing both values combined
value = "Ankit-23"

# # we can use split function
# print(value.split("-")) # return a list containing items individually
# print(value.split('-')[0]) # this will give ankit
# print(value.split("-")[1]) # this will give age



p2 = Person(value.split('-')[0],value.split("-")[1]) # this will also work but it is less readable


# for this we cannot modify our constructor or else line 8 method of using constructor will stop working
# so we made a class method as constructor at line 6
# and now we use it

p3 = Person.fromString(value)
print(p3.name)
print(p3.age) # and now it will start working