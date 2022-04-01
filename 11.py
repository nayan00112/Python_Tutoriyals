#Dictionaries 

"""
Dictionaries are collections of data, which map keys to values.
Each element in a dictionary is represented by a key:value pair.
"""

ages = {"Dave": 24, "Mary": 42, "Jignesh": 18}

"""
You can access elements using their keys:
"""

print(ages['Dave'])

"""
You can also use get() method to access elements.
If the keys is not found in the dictionary you can return another specified value instead:
"""

ages = {"Dave": 24, "Mary": 42, "Jignesh": 18}
print(ages.get('Dave')) #24
print(ages.get("Marmik", 19)) #19

#----------------------------------------------------------------------------------

#Tuples
"""
Tuples are collections of unchangable (immutable) items.
Tuples are defined using parentheses:
"""
words = ('spam', 'angle', 'nicrom')

"""
You can access the value in the tuple with their index:
"""

print(words[0]) # spam

"""
Trying to reassign a value in a tuple causes an error:
"""

#words[1] = 'cheese'
# TypeError: 'tuple' object does not support item assignment.

"""
The main adevantages of tuples over list is that tuples are faster and can be used as key in dictionaries, whereas list can't.
"""

#----------------------------------------------------------------------------------

#Typle Unpacking
"""
Tuple unpacking lets you assign each item in tuple to a variable using a single statement.
"""

numbers = (1, 2, 3)
a, b, c = numbers
print(a) #1
print(b) #2
print(c) #3


numbers = (1, 2, 3)
x, y, z = numbers
print(x) #1
print(y) #2
print(z) #3

"""
Tuples unpacking can be used to swap two variable values: a, b = b, a
"""