x = 0
while x < 5:
    print(x)
    x += 1

print("===================")

x = 3

while x != 12:
    if x%2 == 0:
        print(x)
    else:
        pass
    x += 1

print("===================")

li = ["apple", "banana", 45, "cat", "dog", 34, "3", True]

for i in li:
    print(i)

print("===================")

for i in range(5):
    print(i)


print("===================")


for i in range(4, 10):
    print(i)


print("===================")

for i in range(4, 20, 3):
    print(i)


print("===================")

dic = {
    "a":"Arjit",
    "b":"Bharat",
    "c":"Chetan",
    "d":"Deepak"
}

for k in dic:
    print(k)
    print(dic[k])


print("===================")


for i in range(4, 10):
    if i == 8:
        break
    print(i)

# Output
# 0
# 1
# 2
# 3
# 4
# ===================
# 4
# 6
# 8
# 10
# ===================
# apple
# banana
# 45
# cat
# dog
# 34
# 3
# True
# ===================
# 0
# 1
# 2
# 3
# 4
# ===================
# 4
# 5
# 6
# 7
# 8
# 9
# ===================
# 4
# 7
# 10
# 13
# 16
# 19
# ===================
# a
# Arjit
# b
# Bharat
# c
# Chetan
# d
# Deepak
# ===================
# 4
# 5
# 6
# 7