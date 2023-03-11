1. Class methods are methods that are called on the class itself, not on a specific object instance². Therefore, they belong to a class level, and all class instances share a class method².

2. Class methods can be used to access or modify class variables (also known as static variables), which are variables that are defined inside the class but outside any instance methods³. Class variables are shared by all objects of the same class¹.

3. Class methods can also be used to create alternative constructors for a class, which are methods that return an object of the class with different initialization parameters⁴.

 * To define a class method in Python, we need to use either the `@classmethod` decorator or the `classmethod()` function on top of the method definition¹². 
 * The first parameter of a class method is usually named `cls`, which refers to the current class¹². 
 * We can use `cls` to access or modify class variables or to call other class methods.

Here is an example of how to define and use class methods in Python:

```python
class Student:
  # defining a class variable
  school = "XYZ School"

  # defining a constructor with instance variables
  def __init__(self, name, grade):
    # assigning values to instance variables
    self.name = name
    self.grade = grade

  # defining an instance method with instance variable
  def display(self):
    print(f"Name: {self.name}, Grade: {self.grade}")

  # defining a class method with @classmethod decorator
  @classmethod
  def change_school(cls, new_school):
    # modifying a class variable using cls parameter
    cls.school = new_school

  # defining another class method with @classmethod decorator
  @classmethod
  def from_string(cls, student_str):
    # creating an alternative constructor using cls parameter
    name, grade = student_str.split(",")
    return cls(name, grade)

# creating two objects of Student class using normal constructor
s1 = Student("Alice", "A")
s2 = Student("Bob", "B")

# calling display method on both objects
s1.display() # output: Name: Alice, Grade: A
s2.display() # output: Name: Bob, Grade: B

# printing school name for both objects using dot notation
print(s1.school) # output: XYZ School 
print(s2.school) # output: XYZ School

# calling change_school method on Student class using dot notation 
Student.change_school("ABC School")

# printing school name for both objects after changing school name using dot notation 
print(s1.school) # output: ABC School 
print(s2.school) # output: ABC School

# creating another object of Student class using from_string method 
s3 = Student.from_string("Charlie,C")

# calling display method on s3 object 
s3.display() # output: Name: Charlie, Grade: C

```

As you can see, we can define and use class methods in Python. Class methods act upon the class itself and can access or modify class variables. Class methods can also provide alternative constructors for a class.
