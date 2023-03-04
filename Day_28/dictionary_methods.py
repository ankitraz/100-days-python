dict = {
    "Name" : "Ankit",
    "UID" : "21CDO1058",
    "Branch" : "DevOps"
}


# update() method is used t update the value of existing key, if the key do not exist, it will create new one
dict.update({"Name":"Ankit raj"})
dict.update({"Age": 21})

print(dict)



# # clear() method is used to remove all the items from the list.
# dict.clear()
# print(dict)


# pop() method removes the key-value pair whose key is passed as a parameter
dict.pop('Age')
print(dict)



# popitem() method removes the last key-value pair from the dictionary

dict.popitem()
print(dict)



# del keyword is used to remove a dictionary item
# however if no key is provided as paramater, it will delete the entire dictionary

del dict['Name']
print(dict)


del dict
