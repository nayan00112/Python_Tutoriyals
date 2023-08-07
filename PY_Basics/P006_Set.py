s = {2, 4, 6, 7, "a", "b", "c", "PQR", "XYZ"}

print(s)

print(s.add("Nayan"))
print(s)

t = {2, 7, "a"}
print(s.issubset(t))
print(t.issubset(s))

print(t.issuperset(s))
print(s.issuperset(t))

print(t.issubset(t))
print(t.issubset(t))

print(t.issuperset(t))
print(t.issuperset(t))

print(s.pop())
print(s.pop())
# print(s.remove(2)) #Error
print(s.union(t))

u = {3, 2, 6, 8, 123, 545}

print(t.union(u))
w = t.copy()
v = t
print(id(t))
print(id(w))
print(id(v))

print(t.isdisjoint(s))


# Output
# {'c', 2, 'a', 4, 6, 7, 'b', 'PQR', 'XYZ'}
# None
# {'c', 2, 'a', 4, 6, 7, 'b', 'PQR', 'XYZ', 'Nayan'}
# False
# True
# False
# True
# True
# True
# True
# True
# c
# 2
# {2, 'a', 4, 6, 7, 'b', 'PQR', 'XYZ', 'Nayan'}
# {545, 2, 3, 'a', 6, 7, 8, 123}
# 1357542058688
# 1357542058240
# 1357542058688
# False