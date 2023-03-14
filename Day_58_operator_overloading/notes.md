# Operator Overloading
Operator overloading is a ways to extend the functionality of an operator.

for example: `+` operator can be used to add two numbers or concatenate two strings. This is called operator overloading.

## Overloading the `+` operator
```python
class Vector:
    def __init__(self,i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,b):  # these are known as magic arithmetic operators
        return Vector(self.i + b.i,self.j+b.j,self.k+b.k)
    

v1 = Vector(4,5,6)
v2 = Vector(1,2,3)


result = v1 + v2   # we can also call dunder method here but it is not advised to do so.
print(result)
```
In ABove code we have overriden the `+` operator to add two vectors.
* `__add__` is a dunder method which is called when we use `+` operator on two objects.

* `__add__` takes two arguments `self` and `b` which are the two objects on which we are using `+` operator.

* `__add__` returns a new object of the same class. In our case it returns a new vector object. It is important to return an object type because then only we will be able to add this vector class object to another object in future.

## Similarly, we can overload other operators : 
* `__sub__` for `-` operator
  
* `__mul__` for `*` operator

* `__truediv__` for `/` operator

* `__floordiv__` for `//` operator

* `__mod__` for `%` operator

* `__pow__` for `**` operator

And many more. You can find the complete list [here](https://docs.python.org/3/reference/datamodel.html#special-method-names)

Go to top of page [here](#operator-overloading)