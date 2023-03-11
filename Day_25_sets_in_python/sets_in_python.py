"""sets are unordered collection of data items. 
the store multiple items in a single variable.
set items are separated by commas and enclosed withing curly brackets{}
sets are unchangeable, meaning you cannot change items of the set once created.
sets do not contain duplicate items."""


set1 = {
    "Ankit",
    3,
    6.7,
    3,
}
print(set1)  # duplicate item is automatically removed


# creating an emply set
set2 = set()  # this will create a new set
print(type(set2))


# Accessing elements of a set - we know that sets are unordered, so there is no concepts of indexing here.
# random order is followed by set elements.

for i in set1:
    print(i)
