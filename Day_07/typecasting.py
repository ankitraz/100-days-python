# typecasting means converting one data type to another data type

var = 5
print(var, type(var))  # explicit typecasting
var = float(var)
print(var, type(var))


# implicit typecasting - python automatically converts one data type to another data type
var = (5 + 4.1)
print(var, type(var))