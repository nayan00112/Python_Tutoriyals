class Car:
    def __init__(self, model, price, kmpl):
        self.model = model
        self.price = price
        self.kmpl = kmpl

    def __gt__(self, other):
        if (self.kmpl/self.price) > (other.kmpl/other.price):
            return self.model
        else:
            return other.model

c1 = Car("ABC", 700000, 25)
c2 = Car("PQR", 605000, 27)
c3 = Car("XYZ", 400000, 27)

print("Which is batter btw, c1 and c2?")
print(c1>c2)

print("Which is batter btw, c2 and c3?")
print(Car.__gt__(c2, c3))

print("Which is batter btw, c3 and c1?")
print(c1>c3)

# Output:
# Which is batter btw, c1 and c2?
# PQR
# Which is batter btw, c2 and c3?   
# XYZ
# Which is batter btw, c3 and c1?   
# XYZ