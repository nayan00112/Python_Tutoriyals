from pandas import *

# DataFrames

# Data sets in Pandas are usually "multi-dimensional" tables, called DataFrames.
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# Series is like a column, a DataFrame is the whole table.

datas = {
    "Name": ["Nayan", "Jignesh", "Rudra", "Om"],
    "Roll_Num": [12, 14, 15, 16],
    "Email": ["Nayan123@gmail.com", "Jignesh123@gmail.com", "Rudra123@gmail.com", "Om123@gmail.com"],
}

print(DataFrame(datas))
#       Name  Roll_Num                 Email  
# 0    Nayan        12    Nayan123@gmail.com  
# 1  Jignesh        14  Jignesh123@gmail.com  
# 2    Rudra        15    Rudra123@gmail.com  
# 3       Om        16       Om123@gmail.com 

t = DataFrame(datas)
print(type(t))
# <class 'pandas.core.frame.DataFrame'>

# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)

# Insert the correct syntax to return the first row of a DataFrame.
print(t.loc[0])
# Name                     Nayan
# Roll_Num                    12
# Email       Nayan123@gmail.com
# Name: 0, dtype: object

# Note: This example returns a Pandas Series.

# Insert the correct syntax to return the second row of a DataFrame.
print(t.loc[1])
# Name                     Jignesh
# Roll_Num                      14
# Email       Jignesh123@gmail.com
# Name: 1, dtype: object

# Insert the correct syntax to return the third row of a DataFrame.
print(t.loc[2])
# Name                     Rudra
# Roll_Num                    15
# Email       Rudra123@gmail.com
# Name: 2, dtype: object

#use a list of indexes:
# Note: When using [], the result is a Pandas DataFrame.
print(t.loc[[0,1]])
#       Name  ...                 Email
# 0    Nayan  ...    Nayan123@gmail.com
# 1  Jignesh  ...  Jignesh123@gmail.com

# [2 rows x 3 columns]

# Insert the correct syntax to return the entire DataFrame.
print(t.to_string())

t1 = t.to_string()
print(type(t1))
# <class 'str'>
print(t1)
#       Name  Roll_Num                 Email
# 0    Nayan        12    Nayan123@gmail.com
# 1  Jignesh        14  Jignesh123@gmail.com
# 2    Rudra        15    Rudra123@gmail.com
# 3       Om        16       Om123@gmail.com


# Named Indexes
# With the index argument, you can name your own indexes.

df = DataFrame(datas, index=["I", "II", "III", "VI"])
print(df)
#         Name  Roll_Num                 Email
# I      Nayan        12    Nayan123@gmail.com
# II   Jignesh        14  Jignesh123@gmail.com
# III    Rudra        15    Rudra123@gmail.com
# VI        Om        16       Om123@gmail.com

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).

print(df.loc["II"])
# Name                     Jignesh
# Roll_Num                      14
# Email       Jignesh123@gmail.com
# Name: II, dtype: object


# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

my_csv_file = read_csv(r"E:\pythonTutoriyals\Libraries\files\T001_csvfile.csv")
'''
In Python, the 'r' before a string literal indicates a raw string literal. It tells Python interpreter to treat backslashes (\) as literal characters, rather than as escape characters.

For example, in Windows file paths, backslashes are used as directory separators, like in your example: `r"E:\pythonTutoriyals\Libraries\files\T001_csvfile.csv"`. Without the 'r' prefix, Python would interpret the backslashes as escape characters. However, by prefixing the string with 'r', you're telling Python to treat it as a raw string, so the backslashes are not escaped.

In the context of your code snippet, `read_csv(r"E:\pythonTutoriyals\Libraries\files\T001_csvfile.csv")`, it's being used to specify the file path to the CSV file you want to read using pandas' `read_csv` function.
'''
print(my_csv_file)
#       Name   Roll Number                  Email  Date of Birth
# 0    Nayan            12      nayan12@gmail.com     14/06/2003
# 1  Jignesh            23   Jignesh_23@gmail.com     28/07/2003
# 2      Raj            43       Raj_43@gmail.com     05/02/2003
# 3    Tarun            13     Tarun_13@gmail.com     03/05/2004
# 4   Rajesh            56    Rajesh_56@gmail.com     16/03/2004
# 5    Kanak            28     Kanak_28@gmail.com     18/01/2003
# 6   Jaimin            46    Jaimin_46@gmail.com     26/06/2004
# 7     Udit            67      Udit_67@gmail.com     17/02/2003
# 8   Pratik            11    Pratik_11@gmail.com     01/01/2003
# 9   Naitik             5    Naitik_05@gmail.com     05/12/2004

print(type(my_csv_file))
# <class 'pandas.core.frame.DataFrame'>

