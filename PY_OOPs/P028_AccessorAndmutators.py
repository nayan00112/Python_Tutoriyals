# Accessor Methods: Gatters
# Mutators Methods: Satter

class Employee:
    Compney = "ABCD Compney"

    def __init__(self, name, work):
        self.name = name
        self.work = work

    def display(self):
        print(self.name + " " + self.work)

    # Accessor
    def getWork(self):
        return self.work

    def getName(self):
        return self.name

    # Mutators
    def setWork(self, work):
        print("updating work...")
        self.work = work
        print("Done...")

    def setName(self, name):
        print("updating name...")
        self.name = name
        print("Done...")


e1 = Employee("RUdra", "Level 4")
e2 = Employee("Kanj", "Level 3")

print(e1.getName())
print(e2.getName())
print(e1.getWork())
print(e2.getWork())

e1.setName("Rudra Shah")
e1.display()

e2.setWork("Level 4")
e2.display()

# Output
# RUdra
# Kanj
# Level 4
# Level 3
# updating name...
# Done...
# Rudra Shah Level 4
# updating work...
# Done...
# Kanj Level 4