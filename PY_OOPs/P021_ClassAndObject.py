class Car:
    def __init__(self, name):
        self.name = name
    wheel = 4
    engineCulinder = 6
    def run(self):
        print("Car is running.", self.name)
    def stop(self):
        print("Car is stopped.", self.name)

c1 = Car("BMW")
c2 = Car("Farari")

c1.run()
c2.run()
c1.stop()
c2.stop()

# Output:
# Car is running. BMW
# Car is running. Farari
# Car is stopped. BMW
# Car is stopped. Farari