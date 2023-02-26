# upper and lower methods

s1 = "Ankit"
print(s1.upper())

s2 = "ANKIT"
print(s2.lower())

# most commmon question is that - does python changes the original string or not?
# the answer is no, it does not change the original string as strings are immutable
# but it returns a new string with the changes.


# remove trailing characters from the string
s3 = "Ankit!!!!!!!!!!"
print(s3.rstrip("!"))


# replace all occurence of a string with another string
print(s3.replace("Ankit", "Ankit raj"))

# split method is used to split a string into a list of substrings
s4 = "Ankit Raj is pro"
print(s4.split())


#capitalize method is used to capitalize the first letter of the string and make the rest of the string lower case
s5 = "ankit raj is pro."
print(s5.capitalize())

# center method is used to center the string in a given width
s6 = "ankit"
print(s6.center(20, "*"))


# count method is used to count the number of occurences of a substring in a string
s7 = "ankit raj is pro"
print(s7.count("a"))


# endswith method is used to check if a string ends with a given substring
s8 = "ankit raj is pro"
print(s8.endswith("pro"))
# we can also even check of a value in between the string
print(s8.endswith("is", 0, 10))


# find method is used to find the index of a substring in a string
s9 = "ankit raj is pro"
print(s9.find("is"))

# index method is used to find the index of a substring in a string
# the difference between find and index is that find returns -1 if the substring is not found but index throws an exception
# print(s9.index("hello"))


# isalnum method is used to check if a string is alphanumeric
s10 = "ankit123"
print(s10.isalnum())

# isalpha method is used to check if a string is alphabetic
s11 = "ankit"
print(s11.isalpha())
# the difference between isalpha and isalnum is that isalpha returns true if the string is alphabetic but isalnum returns true if the string is alphanumeric


# islower method is used to check if a string is lower case
s12 = "ankit"
print(s12.islower())

# isupper method is used to check if a string is upper case
s13 = "ANKIT"
print(s13.isupper())

# isprintable method is used to check if a string is printable. it means that it does not contain any non-printable characters. suppose we have a string with a new line character in it, then it is not printable
s14 = "ankit"
print(s14.isprintable())


# isspace method is used to check if a string contains a space
s15 = " "
s16 = "ankit"
print(s15.isspace())
print(s16.isspace())

# istitle method is used to check if a string is a title
s17 = "Ankit Raj Is Pro"
print(s17.istitle())

# swapcase method is used to swap the case of a string i.e. lower case becomes upper case and vice versa
s18 = "Ankit Raj Is Pro"
print(s18.swapcase())


# title method is used to convert a string into title case
s19 = "ankit raj is pro"
print(s19.title())


