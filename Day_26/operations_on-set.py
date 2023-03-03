s1 = {1,2,5,6}
s2 = {3,6,7,1}


# union of set
print(s1.union(s2))
print(s1,s2) # we can see that our original s1 and s2 set is unaffected


# # what if we want to update our original set
# s1.update(s2)
# print(s1) # now our set1 is changed


# intersection of set
print(s1.intersection(s2))

# # intersection_update
# s1.intersection_update(s2)
# print(s1)


# symmetric difference of set - those values which are not common in two sets
print(s1.symmetric_difference(s2))
# similarly there is symmetric difference update operation as well


# difference of set - prints only items that are only present in the original set and not in both the sets
print(s1.difference(s2))
# similarly there is difference_update method as well



## SET METHODS 

# isdisjoint()
print(s1.isdisjoint(s2))


# issuperset()
print(s1.issuperset(s2))


# issubset()
print(s1.issubset(s2))

# add a single item to the set
s1.add(57)
print(s1)


#update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

s1.update(s2)
print(s1)


# remove() - used to remove an item form list
#The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

s1.remove(6)
print(s1)


# pop() - """
# The main difference between remove and discard is that, 
# if we try to delete an item which is not present in set, 
# then remove() raises an error, whereas discard() does not raise any error.


s1.pop()
print(s1)


# del is used to delete the set entirely

del s1


# clear() method is used to clears all items in the set and prints and empty set
s2.clear()
print(s2)