#while loop : The while loop lets you repeat a blockof code multiple times, until its conditions holds.
i = 1
while i < 5:
    print(i)
    i = i + 1
#1
#2
#3
#4



# infinite loop : A loop becomes infinite if its condition is always True.
##x = 4
##while x < 5:
##    print(x)



#break : Ust the break statement to stop a loop.
i = 1
while 1 < 7:
    print(i)
    if i == 3:
        break
    i += 1
# The loop will stop when i reaches the value 3.


#continue : The continue statement stop the current iteration of a loop and continues with the next one
x = 0
while x < 5:
    x += 1 #x= x + 1
    if x == 2:
        continue
    print('"continue in loop"',x)
    # The loop will print the number 1 to 5 skipping the number 2.

#for loop : Use for loop to iterate over a given sequency, like list or strings.
num = [1, 2, 3]
for x in num:
    print(x)

for x in 'Hello':
    print(x)

name = "Jignesh"
for x in name:
    print(x)

#range
#The range() function is used to create a sequency of numbers.
for x in range(5):
    print('"range function"', x)
    # Start 0 to 4 in this case.

for x in range(3, 7):
    print(x)
    # Start 3 to 6 in this case.(a range() starts from 0 by default, but it's possible to specify the starting value by adding an argument(example is above.).)

    # The range() can also take a third argument, specifying the stap:
for x in range(3,8,2):
    print(x)
    # output 3, 5, 7
