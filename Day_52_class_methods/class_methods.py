class Student:
    school = "Woodbine modern school"

    def __init__(self,name,grade) -> None:
        self.name = name
        self.grade = grade
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

    @classmethod  # static or class method used to change class variable
    def change_school(cls,new_school):
        cls.school = new_school


s1 = Student("Ankit",'A')
s2 = Student("shobhit",'B')


print(s1.school)  # accessing class variable
print(s2.school)  # accessing class variable


# suppose we want to change school for
Student.change_school("new School") # changing class variable

s1.change_school("Bro") # this will change class variable.

print(s1.school)  # accessing class variable
print(s2.school)  # accessing class variable
