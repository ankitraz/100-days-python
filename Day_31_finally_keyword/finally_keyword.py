try:
    l = [1,4,5,6,7]
    usr_input = input("Enter the index: ")
    print(l[usr_input])
except:
    print("Some error excepted")

# finally:
#     print("this is always executed")
print("this is always executed.")

# finally block is always executed no matter whether an exception is occured or not.

## but the important question is why do we need finally? 
# even if we don't use finally keyword and just use some print statemnt below except block, that statement will get executed also
# like we did in line 10

# ✨ The main difference is when we use these try-execpt-finally in a function definition*****

def fun():
    try:
        l = [1,4,5,6,7]
        usr_input = input("Enter the index: ")
        return 0
    except:
        return -1
    finally:
        print("This is always executed even after funtion return.✨")
    print("this is always executed.")  # this is not executed after function returns.



print(fun())



# this is the actual use of finally block in execption handling.
