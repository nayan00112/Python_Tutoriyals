# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).

# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

# In our examples we will be using a CSV file called 'data.csv'.

import pandas as pd

df = pd.read_csv("Libraries/files/data.csv")

print(df)
print() # new line
print(df.to_string())
print() # new line
print(type(df))
print() # new line
print(type(df.to_string()))

#     Index  Organization Id                       Name
# 0       1  FAB0d41d5b5d22c                Ferrell LLC
# 1       2  6A7EdDEA9FaDC52    Mckinney, Riley and Day
# 2       3  0bFED1ADAE4bcC1                 Hester Ltd
# 3       4  2bFC1Be8a4ce42f             Holder-Sellers
# 4       5  9eE8A6a4Eb96C24                Mayer Group
# 5       6  cC757116fe1C085             Henry-Thompson
# 6       7  219233e8aFF1BC3             Hansen-Everett
# 7       8  ccc93DCF81a31CD              Mcintosh-Mora
# 8       9  0B4F93aA06ED03e                   Carr Inc
# 9      10  738b5aDe6B1C6A5                 Gaines Inc
# 10     11  AE61b8Ffebbc476                 Kidd Group
# 11     12  eb3B7D06cCdD609               Crane-Clarke
# 12     13  8D0c29189C9798B   Keller, Campos and Black
# 13     14  D2c91cc03CA394c                Glover-Pope
# 14     15  C8AC1eaf9C036F4             Pacheco-Spears
# 15     16  b5D10A14f7a8AfE                Hodge-Ayers
# 16     17  68139b5C4De03B4  Bowers, Guerra and Krause
# 17     18  5c2EffEfdba2BdF            Mckenzie-Melton
# 18     19  ba179F19F7925f5                Branch-Mann
# 19     20  c1Ce9B350BAc66b             Weiss and Sons

#     Index  Organization Id                       Name
# 0       1  FAB0d41d5b5d22c                Ferrell LLC
# 1       2  6A7EdDEA9FaDC52    Mckinney, Riley and Day
# 2       3  0bFED1ADAE4bcC1                 Hester Ltd
# 3       4  2bFC1Be8a4ce42f             Holder-Sellers
# 4       5  9eE8A6a4Eb96C24                Mayer Group
# 5       6  cC757116fe1C085             Henry-Thompson
# 6       7  219233e8aFF1BC3             Hansen-Everett
# 7       8  ccc93DCF81a31CD              Mcintosh-Mora
# 8       9  0B4F93aA06ED03e                   Carr Inc
# 9      10  738b5aDe6B1C6A5                 Gaines Inc
# 10     11  AE61b8Ffebbc476                 Kidd Group
# 11     12  eb3B7D06cCdD609               Crane-Clarke
# 12     13  8D0c29189C9798B   Keller, Campos and Black
# 13     14  D2c91cc03CA394c                Glover-Pope
# 14     15  C8AC1eaf9C036F4             Pacheco-Spears
# 15     16  b5D10A14f7a8AfE                Hodge-Ayers
# 16     17  68139b5C4De03B4  Bowers, Guerra and Krause
# 17     18  5c2EffEfdba2BdF            Mckenzie-Melton
# 18     19  ba179F19F7925f5                Branch-Mann
# 19     20  c1Ce9B350BAc66b             Weiss and Sons

# <class 'pandas.core.frame.DataFrame'>

# <class 'str'>


# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

ldf = pd.read_csv(r"Libraries\files\largdata.csv")

print(ldf)

#      Index  ... Number of employees
# 0        1  ...                6852
# 1        2  ...                7994
# 2        3  ...                5105
# 3        4  ...                9069
# 4        5  ...                6991
# ..     ...  ...                 ...
# 114    115  ...                7209
# 115    116  ...                4998
# 116    117  ...                5726
# 117    118  ...                7152
# 118    119  ...                1202

# [119 rows x 9 columns]


# max_rows
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows with the pd.options.display.max_rows statement.

print(pd.options.display.max_rows)
# 60

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

# You can change the maximum rows number with the same statement.

ldf = pd.read_csv(r"Libraries\files\largdata.csv")

pd.options.display.max_rows=500
# in our case, no. of rows is 119, and 119 < 500 hense, all rows are displayed.

print(ldf)
#      Index  ... Number of employees
# 0        1  ...                6852
# 1        2  ...                7994
# 2        3  ...                5105
# 3        4  ...                9069
# 4        5  ...                6991
# 5        6  ...                3503
# 6        7  ...                2762
# 7        8  ...                7020
# 8        9  ...                2709
# 9       10  ...                5731
# 10      11  ...                2252
# 11      12  ...                6165
# 12      13  ...                 730
# 13      14  ...                9890
# 14      15  ...                8497
# 15      16  ...                5205
# 16      17  ...                6706
# 17      18  ...                 117
# 18      19  ...                6765
# 19      20  ...                5926
# 20      21  ...                5687
# 21      22  ...                9277
# 22      23  ...                8299
# 23      24  ...                7245
# 24      25  ...                7464
# 25      26  ...                2788
# 26      27  ...                3738
# 27      28  ...                8641
# 28      29  ...                2952
# 29      30  ...                1075
# 30      31  ...                2548
# 31      32  ...                  95
# 32      33  ...                8106
# 33      34  ...                2938
# 34      35  ...                9056
# 35      36  ...                8937
# 36      37  ...                3985
# 37      38  ...                7675
# 38      39  ...                9145
# 39      40  ...                1175
# 40      41  ...                6202
# 41      42  ...                7426
# 42      43  ...                2861
# 43      44  ...                2726
# 44      45  ...                4595
# 45      46  ...                4171
# 46      47  ...                 406
# 47      48  ...                 746
# 48      49  ...                8287
# 49      50  ...                4604
# 50      51  ...                8952
# 51      52  ...                 440
# 52      53  ...                5359
# 53      54  ...                7982
# 54      55  ...                1693
# 55      56  ...                5784
# 56      57  ...                7775
# 57      58  ...                6151
# 58      59  ...                9151
# 59      60  ...                  58
# 60      61  ...                9676
# 61      62  ...                9431
# 62      63  ...                4941
# 63      64  ...                 142
# 64      65  ...                1729
# 65      66  ...                1891
# 66      67  ...                8263
# 67      68  ...                3296
# 68      69  ...                4660
# 69      70  ...                8802
# 70      71  ...                5800
# 71      72  ...                7610
# 72      73  ...                4963
# 73      74  ...                8904
# 74      75  ...                5683
# 75      76  ...                5416
# 76      77  ...                4929
# 77      78  ...                2658
# 78      79  ...                 816
# 79      80  ...                4989
# 80      81  ...                3232
# 81      82  ...                6016
# 82      83  ...                 381
# 83      84  ...                4759
# 84      85  ...                3925
# 85      86  ...                2011
# 86      87  ...                7902
# 87      88  ...                9074
# 88      89  ...                5158
# 89      90  ...                9014
# 90      91  ...                2330
# 91      92  ...                4087
# 92      93  ...                5338
# 93      94  ...                7978
# 94      95  ...                2806
# 95      96  ...                2240
# 96      97  ...                9497
# 97      98  ...                4291
# 98      99  ...                7429
# 99     100  ...                4897
# 100    101  ...                3468
# 101    102  ...                3415
# 102    103  ...                8471
# 103    104  ...                6746
# 104    105  ...                6321
# 105    106  ...                1027
# 106    107  ...                9569
# 107    108  ...                8887
# 108    109  ...                5303
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

