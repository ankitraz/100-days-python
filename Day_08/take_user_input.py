# we can take input from user using input() function

print("Enter your name: ")
name = input()
print("Enter your age: ")
age = input()
print("Hi", name,"you are ", age, "years old.")

# we can also typecast the input to int or float because input() function always returns a string
print("Enter your age: ")
age = int(input())
print("Hi", name,"you are ", age, "years old.")

# we can also do this in one line
age = int(input("Enter your age: "))
print("Hi", name,"you are ", age, "years old.")

