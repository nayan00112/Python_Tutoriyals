class Computer:
    def __init__(self): #like constructor in java or cpp
        print("in init")
    def config(self):
        print("i5, 8gb, 512gb")

com1 = Computer()
com2 = Computer()

com1.config()
com2.config()

# Outputin init
# in init
# i5, 8gb, 512gb
# i5, 8gb, 512gb