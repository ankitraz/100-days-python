# variables are containers for storing data values.
#   - variable name must start with a letter or the underscore character
#   - variable name cannot start with a number

a = 4
b = 6.0
c = "ankit"
d = True
e = None
print(a, b, c, d, e)
# we don't need to specify the data type of the variable in python

a = 5
print(a)  # printng the updated value of a

print("Type of a is", type(a) , "and type of b is", type(b))

# there are some advanced data types in python
# list, tuple, set, dictionary

# list is a collection which is ordered and changeable. Allows duplicate members.
name = ['ankit', 6, 9.0, True, None]
print(name[0])  # accessing the first element of the list
print(name[-1])  # accessing the last element of the list
print(name[1:3])  # accessing the elements from index 1 to 2
print(name[1:])  # accessing the elements from index 1 to last
print(name[:3])  # accessing the elements from index 0 to 2

# we will see these in advanced data types
# one thing to note is that list everything in python is an object.


# we can also do arithmatic operations inside print function
print(5 + 6, 5 - 6, 5 * 6, 5 / 6, 5 % 6, 5 ** 6, 5 // 6, sep=",") #// is floor division, and ** is power and % is modulus
