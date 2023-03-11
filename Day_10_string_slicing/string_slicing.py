# string slicing is used to access the elements of string
s1 = 'Hello World'
print(s1[0:5])
print(s1[6:11])

print(s1[0:5:2]) # it will print every second character from 0 to 5 with step size 2
print(s1[:5]) # it will print from 0 to 5

print(s1[0:-1]) # it will print from 0 to len(s1)-1

print(len(s1)) # this will print the length of string
