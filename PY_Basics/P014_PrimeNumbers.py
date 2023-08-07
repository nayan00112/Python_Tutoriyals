import math as m

num1 = int(input("Enter the number:"))

for i in range(2, m.ceil(m.pow(num1, 0.5))):
    if num1 % i == 0:
        print("Non Prime")
        break
else:
    print("Prime")

# Output:
# Enter the number:78
# Non Prime

# Enter the number:7 
# Prime