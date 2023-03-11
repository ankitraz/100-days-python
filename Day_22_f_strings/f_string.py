# fstring is used to format a string.



#old ways to format a stirng
letter = "I am learning {} and building {}"
language = "python"
building = "apps"

print(letter.format(language,building)) # we can also switch order as well

# we can also add number to the {} in the variable letter.

letter2 = "I am learning {0} and building {1}"
print(letter.format(language,building))



# fstring way
print(f"I am learning {language} and building {building}")
price = 45.77788
print(f"this is the {price:.2f}")  # print prices till 2nd decimal places


print(type(f"{2*5}"))


print(f"we use f-stirng like this {{var1}} and {{var2}}")  # this will literally print var1 and var2 and not their values.