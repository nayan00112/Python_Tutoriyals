class A:
    def __init__(self):
        print("in A init")


class B(A):
    def __init__(self):
        print("in B init")


b1 = B()  # in B init


print("-------------------------")


class C:
    def __init__(self):
        print("in C init")


class D(C):
    def __init__(self):
        super().__init__()
        print("in D init")


d1 = D()

print("-------------------------")


class E:
    def __init__(self):
        print("in E init")

    def Hello(self):
        print("Hello E")


class F(E):
    def __init__(self):
        print("in F init")

    def Hello(self):
        print("Hello F")


f1 = F()
f1.Hello()

print("-------------------------")


class G:
    t = 5
    def __init__(self):
        print("in G init")

    def Hello(self):
        print("Hello G")


class H(G):
    t = 45
    def __init__(self):
        print("in H init")

    def Hello(self):
        super().Hello()
        print("Hello H")

    def disp_t(self):
        print(self.t)
        print(super().t)

h1 = H()
h1.Hello()
h1.disp_t()

# Output
# in B init
# -------------------------
# in C init
# in D init
# -------------------------
# in F init
# Hello F
# -------------------------
# in H init
# Hello G
# Hello H
# 45
# 5