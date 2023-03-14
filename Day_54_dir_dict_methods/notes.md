# dir(), dict() and help( ) methods

## dir method

* `dir()` - It is used to get the list of attributes and methods of any object (say functions, modules, strings, lists, dictionaries etc.)
  * Tool for discovering what you can do with an object.

Example:
```python
l = [1,3,4]

print(dir(l))  # it will list all the methods and attribute of any module or anything

we can also get info about a specific methods from that list
print(l.__add__)
print(l.append)
```

## dict method

* `dict()` - It return the dictionary representation of attributes related to an object 

Example:

```python
class Person:
    def __init__(self,name,age,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

p = Person("Ankit", 20,34000)
print(p.__dict__)
```

Output:

```bash
{'name': 'Ankit', 'age': 20, 'salary': 34000}
```

## help method

* `help()` - It is used to get the documentation of any object.
    * Example: 
        ```python
        help(str)
        help(list)
        help(YourClass)
        ```
  

**Overall, These are the methods which are used to get the information about the object.**