# Super Keyword

Super keyword is used to invoke the methods of parent class in child class.

## Example:

```python
class ParentClass:


    def parent_method(self):
        print("This is the parent method.")



class ChildClass(ParentClass):


    def child_method(self):
        print("This is the child method.")
        super().parent_method()

    def parent_method(self):
        print("This is the parent method form child class. Now calling parent method.")
        super().parent_method()




child_object = ChildClass()
child_object.child_method()
child_object.parent_method()
```

Output:

```bash
This is the child method.
This is the parent method.
This is the parent method form child class. Now calling parent method.
This is the parent method.
```

## How Super Keyword Works?

* When we create a child class, it inherits all the methods from the parent class.

* When we call a method with the same name as a method in the parent class, the child's method is called instead of the parent's method.

* To call the parent's method, we use the `super()` function.

## Why Super Keyword?
* It is used to invoke the methods of parent class in child class.

* It is used to invoke the constructor of parent class in child class.


## `super` keyword with constructor

```python
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

```

In above code:
* We are using `super()` to call the constructor of parent class.

* We are passing the arguments `name` and `id` to the constructor of parent class. this is done by `super().__init__(name, id)`.

* We are passing the argument `language` to the constructor of child class.

Conclusion:
Super keyword is used to invoke the methods of parent class in child class.