# create a function that takes returns sum of two numbers.

# def product(num1, num2):
#     temp = num1*num2
#     return temp


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# Sum = product(num1,num2)   #function call is happening here
# print("Sum: ", Sum)



num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("1. Sum")
print("2. division")
print("3. product")
print("4. subtraction")
print("5. All")
choice = int(input("Enter your choice: "))
print("==================================")

if choice == 1:
    print("Sum : ",num1+num2 )
elif choice == 2:
    print("Division: ", num1/num2)
elif choice == 3:
    print("Product: ", num1*num2)
elif choice == 4:
    print("subtraction: ", num1-num2)
elif choice == 5:
    print("Sum : ",num1+num2 )
    print("Division: ", num1/num2)
    print("Product: ", num1*num2)
    print("subtraction: ", num1-num2)
else:
    print("Invalid choice!")
print("==================================")

