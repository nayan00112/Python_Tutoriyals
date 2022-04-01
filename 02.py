#input
#name = input('enter name: ')
#print(name)


#Type conversion
x = '445'
print(type(x))
y = int(x)
print(type(y))

s = 'hello'
print(list(s))


#Concatenation
print ('spam' + " " + 'eggs')


#Booleans
print(4 == 5) # False
print(3 < 4) # True
print(2 > 3)# False

# If Statement
x = 33
if x > 10:
    print("yes")


#else Statement
age = 4
if age >= 18:
    print('Adult')
else:
    print("child")

#elif
num = 3
if num == 4:
    print('four')
elif num == 3 :
    print('three')
else:
    print('Something else')


# and 
age = 18
if age >16 and age <21:
    print("16<x<21")
else:
    print('grater then 21 or smaller then 16')
#or
x = 11
y = 2
if x > 10 or y > 4:
    print('True')
else:
    print("False")

# not
x = 9
if not x > 10:
    print('yes')

# list
name = ['Nayan', 'Marmik', 'Jignesh']
print(name)
print(name[1])

#in 
#The in operator is used to check if an item is present in a list
name = ['Nayan', 'Marmik', 'Jignesh']
if 'Jignesh' in name:
    print("yes")
