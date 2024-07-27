# import time [in this case like delay happen in executing function]
import time

# import thread
from threading import Thread

# Demo class inherite Thread
class Demo(Thread):
    
    # init method
    def __init__(self, number):
        super().__init__()
        self.number = number
        
    # run method
    def run(self):
        time.sleep(1) # dumy delay
        print(self.number)


# make a list of objects on Demo class
a = [Demo(_) for _ in range(5)]

# call run method of Demo class by thread start method
for i in a:
    i.start()

# wait for all thread execute completely
for i in a:
    i.join()
    
# done!
print("Done")


# ------------------------------------------------

print("Old way:")
class oldDemo:
    def __init__(self, number):
        self.number = number
        
    def show(self):
        time.sleep(1)
        print(self.number)
    
b = [oldDemo(_) for _ in range(5)]
for i in b:
    i.show()
    
print("Old Done")
        
    
    