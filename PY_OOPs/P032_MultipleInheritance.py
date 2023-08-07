# Multiple inheritance

# MRO (Method Resolutation Order)
# Sub class can access all the features of super class but Super class cannot access any feature of subclass 

class A:
    v = 34
    t = 55

    def show(self):
        print("Hello A")

    def a_method(self):
        print("In A Method")

    def hay(self):
        print("A: HellO")


class B:
    v = 35

    def show(self):
        print("Hello B")

    def b_method(self):
        print("In B Method")

    def hay(self):
        print("B: HellO")


class C (A, B):
    v = 36

    def show(self):
        print("Hello C")

    def c_method(self):
        print("In C Method")


a1 = A()
a1.a_method()
a1.show()
print()
b1 = B()
b1.b_method()
b1.show()
print()
c1 = C()
c1.a_method()
c1.b_method()
c1.c_method()
c1.show()
print(c1.v)
print(c1.t)

# MRO (Method Resolutation Order)
# A and B both class have same name mathod named hay(). in this multile inheritance case, which class method will execute? -> Class A, it search left to right.
c1.hay() # >>>>>=== LEFT TO RIGHT ===>>>>>

# Output:
# In A Method
# Hello A

# In B Method
# Hello B

# In A Method
# In B Method
# In C Method
# Hello C
# 36
# 55
# A: HellO
