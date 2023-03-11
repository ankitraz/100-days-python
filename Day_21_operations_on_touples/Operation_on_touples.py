########change element in touple indirectly

countries = ("Spain","Italy", "India","England")
# -- first we need to conver this toubpe into a list
temp = list(countries)
temp.append("Russia") # adding a new item in list
temp.pop(2) # removing an item from list

countries = tuple(temp) # again changing that temp list to touple.
print(countries)



# merge two touples
a = (1,3,4,5)
b = ('A','B','c')

d = a + b  # we are just creating a new touple from existing ones.
print(d)



# touple methoods ##

# count method used to count the occurence of an element in touple
print(a.count(1))

# index method is used to get the first occurence of a particular element in a touple
print(a.index(4))

# find length of touple
print(len(a))


# important note is that  - you can not change a touple in its original state, but it can be done by modifiying it into a list just like i did above
