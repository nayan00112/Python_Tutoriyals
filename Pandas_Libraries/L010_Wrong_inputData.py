# Pandas - Cleaning Data of Wrong Format



# ===========================================================
## ERROR NOT WORKING ? WHY  ?
#  https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
# ===========================================================






# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# Convert Into a Correct Format

# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:

from pandas import *

a = read_csv(r'Libraries\files\data4.csv')

print("origonal csv file")
print(a)

# origonal csv file
#     Duration          Date  Pulse  Maxpulse  Calories
# 0         60  '2020/12/01'    110       130     409.1
# 1         60  '2020/12/02'    117       145     479.0
# 2         60  '2020/12/03'    103       135     340.0
# 3         45  '2020/12/04'    109       175     282.4
# 4         45  '2020/12/05'    117       148     406.0
# 5         60  '2020/12/06'    102       127     300.0     
# 6         60  '2020/12/07'    110       136     374.0     
# 7        450  '2020/12/08'    104       134     253.3     
# 8         30  '2020/12/09'    109       133     195.1     
# 9         60  '2020/12/10'     98       124     269.0     
# 10        60  '2020/12/11'    103       147     329.3     
# 11        60  '2020/12/12'    100       120     250.7     
# 12        60  '2020/12/12'    100       120     250.7     
# 13        60  '2020/12/13'    106       128     345.3     
# 14        60  '2020/12/14'    104       132     379.3     
# 15        60  '2020/12/15'     98       123     275.0     
# 16        60  '2020/12/16'     98       120     215.2     
# 17        60  '2020/12/17'    100       120     300.0     
# 18        45  '2020/12/18'     90       112       NaN     
# 19        60  '2020/12/19'    103       123     323.0     
# 20        45  '2020/12/20'     97       125     243.0     
# 21        60  '2020/12/21'    108       131     364.2     
# 22        45           NaN    100       119     282.0     
# 23        60  '2020/12/23'    130       101     300.0     
# 24        45  '2020/12/24'    105       132     246.0     
# 25        60  '2020/12/25'    102       126     334.5     
# 26        60      20201226    100       120     250.0     
# 27        60  '2020/12/27'     92       118     241.0     
# 28        60  '2020/12/28'    103       132       NaN     
# 29        60  '2020/12/29'    100       132     280.0     
# 30        60  '2020/12/30'    102       129     380.3     
# 31        60  '2020/12/31'     92       115     243.0 


print("After Fixed Data")
a = read_csv(r'Libraries\files\data4.csv')
print(a["Data"])
# # df1['Date'] = to_datetime(df1['Date'])
# df1['Date'] = to_datetime(df1['Date'])
# print(df.to_string())
 

# ===========================================================
 ## ERROR NOT WORKING ? WHY  ?
#  https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
# ===========================================================
