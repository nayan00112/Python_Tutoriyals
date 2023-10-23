#format

"""
The format() method lets you insert values into placeholders in a string
"""

text = '{0} is {1} years old'.format("Jignesh", 18)
print(text) #Jignesh is 18 years old

sentance = "{0} is {1} {2} with {3} teams.".format('He', 'playing', 'cricket', 'his')
print(sentance) #He is plays cricket with his teams.

"""
The placeholders are defined using curly braces.

String formatting can also be done with named arguments:
"""

a = '({x}, {y})'.format(x = 5, y = 12)
print(a) # (5, 12)
