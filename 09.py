# Exceptions

"""
An exception is a programm err that happens when somthings goes wrong due to incorrect code or input
"""


"""
This code produce a ZeroDivisionError exception by trying to divide 7 by 0.
"""

#x = 7
#y = 0
#print(x/y)

"""
print(x/y)
ZeroDivisionError: division by zero
"""


"""
There are a lot of different types of exceptions:
    'ImportError': an import fails.
    'IndexError': a list is indexed with an out-of-range number;
    'NameError': an unknown variables is used:
    'SyntaxError': the code can't be parsed properly;
    'TypeError': a function is called on a value of an inappropriate type;
    'ValueError': a function is called on  a value the correct type, but with an inappropriate value.
"""

#_____________________________________________________________

#try/except
"""
The try/except block allows you to handle exceptions.
they try block contains code that might throw an exception.
If that exception occurs, the code in the try block stops, and the cpde in the except block is run.
"""
#for example
x = 7
y = 0
try:
    print(z/y)
except:
    print('An error occured by dividing number zero.')
# output: An error occured by dividing number zero.

"""
A try statement can have multipal different except block to handle different exceptions:
"""
x = input("Enter: ")
try:
    print(x + 'Hello')
    print(10 / x)
except ZeroDivisionError:
    print('Divided by zero')
except (ValueError, TypeError):
    print('Error occurred')

#_____________________________________________________________

#finally
"""
The finally statement is placed after a try/except statement and used to run code no matter if an exception occurs or not.
"""
try:
    print('Hello')
    print(1/0)
except ZeroDivisionError:
    print('Divided by zero')
finally:
    print('This code will run no matter what')

'''
The code in finally will run even if the code exceptions that occurred wasn't handled.
'''

#_____________________________________________________________

#else statement in try/except
'''
An else statement can be used after a try/except block, to run code only if on exception occurs in the try statement.
'''
x = 7
y = 2
try:
    print(x/y)
except ZeroDivisionError:
    print('Error')
else:
    print('All good')

#_____________________________________________________________

#raise
'''
The raise keyword is used to manually raise an exception.
It can be used, for example, to validate an input formate.
'''
#ex.
name = input("Enter the name: ")
if len(name) < 3:
    raise ValueError("invalid name")
"""
exceptions must derive from BaseException
BaseExceptions like ValueError, ZeroDivisionError etc...
"""

