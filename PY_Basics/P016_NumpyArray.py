from numpy import *
# Copy Array
a = array([1, 2, 3, 4])
b = array([3, 4, 5, 6])

c = a
# Here, both have same id means same location. so not unique.
# modification with a is also effect in c.
print(id(a))
print(id(c))
c.put(1,3)
print(a, c)
# this is called Aliasing.


print("============== view ==============")
# view do not working : AttributeError: 'array.array' object has no attribute 'view'
c = a.view()
print(id(a))
print(id(c))
# different location but changes in one also affect to another.
a.put(0,22)
print(a, c)

print("============== copy ==============")

# Copy of array
# proper copy, different location and no any relation so changes in one cannot affect to another copy.

c = a.copy()

print(id(a))
print(id(c))
a.put(0, 34)
print(a, c)

print('=====================================')

s = array([3, 5, 7 ,8, 2])
print(s + 1)
print(s * 5)
print(log(s))
print(sin(s))
print(cos(s))
print(sqrt(s))


# Output
# 2459835290128
# 2459835290128
# [1 3 3 4] [1 3 3 4]
# ============== view ==============
# 2459835290128
# 2460108842736
# [22  3  3  4] [22  3  3  4]
# ============== copy ==============
# 2459835290128
# 2460108842832
# [34  3  3  4] [22  3  3  4]
# =====================================
# [4 6 8 9 3]
# [15 25 35 40 10]
# [1.09861229 1.60943791 1.94591015 2.07944154 0.69314718]
# [ 0.14112001 -0.95892427  0.6569866   0.98935825  0.90929743]
# [-0.9899925   0.28366219  0.75390225 -0.14550003 -0.41614684]
# [1.73205081 2.23606798 2.64575131 2.82842712 1.41421356]