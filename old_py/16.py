# Pattern Fun
# down piramid
n = 6
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n - i):
        print(" *", end="")  
    print()
#left tryangle 90
n = 6
for i in range(n):
    for j in range( i):
        print(" *", end="")
    for j in range( n - i):
        print(" ", end="")  
    print()



#Piramid up
n = 6
for i in range(n):
    for k in range( n - i):
        print(" ", end="") 
    for j in range( i):
        print(" *", end="") 
    print()

#Right trayangle
n = 6
for i in range(n):
    for j in range(2*(n- i)):
        print(" ", end="")
    for j in range(i):
        print(" *", end="")  
    print()