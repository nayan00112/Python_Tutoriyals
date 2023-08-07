class A:
    def __init__(self):
        print("in A init")


class B(A):
    def __init__(self):
        print("in B init")

b1 = B()

print("======================================")

class C:
    def __init__(self):
        print("in C init")


class D(C):
    pass


d1 = D()

print("======================================")

class E:
    def __init__(self):
        print("in E init")


class F(E):
    def __init__(self):
        print("in F init")

f1 = F()

print("======================================")

# If you create object of sub class it will first try find init of subclass. if it  is not found then it will call init of super class


# Output:
# in B init
# ======================================
# in C init
# ======================================
# in F init
# ======================================
