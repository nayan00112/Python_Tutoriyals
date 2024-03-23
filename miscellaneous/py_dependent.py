from py_independent import MyStr
str2 = MyStr("this is from dependent string.")
print("From dependent file", str2)

# Output:
# This is from independent file not in main:  41       
# From dependent file 30