from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            
class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")

t1 = Hello()
t2 = Hii()

# t1.run()
# t2.run()
# Output (using above two lines, Not use thread but simple method call):
# Hello
# Hello
# Hello
# Hello
# Hello
# Hii
# Hii
# Hii
# Hii
# Hii

t1.start()
t2.start()
# Output: (actually use multiple thread.)
# Hello
# Hii
# HelloHii
# Hello

# HelloHii

# Hii
# HelloHii
