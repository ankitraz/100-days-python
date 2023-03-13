# Multilevel Inheritance
## Introduction

Multilevel Inheritance is a feature in Python where a class can inherit from a derived class. This is different from single inheritance where a class can only inherit from one base class.

## Syntax : 

```python
class Base:
    pass
class Derived(Base):
    pass
class Derived2(Derived):
    pass
```

## Example :

```python
class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    pass


class chicken(Bird):  # this may lead to inheritance abuse
    pass

# chicken is a derived class of Bird which is a derived class of Animal

# there may be an inheritance abuse like in the above example bird class may have a method called fly() which later gets inherited to chicken, and we all know chickens can't fly.
```

* *One or Two level of inheritance is fine, but more than that may lead to inheritance abuse and increased overall complexity and readibility of code.*