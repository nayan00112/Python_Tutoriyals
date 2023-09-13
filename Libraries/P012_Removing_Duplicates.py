# Pandas - Removing Duplicates

# Discovering Duplicates
# Duplicate rows are rows that have been registered more than one time.

from pandas import *
a = read_csv(r"Libraries\files\data6.csv")

# To discover duplicates, we can use the duplicated() method.

# The duplicated() method returns a Boolean values for each row:

# ExampleGet your own Python Server
# Returns True for every row that is a duplicate, othwerwise False:

print(a.duplicated())

# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5    False
# 6    False
# 7     True
# 8    False
# dtype: bool


# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.

# Example
# Remove all duplicates:

a.drop_duplicates(inplace=True)
print(a.duplicated())
# 0    False
# 1    False
# 3    False
# 4    False
# 5    False
# 6    False
# 8    False
# dtype: bool