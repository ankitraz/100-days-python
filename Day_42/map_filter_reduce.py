from functools import reduce

# MAP function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
# syntax -> map(function, iterable)


def square(num):
    return num**2

# suppose we want to create a new list that contains the square of each elemnents of some another list items
l = [1,2,3,4,5,6]
newlist = list()

# traditional approach
for i in l:
    newlist.append(square(i))

print(newlist)

# but we can do this in simpler way using map function
newlist2 = list(map(square,l))
print(newlist2)

# we can also use lambda function with map functon
# a function which takes another function as argument is known as higher order function
newlist3 = map(lambda num:num**2,l)
print(list(newlist3))






# FILTER -> this function is filters a sequence of elements based on a given predicate(a function that returns a boolean value)
# and returns a new sequence containing only the elements that meet the predicate. the filter function has the following syntax
# filter(predicate, iterable) ---> predicate is a funcion which returns a boolean value.

def iseven(num):
    return num % 2 == 0


evens = filter(iseven,l)
print(list(evens))


# we can also use lamda funcition with map and filters
evens2 = filter(lambda num:num%2 == 0,l)
print(list(evens2))






# REDUCE ->  this is a higher-order function that applies a function to a sequence and returns a single value.
# we need to import it from functools module first
# syntax -> reduce(function, iterable)

numbers = [1,2,3,4,5]

# calculate the sum of the number using the reduce function
sum = reduce(lambda x,y:x+y, numbers)
print(sum)


