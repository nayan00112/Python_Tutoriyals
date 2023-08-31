class Laptop:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    
    # Our MAgic method for + Operator. 
    def __add__(self, other):
        return self.price + other.price

l1 = Laptop("ABC01", 50000)
l2 = Laptop("PQR02", 60000)

print(Laptop.__add__(l1,l2))

print(l1 + l2)

# Output:
# 110000
# 110000