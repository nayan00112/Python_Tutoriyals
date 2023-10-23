# List Slices

"""
List Slices let you get certain elements of a list.
You can privide two colon-separated numbers to get the elements between the indices:
"""

squares = [0, 1, 4, 9, 16, 25, 36]
print(squares[2:5]) #[4, 9, 16]

# {{{Notice that the element at the second index is not include.}}}

"""
Omitting the first index is taken to be the start of the list, while omitting the  senond index is taken to the end.
"""

squares = [0, 1, 4, 9, 16, 25, 36]
print(squares[5:]) #[25, 36]
print(squares[:5]) #[0, 1, 4, 9, 16]

"""
List slices can also have a third number representing the step:
"""

squares = squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:9:3]) #[4, 25, 64]

#---------------------------------------------------------------------------

#List Comprehensions
"""
List comperehesions are a useful way of quickly creating lists whose contents obey simple rule.
"""

cubes = [i**3 for i in range(5)]
print(cubes) #[0, 1, 8, 27, 64]

"""
A list comperehesion can also contain an if statement:
"""

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens) #[0, 4, 16, 36, 64]
