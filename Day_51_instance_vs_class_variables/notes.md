### Instance variables and class variables are two types of variables that can be used in Python classes. They have different scopes and behaviors.

1. Instance variables are variables that are declared inside the constructor or other instance methods of a class. 
2. They are not shared by objects of the same class¹. 
3. They are created when an object of the class is instantiated¹³. 
4. They can be accessed or modified using the `self` parameter that refers to the current object²³. Changes made to these variables through one object do not affect other objects of the same class¹.

Class variables are variables that are declared inside the class definition but outside any instance methods²⁴. They are shared by all objects of the same class¹. They are created when the program begins to execute¹⁴. They can be accessed or modified using either the class name or the `self` parameter that refers to the current object²⁵. Changes made to these variables through one object will affect all other objects of the same class¹.

Here is an example of how to use instance variables and class variables in Python:

```python
class Employee:
  # defining a class variable
  company = "ABC Inc."

  # defining a constructor with instance variables
  def __init__(self, name, salary):
    # assigning values to instance variables
    self.name = name
    self.salary = salary

  # defining an instance method with instance variable
  def display(self):
    print(f"Name: {self.name}, Salary: {self.salary}")

# creating two objects of Employee class
e1 = Employee("Alice", 5000)
e2 = Employee("Bob", 6000)

# accessing and modifying class variable using object e1
print(e1.company) # output: ABC Inc.
e1.company = "XYZ Ltd."
print(e1.company) # output: XYZ Ltd.

# accessing and modifying class variable using object e2
print(e2.company) # output: ABC Inc.
e2.company = "PQR Co."
print(e2.company) # output: PQR Co.

# accessing and modifying instance variable using object e1
print(e1.name) # output: Alice
e1.name = "Anna"
print(e1.name) # output: Anna

# accessing and modifying instance variable using object e2
print(e2.name) # output: Bob
e2.name = "Ben"
print(e2.name) # output: Ben

# calling display method on both objects
e1.display() # output: Name: Anna, Salary: 5000
e2.display() # output: Name: Ben, Salary: 6000

```

As you can see, we can use both instance variables and class variables in Python classes. Instance variables store data that is specific to each object. Class variables store data that is common to all objects.
