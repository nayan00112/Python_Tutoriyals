from numpy import *
# 2D Array
arr1 = array([[1, 2, 3], [5, 6, 7]])

print(arr1)
print(size(arr1))

for i in arr1:
    for j in i:
        print(j, end=" ")
    print()
arr2 = array([[5, 2, 8], [4, 3, 5]])

print("arr1 + arr2 is: \n", (arr1 + arr2))


print("Simple multiplication is (arr1 * arr2): \n", (arr1 * arr2))

# Output
# [[1 2 3]
#  [5 6 7]]
# 6
# 1 2 3
# 5 6 7
# arr1 + arr2 is:
#  [[ 6  4 11]
#  [ 9  9 12]]
# Simple multiplication is (arr1 * arr2):
#  [[ 5  4 24]
#  [20 18 35]]


#Matrix is in next file.