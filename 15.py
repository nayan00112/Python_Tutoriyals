#replace 

"""
The replace() method is used to replace a substring with another:
"""

text = 'I play cricket.'
print(text) # I play cricket.
print(text.replace('cricket', 'chess')) # I play chess.

#----------------------------------------------------------------------

#split

"""
The split() method turns a string withh a certain separator into a list.
"""

text = 'spam, angle, ham'
print(text.split(", ")) # ['spam', 'angle', 'ham'] (((This is oky for this example to split by ", ".)))
print(text.split(",")) # ['spam', ' angle', ' ham']
print(text.split(" ")) # ['spam,', 'angle,', 'ham']

"""
It can be used to separate words in a given string:
"""

text = 'How are you doing'
print(text.split(' ')) # ['How', 'are', 'you', 'doing']
print(text.split(' ')[2]) # you
