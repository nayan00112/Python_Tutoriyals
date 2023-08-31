class Laptop:
    def __init__(self, model, price):
        self.model = model
        self.price = price

l1 = Laptop("ABC01", 50000)
l2 = Laptop("PQR02", 60000)

# here we want to make addition of their price using + operator only,

# print(l1 +l2) # TypeError: unsupported operand type(s) for +: 'Laptop' and 'Laptop'

# but above sentance throws an error (as l1 and l2 is not integer or number but objects of class laptop.)
# hence we make our magic method for + operator which do addition of their price. 
# Visite next code... 

