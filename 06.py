# Function
# A function is a block of code which gets executed when called.
def welcome():
    print("Welcome")

welcome()
# The code above defines a function calleed 'welcome()' using the 'def' keyword and callit.


#Function argument
def fun(a, b):
    print(a+b)
fun(1,3)
#return
def mean(a, b, c):
    return ((a + b + c)/3)
d = mean(2, 4, 6)
print(d)

#{{{once the return a value frim a function, it immiediatakey stops being excuted. And code after it will never happen.}}}

