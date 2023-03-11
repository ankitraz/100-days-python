# recursion is a function calling itself

def factorial(num):
    if (num in (1,0)):   # num==1 or num==0
        return 1
    return (num*factorial(num-1))
    


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)




print(factorial(3))
print(fibonacci(3))



