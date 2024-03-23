# class MyStr:
#     def __init__(self, str):
#         self.str = str
#     def __str__(self): # Magic Method
#         return self.strLength()
#     def strLength(self):
#         return ""+str(len(self.str))

# in short code:
class MyStr:
    def __init__(self, str):
        self.str = str
    def __str__(self): # Magic Method
        return str(len(self.str))


if __name__ == "__main__":
    str1 = MyStr("Hello, From main page")
    print("This is from __main__: ", str1)

str_for_every_time = MyStr("This is call every time if this file call")
print("This is from independent file not in main: ", str_for_every_time)


# Output:
# This is from __main__:  21
# This is from independent file not in main:  41


# In Python, `if __name__ == '__main__':` is a common 
# conditional statement used to control the execution of 
# code when a Python script is run directly. 

# Here's what it means:

# - `__name__` is a special built-in variable in Python.
#  When Python runs a script, it sets the `__name__` variable 
# for that script.
# - If the Python interpreter is running that script as 
# the main program, it sets the `__name__` variable for 
# that script to `'__main__'`.
# - If the script is imported as a 
# module into another 
# script, the `__name__` variable is set to the name of 
# the script/module.

# So, `if __name__ == '__main__':` checks if the script 
# is being run directly by the Python interpreter as the 
# main program. If it is, the code block following this 
# condition will be executed. This is often used to include 
# code that should only run when the script is executed directly, 
# and not when it is imported as a module into another script.