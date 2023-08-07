class Humen:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def display(self):
        print(self.name, self.age)
    
    # ERROR May BW
    def comp(self, other): 
        if ((self.name == other.name) and (self.age == other.age)):
            return "Both are same"
        else:
            return "Not Same"
        
h1 = Humen("Nayan", 21)
h2 = Humen("Jignesh", 21)
h3 = Humen("jignesh", 21)

h1.display()
h2.display()

print(h1.comp(h2))
print(h2.comp(h3))
