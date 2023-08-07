from numpy import *

m1 = matrix([[1, 2, 3], [5, 3, 1], [3, 6, 2]])
m2 = matrix([[3, 4, 3], [1, 4, 1], [6, 5, 5]])
print("Matrix 1 is")
print(m1)
print("Matrix 2 is")
print(m2)
print("Matrix Multiplication of m1 and m2 is:")
print(m1 * m2)

print(m1 + 3)

print("=============================")
# Another Way to represent matrix. 
m3 = matrix("1, 3, 5; 6, 2, 7; 8, 4, 5")
print(m3)

print(m1.dot(m2))
# print(m3.all())
# print(m1.any())
# print(m1.conjugate())
# print(m1.conj())
print(m1.transpose())
print(m1.sort())
# print(m1.size())

print(m1.max())
print(m1.min())

print(m2.diagonal())
# print(m1.getH())


# Output:
# Matrix 1 is
# [[1 2 3]
#  [5 3 1]
#  [3 6 2]]
# Matrix 2 is
# [[3 4 3]
#  [1 4 1]
#  [6 5 5]]
# Matrix Multiplication of m1 and m2 is:
# [[23 27 20]
#  [24 37 23]
#  [27 46 25]]
# [[4 5 6]
#  [8 6 4]
#  [6 9 5]]
# =============================
# [[1 3 5]
#  [6 2 7]
#  [8 4 5]]
# [[23 27 20]
#  [24 37 23]
#  [27 46 25]]
# [[1 5 3]
#  [2 3 6]
#  [3 1 2]]
# None
# 6
# 1
# [[3 4 5]]