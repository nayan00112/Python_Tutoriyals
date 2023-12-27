from pandas import *

# Pandas - Cleaning Empty Cells
# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.

# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# Example:
# Return a new Data Frame with no empty cells:

df = read_csv(r"Libraries\files\errorfullcsvfile.csv")
print("Orignal csv file: ")
print(df)
# Orignal csv file:
#               name               email  subjects
# 0            nayan  nayan123@gmail.com   physics
# 1            rudra  rudra123@gmail.com     maths
# 2            mohit                 NaN     maths
# 3  rahulr@.c.maths                 NaN       NaN
# 4  rahulr@.c.maths                 NaN       NaN
# 5           chirag    chirag1@gail.com       NaN
# 6             deep           deep2@g.c  gujarati

new_df = df.dropna()
print(" new Data Frame with no empty cells:")
print(new_df)
#  new Data Frame with no empty cells:
#     name               email  subjects
# 0  nayan  nayan123@gmail.com   physics
# 1  rudra  rudra123@gmail.com     maths
# 6   deep           deep2@g.c  gujarati

#  Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:


# If you want to change the original DataFrame (NOT IN ORIGNAL FILE BUT DATAFRAM OBJECTS, HERE IT IS "df"), use the inplace = True argument:

# Example
# Remove all rows with NULL values:


df = read_csv(r"Libraries\files\errorfullcsvfile_copy.csv")
print("Orignal csv file: ")
print(df)
# Orignal csv file:
#               name               email  subjects
# 0            nayan  nayan123@gmail.com   physics
# 1            rudra  rudra123@gmail.com     maths
# 2            mohit                 NaN     maths
# 3  rahulr@.c.maths                 NaN       NaN
# 4  rahulr@.c.maths                 NaN       NaN
# 5           chirag    chirag1@gail.com       NaN
# 6             deep           deep2@g.c  gujarati

df.dropna(inplace=True)
print("after removing all rows whit NULL values: (also update in orignal DataFram object, NOT in Actual file.)")
print(df)
# after removing all rows whit NULL values:
#     name               email  subjects
# 0  nayan  nayan123@gmail.com   physics
# 1  rudra  rudra123@gmail.com     maths
# 6   deep           deep2@g.c  gujarati

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

obj = read_csv(r"Libraries\files\errorfullcsvfile.csv")
obj.fillna("Unknown", inplace=True)

print(obj)
#               name               email  subjects
# 0            nayan  nayan123@gmail.com   physics
# 1            rudra  rudra123@gmail.com     maths
# 2            mohit             Unknown     maths
# 3  rahulr@.c.maths             Unknown   Unknown
# 4  rahulr@.c.maths             Unknown   Unknown
# 5           chirag    chirag1@gail.com   Unknown
# 6             deep           deep2@g.c  gujarati

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.

# To only replace empty values for one column, specify the column name for the DataFrame:


obj = read_csv(r"Libraries\files\errorfullcsvfile.csv")
obj["subjects"].fillna("Hindi", inplace=True)
# let by default subject is Hindi.

print(obj)
#               name               email  subjects
# 0            nayan  nayan123@gmail.com   physics
# 1            rudra  rudra123@gmail.com     maths
# 2            mohit                 NaN     maths
# 3  rahulr@.c.maths                 NaN     Hindi
# 4  rahulr@.c.maths                 NaN     Hindi
# 5           chirag    chirag1@gail.com     Hindi
# 6             deep           deep2@g.c  gujarati


# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Mean = the average value (the sum of all values divided by number of values).

# display data:
project = read_csv(r'Libraries\files\data3.csv')
print("Orognal Data")
print(project.to_string())
print("Max of input: " + str(project['input'].dropna().max()))
print("Min of input: " + str(project['input'].dropna().min()))
print("Mean of output: " + str(project['output'].dropna().mean()))
print("Median of output: " + str(project['output'].dropna().median()))
# Orognal Data
#       Title  input  output
# 0  project1     12    34.0
# 1  project2     32    34.0
# 2  project3     69    37.0
# 3  project4     54     NaN
# 4  project5     41    35.0
# 5  project6     67     NaN
# 6  project7     45    33.0
# 7  project8     11    38.0
# Max of input: 69
# Min of input: 11
# Mean of output: 35.166666666666664
# Median of output: 34.5

# Example
# Calculate the MEDIAN, and replace any empty values with it:

c = project["output"].median()
print("median is: "+str(c))
project.fillna(c, inplace=True)
print(project)
# median is: 34.5
#       Title  input  output
# 0  project1     12    34.0
# 1  project2     32    34.0
# 2  project3     69    37.0
# 3  project4     54    34.5
# 4  project5     41    35.0
# 5  project6     67    34.5
# 6  project7     45    33.0
# 7  project8     11    38.0

print("mode of data is:" + str(project['output'].median()))
# mode of data is:34.5

print(project.count())
# Title     8
# input     8
# output    8
# dtype: int64