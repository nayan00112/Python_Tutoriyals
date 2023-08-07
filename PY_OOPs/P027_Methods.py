# Instances methods
# Class method
# Static methods


class Student:
    school = "R. P. Patel School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def displayName(self):
        print(self.name)

    # Static method
    @staticmethod
    def info():
        print("This is for students only.")

    # Class method
    @classmethod #compulsory
    def dispSchoolName(cls):
        print("School name is " + cls.school + ".")


s1 = Student("Mitul", 13)
s2 = Student("Rajesh", 14)

s1.displayName()

Student.info()

Student.dispSchoolName()

# Output
# Mitul
# This is for students only.
# School name is R. P. Patel School.
