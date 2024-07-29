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




# Instance Method:
# Use: When the method operates on a specific instance of a class.
# Access: Via the self parameter, which refers to the instance.
# Syntax: def method_name(self, ...):

# Class Method:
# Use: When the method operates on the class itself, rather than a specific instance.
# Access: Via the cls parameter, which refers to the class.
# Syntax: @classmethod\ndef method_name(cls, ...):

# Static Method:
# Use: When the method operates on data or utility functions that are not dependent on the instance or the class.
# Access: No special parameters (class or instance).
# Syntax: @staticmethod\ndef method_name(...):


# When to Use Each Method:

# Instance Method:
# Instance initialization and modification
# Accessing instance attributes
# Performing instance-specific calculations or actions

# Class Method:
# Creating new instances of the class (often called factory methods)
# Modifying class-level attributes
# Accessing class-level data

# Static Method:
# Utility methods that operate on data or perform calculations that are independent of the instance or class
# Operations that relate to the class’s purpose but do not modify its state
# Mathematical operations or conversions