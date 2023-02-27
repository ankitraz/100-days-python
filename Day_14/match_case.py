x = int(input("Enter a number: "))

match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _ if x < 1:
        print("x is less than 1")
    # we can also use if statement in match case
    case _ if x > 3:
        print("x is greater than 3")
    case _:
        print("x is something else")
        # _ is a wildcard this is default case.