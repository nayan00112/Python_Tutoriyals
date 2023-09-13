# Pandas - Fixing Wrong Data

# Wrong Data
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

# in our case, max time is only 60second, but in row 0 and 4, tie is 77 and 84, which are false data.

import pandas as pd

a = pd.read_csv(r"Libraries\files\data5.csv")

# print(a)
#      name  time(second)  maxtime Winner
# 0     raj            77       60     No
# 1     tej            46       60     No
# 2    kunj            56       60     No
# 3   parav            34       60    Yes
# 4     dev            84       60     No
# 5  dinesh            38       60     No
# 6  manana            49       60     No


# for fix it, first look below code:

for r in a:
    print(r)
# name
# time(second)
# maxtime
# Winner

print()
for r in a:
    print(a['name'])
    print(a['time_second'])
    print(a['maxtime'])
    print(a['Winner'])
# 0       raj
# 1       tej
# 2      kunj
# 3     parav
# 4       dev
# 5    dinesh
# 6    manana
# Name: name, dtype: object
# 0    77
# 1    46
# 2    56
# 3    34
# 4    84
# 5    38
# 6    49
# Name: time_second, dtype: int64
# 0    60
# 1    60
# 2    60
# 3    60
# 4    60
# 5    60
# 6    60
# Name: maxtime, dtype: int64
# 0     No
# 1     No
# 2     No
# 3    Yes
# 4     No
# 5     No
# 6     No
# Name: Winner, dtype: object
# 0       raj
# 1       tej
# 2      kunj
# 3     parav
# 4       dev
# 5    dinesh
# 6    manana
# Name: name, dtype: object
# 0    77
# 1    46
# 2    56
# 3    34
# 4    84
# 5    38
# 6    49
# Name: time_second, dtype: int64
# 0    60
# 1    60
# 2    60
# 3    60
# 4    60
# 5    60
# 6    60
# Name: maxtime, dtype: int64
# 0     No
# 1     No
# 2     No
# 3    Yes
# 4     No
# 5     No
# 6     No
# Name: Winner, dtype: object
# 0       raj
# 1       tej
# 2      kunj
# 3     parav
# 4       dev
# 5    dinesh
# 6    manana
# Name: name, dtype: object
# 0    77
# 1    46
# 2    56
# 3    34
# 4    84
# 5    38
# 6    49
# Name: time_second, dtype: int64
# 0    60
# 1    60
# 2    60
# 3    60
# 4    60
# 5    60
# 6    60
# Name: maxtime, dtype: int64
# 0     No
# 1     No
# 2     No
# 3    Yes
# 4     No
# 5     No
# 6     No
# Name: Winner, dtype: object
# 0       raj
# 1       tej
# 2      kunj
# 3     parav
# 4       dev
# 5    dinesh
# 6    manana
# Name: name, dtype: object
# 0    77
# 1    46
# 2    56
# 3    34
# 4    84
# 5    38
# 6    49
# Name: time_second, dtype: int64
# 0    60
# 1    60
# 2    60
# 3    60
# 4    60
# 5    60
# 6    60
# Name: maxtime, dtype: int64
# 0     No
# 1     No
# 2     No
# 3    Yes
# 4     No
# 5     No
# 6     No
# Name: Winner, dtype: object

for r in a.name:
    print(r)
# raj
# tej
# kunj
# parav
# dev
# dinesh
# manana

# now going towards fix it. stape by stape

for r in a.time_second:
    print(r)

# 77
# 46
# 56
# 34
# 84
# 38
# 49

# Lets Fix it finaly..

index = 0
for r in a.time_second:
    if r > 60:
        a.loc[index, "time_second"] = 60
    index += 1

print(a)
#      name  time_second  maxtime Winner
# 0     raj           60       60     No
# 1     tej           46       60     No
# 2    kunj           56       60     No
# 3   parav           34       60    Yes
# 4     dev           60       60     No
# 5  dinesh           38       60     No
# 6  manana           49       60     No

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.

# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

a = pd.read_csv(r"Libraries\files\data5_copy.csv")

index = 0
for r in a.time_second:
    if r > 60:
        a.drop(index, inplace=True)
    index += 1
print(a)
#      name  time_second  maxtime Winner
# 1     tej           46       60     No
# 2    kunj           56       60     No
# 3   parav           34       60    Yes
# 5  dinesh           38       60     No
# 6  manana           49       60     No
