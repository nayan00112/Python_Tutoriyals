class student: # Outerclass

    def __init__(self, name, rolNum):
        self.name = name
        self.rolNum = rolNum
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rolNum)

    # Innerclass
    class Laptop:
        def __init__(self):
            self.processor = "i5"
            self.ram = 8

        def show(self):
            print(self.processor, self.ram)


s1 = student("Nayan", 48)
s2 = student("Marmik", 11)
s2.lap.processor = "M1 Pro"
s2.lap.ram = 16

s1.show()
s1.lap.show()

s2.show()
s2.lap.show()

# Output:
# Nayan 48
# i5 8
# Marmik 11
# M1 Pro 16
