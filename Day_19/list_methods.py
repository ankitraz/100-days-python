l = [4,5,6,4,3]
print(l)


# using append method to add elements at the end of a list
l.append(8)
print(l)


# using sort method to sort elements of list
l.sort()
print(l)
l.sort(reverse=True)
print(l)


# gettin index of element of list
l2 = [3,5,3,2,4,6,5]
print(l2.index(5))

# count method is used to count all the occurence of an element in a list
print(l2.count(5))


# create a copy of list
k = l2.copy()
print(k)
# Note: to be added, while equating a list to another list, any change made in new list will also reflect in old one. so this is not recommended 

# insert multiple values in a list
l3 = [2,3,5,6,78]
print(l3)
l3.insert(3,0)   # insert element before a particular index.
print(l3)



# merge to list and in a new list
l6 = [1,2,4]
l7 = [45,67,89]

l8 = l6 + l7
print(l8)



# extend an existing list
l_original = [54,67,86,32]
l_extend = [1,0]

l_original.extend(l_extend)
print(l_original)