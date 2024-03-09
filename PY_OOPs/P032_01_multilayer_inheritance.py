class B:
    def __init__(self):
        print("in B super")
class A (B):
    def __init__(self):
        print("in A")
        
aa = A()

# output:
# in A


class C:
    def __init__(self):
        print("in C super")
class D (C):
    def __init__(self):
        super().__init__()
        print("in D")
        
dd = D()

# output:
# in C super
# in D


class X:
    def __init__(self):
        print("X super super")

class Y(X):
    def __init__(self):
        print("in Y super")
class Z (Y):
    def __init__(self):
        super().__init__()
        print("in Z")
        
CC = Z()

# output:
# in Y super
# in Z


class AA:
    def __init__(self):
        print("AA super super")

class BB(AA):
    def __init__(self):
        super().__init__()
        print("in BB super")

class CC (BB):
    def __init__(self):
        super().__init__()
        print("in CC")
        
CCC = CC()

# output:
# in BB super
# AA super super
# in CC


class MM:
    def __init__(self):
        print("MM super super")

class NN(MM):
    def __init__(self):
        print("in NN super")
        super().__init__()

class OO (NN):
    def __init__(self):
        super().__init__()
        print("in OO")
        
o = OO()

# Output:
# in NN super
# MM super super
# in OO


class MMM:
    def __init__(self):
        print("MMM super super")

class NNN(MMM):
    def __init__(self):
        print("in NNN super")
        super().__init__()

class OOO (NNN):
    def __init__(self):
        print("in OOO")
        super().__init__()
        
oo = OOO()

# Output:
# in OOO
# in NNN super
# MMM super super




# In Python, if a subclass has its own __init__ method and does not explicitly call the __init__ method of its parent class using super().__init__(), the constructor of the parent class won't be automatically called.

# In your Python example:


# class B:
#     def __init__(self):
#         print("in B super")

# class A(B):
#     def __init__(self):
#         print("in A")

# aa = A()


# The output will be:

# in A


# This is because the __init__ method of class A does not call the __init__ method of its parent class B.