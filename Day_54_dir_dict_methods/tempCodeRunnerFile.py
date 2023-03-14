class Person:
    def __init__(self,name,age,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

p = Person("Ankit", 20,34000)
print(p.__dict__)