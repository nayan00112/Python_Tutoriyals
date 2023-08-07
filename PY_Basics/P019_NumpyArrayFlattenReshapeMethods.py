from numpy import *

ar = array([
    [2,3,4,5,6,7],
    [6,4,3,6,8,0]
])

print(ar)
a1 = ar.flatten()
a2 =ar.reshape(2,2,3)

print(a1)
print(a2)

# Output:
# [[2 3 4 5 6 7]
#  [6 4 3 6 8 0]]
# [2 3 4 5 6 7 6 4 3 6 8 0]
# [[[2 3 4]
#   [5 6 7]]

#  [[6 4 3]
#   [6 8 0]]]