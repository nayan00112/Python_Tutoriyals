num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
