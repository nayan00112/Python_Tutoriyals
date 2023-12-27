from pandas import *
# What is a Series?
# A Pandas Series is like a column in a table.

# It is a "one-dimensional" array holding data of any type.

l = ["nayan", "jignesh", "monik", "om"]

print()
print("Series function in pandas")
print(Series(l))
# Series function in pandas
# 0      nayan
# 1    jignesh
# 2      monik
# 3         om
# dtype: object

myvar = Series(l)
print(myvar)
# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.
print(myvar[1])
# 0      nayan
# 1    jignesh
# 2      monik
# 3         om
# dtype: object
# jignesh

# Create Labels
# With the index argument, you can name your own labels.

l = ["mango", "123", 346, "cat", "dog"]
index = ['i', 'ii', 'iii', 'vi', 'v']
a = Series(l, index=index)
print(a)
# i      mango
# ii       123
# iii      346
# vi       cat
# v        dog
# dtype: object
print(a["iii"])
# 346

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.
dic = {"a": "apple", "b": "banana", "c": "cat", "d": "dog"}
print(Series(dic["b"]))
# 0    banana

t = Series(dic)
print(t)
print(type(t))
# print(t[0]) #wired output!
print(t["d"])
# dtype: object
# a     apple
# b    banana
# c       cat
# d       dog
# dtype: object
# <class 'pandas.core.series.Series'>
# dog

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

abc = {'day1': 432, "day2": 453, "day3": 411}

t = Series(abc, index=["day1", "day3"])
print(t)
# day1    432
# day3    411
# dtype: int64
