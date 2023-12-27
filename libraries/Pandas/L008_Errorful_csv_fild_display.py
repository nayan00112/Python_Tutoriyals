from pandas import *

d = read_csv(r"E:\pythonTutoriyals\Libraries\files\errorfullcsvfile.csv")

print(d)
#               name               email  subjects
# 0            nayan  nayan123@gmail.com   physics
# 1            rudra  rudra123@gmail.com     maths
# 2            mohit                 NaN     maths
# 3  rahulr@.c.maths                 NaN       NaN
# 4  rahulr@.c.maths                 NaN       NaN
# 5           chirag    chirag1@gail.com       NaN
# 6             deep           deep2@g.c  gujarati

print(d.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7 entries, 0 to 6
# Data columns (total 3 columns):
#  #   Column    Non-Null Count  Dtype 
# ---  ------    --------------  ----- 
#  0   name      7 non-null      object
#  1   email     4 non-null      object
#  2   subjects  4 non-null      object
# dtypes: object(3)
# memory usage: 296.0+ bytes
# None
