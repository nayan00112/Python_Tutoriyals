# Multilevel single inheritance

class A:
    def show(self):
        print("Hello A")

    def a_method(self):
        print("In A Method")


class B(A):
    def show(self):
        print("Hello B")

    def b_method(self):
        print("In B Method")


class C (B):
    def show(self):
        print("Hello C")

    def c_method(self):
        print("In C Method")


a1 = A()
a1.a_method()
a1.show()
print()
b1 = B()
b1.a_method()
b1.b_method()
b1.show()
print()
c1 = C()
c1.a_method()
c1.b_method()
c1.c_method()
c1.show()


# Output:
# In A Method
# Hello A

# In A Method
# In B Method
# Hello B

# In A Method
# In B Method
# In C Method
# Hello C
