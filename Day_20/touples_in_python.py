# touples are similar to lists but the only key difference between them is that touples are immutable


# creating a touple by using brackets
tup = (2,4,5,6,7)
print(tup)
print(type(tup))


# when there is only one element in touple then it is mandatory to add a ',' after it otherwise it will become int object
tup2 = (1)
print(type(tup2)) # this will give int object type
tup3 = (1,)
print(type(tup3))


# You can access element of touples just like accessing an element of a list
tup4 = (1,2.4,"Ankit", True)
print(tup4[3])


# using 'in' keyword in touple
if "Ankit" in tup4:
    print("Ankit is available in above touple")


# we can also do touple slicing just like list slicing
tup_new = tup4[1:2]
print(tup_new)


# there is no direct way to add a new element in touple.