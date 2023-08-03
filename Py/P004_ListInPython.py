students = ["Nayan", "Marmik", "Jignesh" ,"Rudra"]
print(students)

students.append("Dharm")
print(students)

students.sort()
print(students)

students.reverse()
print(students)

print(students.index("Nayan"))

students.reverse()
students.append("Parth")
print(students.pop())

students.clear()
print(students)


# Output:
# ['Nayan', 'Marmik', 'Jignesh', 'Rudra']
# ['Nayan', 'Marmik', 'Jignesh', 'Rudra', 'Dharm']
# ['Dharm', 'Jignesh', 'Marmik', 'Nayan', 'Rudra']
# ['Rudra', 'Nayan', 'Marmik', 'Jignesh', 'Dharm']
# 1
# Parth
# []