# Like other languages (for example, method overloading in C++) do, python does not support method overloading by default. But there are different ways to achieve method overloading in Python.

class Calc:
    def sum(self, a=0, b=0, c=0): # Bydefault it is 0.
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        else:
            return a

c1 = Calc()

print(c1.sum(4, 6))

print(c1.sum(6, 2, 7))

print(c1.sum(8))

# Output:
# 10
# 15
# 8