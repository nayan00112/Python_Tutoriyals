print("=========== Arithmatic Operators ===========")
print(16 + 4)
print(16 - 4)
print(16 * 4)
print(16 / 4)
print(16 // 4)
print(17 % 4)
print(16 ** 4)
print(4 + 3 * 2)
print((4 + 3) * 2)
print(4.33 + 3.64 - 2.35)

print("=========== Relational Operators ===========")
print(1 < 5)
print(3 > 5)
print(4 > 4)
print(4 < 4)
print(4 >= 4)
print(4 <= 4)
print(6 != 3)
print(6 == 3)
print(6 != 6)
print(6 == 6)

print("=========== Logical Operators ===========")
print("----- AND -----")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("----- OR -----")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("----- NOT -----")
print(not True)
print(not False)

print("=========== Bitwise Operators ===========")
print(12>>2)
print(12<<2)
print(~10)
print(12 & 4)
print(12 | 4)
print(21^3) # xor

print("=========== Identity Operators ===========")
print("FOR LIST")
x = ["apple", "mango"]
y = ["apple", "mango"]

print(x is y)
print(x is not y)

x = y

print(x is y)
print(x is not y)

print("FOR NORMAL VARIABLE")
x = 4
y = 4

print(x is y)
print(x is not y)

x = y

print(x is y)
print(x is not y)


print("=========== Membership Operators ===========")
laptopComp = ["Macbook", "ASUS", "DELL", "LENOVO", "HP"]

print("ASUS" in laptopComp)
print("Realme" in laptopComp)


print("ASUS" not in laptopComp)
print("Realme" not in laptopComp)



# Output:
# =========== Arithmatic Operators ===========
# 20
# 12
# 64
# 4.0
# 4
# 1
# 65536
# 10
# 14
# 5.620000000000001
# =========== Relational Operators ===========
# True
# False
# False
# False
# True
# True
# True
# False
# False
# True
# =========== Logical Operators ===========
# ----- AND -----
# True
# False
# False
# False
# ----- OR -----
# True
# True
# True
# False
# ----- NOT -----
# False
# True
# =========== Bitwise Operators ===========
# 3
# 48
# -11
# 4
# 12
# 22
# =========== Identity Operators ===========
# FOR LIST
# False
# True
# True
# False
# FOR NORMAL VARIABLE
# True
# False
# True
# False
# =========== Membership Operators ===========
# True
# False
# False
# True