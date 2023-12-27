# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.

# The head() method returns the headers and a specified number of rows, starting from the top.

from pandas import *

df = read_csv(r'Libraries\files\largdata.csv')

print(df.head(10))

#    Index  Organization Id  ...                         Industry Number of employees
# 0      1  E84A904909dF528  ...                Online Publishing                6852
# 1      2  AAC4f9aBF86EAeF  ...                  Import / Export                7994
# 2      3  ad2eb3C8C24DB87  ...                Apparel / Fashion                5105
# 3      4  D76BB12E5eE165B  ...                            Dairy                9069
# 4      5  2F31EddF2Db9aAE  ...            Management Consulting                6991
# 5      6  6774DC1dB00BD11  ...               Mental Health Care                3503
# 6      7  116B5cD4eE1fAAc  ...                Computer Hardware                2762
# 7      8  AB2eA15d98b6BD4  ...                  Performing Arts                7020
# 8      9  0c6D831e8DceCfE  ...  Marketing / Advertising / Sales                2709
# 9     10  9ABE0c8aee135d6  ...     Investment Banking / Venture                5731

# [10 rows x 9 columns]


# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head())
#  Index  ... Number of employees    
# 0      1  ...                6852    
# 1      2  ...                7994    
# 2      3  ...                5105    
# 3      4  ...                9069    
# 4      5  ...                6991    

# [5 rows x 9 columns]

# There is also a tail() method for viewing the last rows of the DataFrame.

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.tail())
#      Index  ... Number of employees
# 114    115  ...                7209  
# 115    116  ...                4998  
# 116    117  ...                5726  
# 117    118  ...                7152  
# 118    119  ...                1202  

# [5 rows x 9 columns]

print(df.tail(10))
#      Index  ... Number of employees
# 109    110  ...                6397  
# 110    111  ...                1839  
# 111    112  ...                2059  
# 112    113  ...                1126  
# 113    114  ...                3806  
# 114    115  ...                7209  
# 115    116  ...                4998  
# 116    117  ...                5726  
# 117    118  ...                7152  
# 118    119  ...                1202  

# [10 rows x 9 columns]

# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.

print(df.info())
# <class 'pandas.core.frame.DataFrame'>RangeIndex: 119 entries, 0 to 118
# Data columns (total 9 columns):
#  #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   Index                119 non-null    int64
#  1   Organization Id      119 non-null    object
#  2   Name                 119 non-null    object
#  3   Website              119 non-null    object
#  4   Country              119 non-null    object
#  5   Description          119 non-null    object
#  6   Founded              119 non-null    int64
#  7   Industry             119 non-null    object
#  8   Number of employees  119 non-null    int64
# dtypes: int64(3), object(6)
# memory usage: 8.5+ KB
# None

d = read_csv(r'Libraries\files\data2.csv')

print(d)
#     Index  Organization Id                       Name
# 0       1  FAB0d41d5b5d22c                Ferrell LLC 
# 1       2              NaN    Mckinney, Riley and Day 
# 2       3  0bFED1ADAE4bcC1                 Hester Ltd 
# 3       4  2bFC1Be8a4ce42f             Holder-Sellers 
# 4       5  9eE8A6a4Eb96C24                        NaN 
# 5       6  cC757116fe1C085             Henry-Thompson 
# 6       7  219233e8aFF1BC3             Hansen-Everett 
# 7       8  ccc93DCF81a31CD              Mcintosh-Mora 
# 8       9  0B4F93aA06ED03e                   Carr Inc 
# 9      10  738b5aDe6B1C6A5                 Gaines Inc 
# 10     11  AE61b8Ffebbc476                 Kidd Group 
# 11     12              NaN               Crane-Clarke 
# 12     13  8D0c29189C9798B   Keller, Campos and Black 
# 13     14  D2c91cc03CA394c                Glover-Pope 
# 14     15  C8AC1eaf9C036F4             Pacheco-Spears 
# 15     16  b5D10A14f7a8AfE                Hodge-Ayers 
# 16     17  68139b5C4De03B4  Bowers, Guerra and Krause 
# 17     18  5c2EffEfdba2BdF                        NaN 
# 18     19              NaN                Branch-Mann 
# 19     20  c1Ce9B350BAc66b             Weiss and Sons 

print(d.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 3 columns):
#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   Index            20 non-null     int64
#  1   Organization Id  17 non-null     object
#  2   Name             18 non-null     object
# dtypes: int64(1), object(2)
# memory usage: 608.0+ bytes
# None



# Result Explained

# The result tells us there are 20 rows and 3 columns:
# RangeIndex: 20 entries, 0 to 19
# Data columns (total 3 columns):


# And the name of each column, with the data type:

#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   Index            20 non-null     int64
#  1   Organization Id  17 non-null     object
#  2   Name             18 non-null     object

# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.
