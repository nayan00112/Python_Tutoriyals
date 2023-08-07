class Student:
    # class variable
    schoolname = "R. P. Patel School"
    # class variable is like static variable.

    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


s1 = Student("Rahul", 16)
s2 = Student("Mitesh", 17)

s1.display()
s2.display()

print(s1.schoolname)
print(s2.schoolname)
print(Student.schoolname)

Student.schoolname = "RPPatel School"  # change for all objects.

print(s1.schoolname)
print(s2.schoolname)
print(Student.schoolname)

s1.schoolname = "rppatel"  # change only for itself

print(s1.schoolname)
print(s2.schoolname)
print(Student.schoolname)
