# Multiple Inheritance
## Introduction 
Multiple Inheritance is a feature in Python where a class can inherit from *multiple base classes*. This is different from single inheritance where a class can only inherit from one base class.

## Syntax
```python
class Base1:
    pass
class Base2:
    pass
class Derived(Base1, Base2):
    pass
```

***Note:*** The order of the base classes in the derived class matters. The first base class **will be searched first for any attribute/method**. If it is not found, the second base class will be searched and so on.

## Example
```python
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer,Swimmer):
    pass

ff = FlyingFish()
ff.fly()

# there is an ambiguity in the above code as to whether the fly method is from the Flyer class or the Swimmer class 
# it is decided by the order of the base classes in the derived class

# like in the above example, the Flyer class is searched first and the fly method is found in the Flyer class
```

