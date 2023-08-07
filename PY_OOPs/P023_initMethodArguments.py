class Computer:
    def __init__(self, proc, ram, disk): #like constructor in java or cpp
        self.processor = proc
        self.ram = ram
        self.disk = disk
    
    def config(self):
        print(self.processor, self.ram, self.disk)


com1 = Computer("i5", "8GB", "512GB")
com2 = Computer("i9", "64GB", "4TB")

com1.config()
com2.config()

# Output:
# i5 8GB 512GB
# i9 64GB 4TB