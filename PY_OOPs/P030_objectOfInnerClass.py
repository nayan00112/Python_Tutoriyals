class OuterClass:
    a = 10

    class InnerClass:
        b = 15
        def show(self):
            print("in innerclass show")

    def show(self):
        print("in Outerclass show")

o = OuterClass()

# inner class object
i = OuterClass.InnerClass()

o.show()
i.show()

# Output:
# in Outerclass show
# in innerclass show


# You can create object of inner class inside the outer class (Privious example where we created laptop class object inside the init method of outer class.)
# or
# You can create object of inner class outeside the outer class provided you use class name to call it (This code example.). 
