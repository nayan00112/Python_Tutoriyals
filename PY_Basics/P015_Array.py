import array as arr

a = arr.array("i", [3, 5, 76, 74, 24, 77, 78, 86])

print(a[3])

print(a)
print(a.pop())
print(a)
print(a.insert(4, 45))  # index, value
print(a)

print(a.append(57))
print(a)

# we have to pass element inside as argument in this function.
print(a.remove(5))

print(a)
print(a.pop())
print(a)
a.reverse()
print(a)

p = arr.array('i', [3, 5, 6, 8])
q = arr.array('i', [53, 54, 63, 28, 3, 9])

r = p + q     # Vectorized Operation

print(r)

s = arr.array("i", [1, 2, 3, 4])

print(sum(s))
print(max(s))
print(min(s))
print(s.tolist())

# Output
# 74
# array('i', [3, 5, 76, 74, 24, 77, 78, 86])
# 86
# array('i', [3, 5, 76, 74, 24, 77, 78])
# None
# array('i', [3, 5, 76, 74, 45, 24, 77, 78])
# None
# array('i', [3, 5, 76, 74, 45, 24, 77, 78, 57])
# None
# array('i', [3, 76, 74, 45, 24, 77, 78, 57])
# 57
# array('i', [3, 76, 74, 45, 24, 77, 78])
# array('i', [78, 77, 24, 45, 74, 76, 3])
# array('i', [3, 5, 6, 8, 53, 54, 63, 28, 3, 9])
# 10
# 4
# 1
# [1, 2, 3, 4]