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



#