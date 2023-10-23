#1ptint
print('Hello World')
print('....................................................................')

#2float
x = 1.34
print(x)
print(type(x))
print(4/2)
print(type(print(4/2))) #give float number but type for 'print'
y = print(type(4/2)) #float type
print(y)
print('....................................................................')

#3integer
x = 3
print(x)
print(4)
print(type(x))
print('....................................................................')

#4Exponentiation
print(2**5) #2^5
print('....................................................................')

#5Floor Division
print( 20 // 3)
print('....................................................................')

#6Modulo
print(20%6)
print('....................................................................')

#7string
name = 'Patel Nayan ashokbhai'
print(name)
print(type(name))
txt = 'I\'m Nayan'
print(txt)
print('I' + ' ' + 'am Nayan')

print('Nayan'*3) #NayanNayanNayan

print("one line \nSecond line\nThird line")
    #one line
    #Second line
    #Third line
print("""one line
is a multiline 
text""")

#one line
#is a multiline 
#text
print('....................................................................')


#8Escaping
txt = 'I \'m learning python' #\'
print(txt)
print('....................................................................')

#9Variable
user = 'Marmik'
x = 3
y = 7
z = x + y
print(x, ' + ', y, ' = ', z)
print('....................................................................')


# print() function provide new line at end of the string,
# if we don't want to new line then:
print("Hello Nayan", end="")
print("Hello Marmik")




# output:
# Hello World
# ....................................................................
# 1.34
# <class 'float'>
# 2.0
# 2.0
# <class 'NoneType'>
# <class 'float'>
# None
# ....................................................................
# 3
# 4
# <class 'int'>
# ....................................................................
# 32
# ....................................................................
# 6
# ....................................................................
# 2
# ....................................................................
# Patel Nayan ashokbhai
# <class 'str'>
# I'm Nayan
# I am Nayan
# NayanNayanNayan
# one line 
# Second line
# Third line
# one line
# is a multiline 
# text
# ....................................................................
# I 'm learning python
# ....................................................................
# 3  +  7  =  10
# ....................................................................
# Hello NayanHello Marmik