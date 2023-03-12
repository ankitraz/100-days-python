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