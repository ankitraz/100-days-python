class Employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, language) -> None:
        super().__init__(name, id)  # for setting value of name and id, we are just using constructor from parent class, we are following dry principle😅
        self.language = language


p = Programmer("Ankit", 34, "Python")
print(p.id)
print(p.name)
print(p.language)