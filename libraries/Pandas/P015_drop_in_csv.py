from pandas import *

a = read_csv("Pandas_Libraries\column.csv")

print(a)
print("--------------------------------------")
print(a.drop(columns=['c2','c4']))
print("--------------------------------------")
print(a)

#    c1  c2  c3  c4
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  14  15  16  17
# --------------------------------------
#    c1  c3
# 0   1   3
# 1   5   7
# 2   9  11
# 3  14  16
# --------------------------------------
#    c1  c2  c3  c4
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  14  15  16  17


a.drop(columns=['c2','c4'], inplace=True)

print(a)
#    c1  c3
# 0   1   3
# 1   5   7
# 2   9  11
# 3  14  16


print("==================================")
b  = read_csv("Pandas_Libraries\column.csv")

print(b)
# ==================================
#    c1  c2  c3  c4
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  14  15  16  17

# b.drop(b.loc[:,1:3], inplace=True, axis=1)
# print(b)
