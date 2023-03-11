class Employee:

    company = "Google"

    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

e1 = Employee("Ankit", 230000)
print(e1.company)
e1.company = "Microsoft"
print(e1.company) 


print(Employee.company)  #In our code, e1.company = "Microsoft" creates a new instance variable called company for the e1 instance, which shadows the class variable company. This means that when you access e1.company, it returns the value of the instance variable, which is "Microsoft", instead of the class variable, which is still "Google".
Employee.company = "BLaBla"
# we can modify  class variable by using class.variable = value


e2 = Employee("Shubham", 340000)
print(e2.company)  # it should be changed to "blabla"
# e2.company = "IBM"
# print(e2.company)


# e1.display()
# e2.display()

