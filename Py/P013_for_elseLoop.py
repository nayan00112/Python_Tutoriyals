n = int(input("Enter the number:"))

for i in [4, 2, 1, 5, 6, 21, 44]:
    if i == n:
        print("Exist")
        break #must use break in for else loop.
else:
    print("No Exist")

# Output:
# Enter the number:5
# Exist

# Enter the number:3
# No Exist