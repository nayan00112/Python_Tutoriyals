a = 4
b = 2

print(a + b)  # 6

print(int.__add__(a, b))  # behind the scene. # 6

# __add__ is one of the magic method.

a = "5"
b = "6"

print(a+b) # 56

print(str.__add__(a, b)) # 56


# Magic Methods:
# __add__()
# __sub__()
# __mul__()
# and more... 




