import array as arr

a = arr.array("i", [3, 5, 76, 74, 24, 77, 78, 86] )

print(a[3])

print(a)
print(a.pop())
print(a)
print(a.insert(4, 45)) #index, value
print(a)

print(a.append(57))
print(a)

print(a.remove(5)) # we have to pass element inside as argument in this function. 

print(a)
print(a.pop())
print(a)
a.reverse()
print(a)
