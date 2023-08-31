class A:
    def show(self):
        print("In A Class")

class B(A):
    def show(self):
        print("In B Class")

a = A()
a.show() # In A Class

b = B()
b.show() # In B Class

c = A()
c.show() # In A Class

c = B()
c.show() # In B Class