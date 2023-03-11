class Person:
    Name = ""
    Age = ""

    def __init__(self, name, age) -> None:
        self.Name = name
        self.Age = age

    def info(self):
        print(f"This is {self.Name} and I am {self.Age} years old.")




p1 = Person("Ankit", 20)
p2 = Person("Shobhit", 21)


p1.info()
p2.info()