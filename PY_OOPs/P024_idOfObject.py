class Computer:
    pass

c1 = Computer()
c2 = Computer()
print(id(c1)) # 2161810734624
print(id(c2)) # 2161810734384
print(c1.__sizeof__())
print(c2.__sizeof__())

# Everytime you create an object it is allocate to new space in heap memory.
# Size of an object is depends on the no. of variables
# Constructor (init method) is allocates size to the object.
