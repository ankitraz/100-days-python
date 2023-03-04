# dictionaries are ordered collection of data items,
# theys store multiple items in a single variable.
# they store data in key:value pair seperated by commas and enclosed with  {}

dict = {
    "Name" : "Ankit",
    "UID" : "21CDO1058",
    "Branch" : "DevOps"
}


print(dict["Name"]) # printing value using its keys. this will throw an error if the key that you are accessing is not available.
print(dict)  # get all the elements of dictionary
print(dict.get('Name')) # this will return 'none' if the key is not found in dictionary


# get all the keys of a dictionary
print(dict.keys())

# get all the values of dictionary
print(dict.values())


# using a for loop to get all the key values
for key in dict.keys():
    print(f"The value correspondig to the key {key} is {dict[key]}")


# we can print all the key-value pairs in the dictionary using items() method.

print(dict.items())
for key,value in dict.items():  # this will map keys with key varaible and values with value variable.
    print(f"{key} --> {value}")
