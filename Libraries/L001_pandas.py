from pandas import *

df = read_csv(r'E:\pythonTutoriyals\Libraries\files\T001_csvfile.csv')

print("read_csv in pandas")
print(df.to_string())
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


