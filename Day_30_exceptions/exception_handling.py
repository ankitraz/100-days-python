# Exception handling is the process of respondint to unwanted or unexpected events when a computer program runs.
# It deals with these events to avoid the program or system crashing and without this process, exceptions 
# would distrupt the normal operation of a program.


try:
    user_input = input("Enter a number: ")
    print(2*int(user_input))
except:
    print("Value in not an interger.")

print("Code continues....")




# we can also use different type of exception in a single try

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")



# we can also print the error we got in terminal to the user
try:
    user_input = input("Enter a number: ")
    print(2*int(user_input))
except Exception as e:
    print(f"Error is: {e}")

print("Code continues....")