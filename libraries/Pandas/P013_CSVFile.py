# CREATE CSV FILE FROM DICTIONARTY

from pandas import *

# create csv file

d = {
    "Name": ["nayan", "jignesh", "raj", "monik", "om"],
    "rollNumber" : [21, 32, 22, 53, 56],
    "subject" : ["physics", "maths", "gujarati", "hindi", "maths"]
}

df = DataFrame(d)

print(df)
#       Name  rollNumber   subject
# 0    nayan          21   physics
# 1  jignesh          32     maths
# 2      raj          22  gujarati
# 3    monik          53     hindi
# 4       om          56     maths

a = df.to_csv()

f = open("Pandas_Libraries/my_csv_create.csv", "w")
f.write(a)
f.close()

f = open("Pandas_Libraries/my_csv_create.csv", "r")
print(f.read())
# ,Name,rollNumber,subject

# 0,nayan,21,physics

# 1,jignesh,32,maths

# 2,raj,22,gujarati

# 3,monik,53,hindi

# 4,om,56,maths

f.close()

d = read_csv("Pandas_Libraries/my_csv_create.csv")
print(d)
#    Unnamed: 0     Name  rollNumber   subject
# 0           0    nayan          21   physics
# 1           1  jignesh          32     maths
# 2           2      raj          22  gujarati
# 3           3    monik          53     hindi
# 4           4       om          56     maths

