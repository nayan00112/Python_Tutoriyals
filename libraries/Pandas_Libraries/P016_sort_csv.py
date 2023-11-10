from pandas import *

b  = read_csv("Pandas_Libraries\column_copy.csv")

print(b)
#    c1   c2   c3  c4
# 0   1  231  344  45
# 1  54  613   47  48
# 2  94  140   11  12
# 3  14   15   16  17


print(b.sort_values(by=["c2"]))
#    c1   c2   c3  c4
# 3  14   15   16  17
# 2  94  140   11  12
# 0   1  231  344  45
# 1  54  613   47  48


print(b.sort_index())
#    c1   c2   c3  c4
# 0   1  231  344  45
# 1  54  613   47  48
# 2  94  140   11  12
# 3  14   15   16  17