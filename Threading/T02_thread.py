l = [1,2,3,4,5,6,7,8]

from threading import *

class listdisp(Thread):
    for i in range(len(l)):
        print(i*5)

t = listdisp()
t.start()