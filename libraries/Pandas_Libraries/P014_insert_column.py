# INSERT COLUMN IN EXISTING METHOD

from pandas import *

a = read_csv("Pandas_Libraries\column.csv")
print(a)
#    c1  c2  c3  c4
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  14  15  16  17


a["newColumn"] = [9, 8, 6, 5]
print(a)
#    c1  c2  c3  c4  newColumn
# 0   1   2   3   4          9
# 1   5   6   7   8          8
# 2   9  10  11  12          6
# 3  14  15  16  17          5


# USING INSERT METHOD

b = read_csv("Pandas_Libraries\column.csv")
print(b)
#    c1  c2  c3  c4
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  14  15  16  17

b.insert(loc=2, column="MyColumn", value=[2,2,1,1])
print(b)
#    c1  c2  MyColumn  c3  c4
# 0   1   2         2   3   4
# 1   5   6         2   7   8
# 2   9  10         1  11  12
# 3  14  15         1  16  17