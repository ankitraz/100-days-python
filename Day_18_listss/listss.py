# list are ordered collection of data items
# they store multiple items in a single variable.
# they are sepearated by command and enclosed within square brackets
# lists are changable meaning we can alter them after creation
# we can access list element by their index.


marks = [2,4,5]
print(marks)

print(type(marks))  # will give the data type of marks variable

print(marks[0])
print(marks[1])  # accessing elements of list using index
# index can be positive and negative as well
print(marks[-1])  # python will convert this into +ve index by subtracting this value form {len(index)-1}


# we can also include multiple data types in a list.
var2 = [1,3,'a',"Ankit", True]
print(var2)


# using "in" keyword with lists
if 4 in marks:
    print("Value is available.")
else:
    print("Value is not available.")
    

# we can also use "in" keyword in strings as well
var3 = "Ankit raj"
if "Ankit" in var3:
    print("Value is present")
else:
    print("Not present")



# print every element of list
print(marks)
print(marks[:])  # python automatically add 0 to len(marks) in this case
print(marks[1:-1])
# print(marks[from:to:step])
# same string concept applies here also.



#LIST COMPREHENSION - used to create new list from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# Syntax - List =[Expression(item) for item in iterable if condition]
#Expression - it is the item which is being iterated
# iterable - it can be list, tuples, dictionaries, sets and even in arrays and strings.
# Condition - condition checks if the item should be added to the new list or not.

lst = [i for i in range(4)]
print(lst)
lst2 = [i*i for i in range(4)]
print(lst2)
lst3 = [i*i for i in range(10) if i%2 == 0]
print(lst3)



