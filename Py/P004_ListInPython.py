students = ["Nayan", "Marmik", "Jignesh" ,"Rudra"]
print(students)
print(type(students))

students.append("Dharm")
print(students)

students.sort()
print(students)

students.reverse()
print(students)

print(students.index("Nayan"))

students.reverse()

students.append("Parth")
print(students)

print(students.pop())
print(students)
students.clear()
print(students)


# Output:
# ['Nayan', 'Marmik', 'Jignesh', 'Rudra']
# <class 'list'>
# ['Nayan', 'Marmik', 'Jignesh', 'Rudra', 'Dharm']
# ['Dharm', 'Jignesh', 'Marmik', 'Nayan', 'Rudra']
# ['Rudra', 'Nayan', 'Marmik', 'Jignesh', 'Dharm']
# 1
# ['Dharm', 'Jignesh', 'Marmik', 'Nayan', 'Rudra', 'Parth']
# Parth
# ['Dharm', 'Jignesh', 'Marmik', 'Nayan', 'Rudra']
# []