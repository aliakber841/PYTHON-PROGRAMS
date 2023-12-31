class Car:
    """ Just a simple program that is written for cars """ #DOC STRING

    def __init__(self,make_and_model,year,gearbox):
        """ Initialize Make and Model,year,gearbox """

        self.make_and_model=make_and_model
        self.year=year
        self.gearbox=gearbox

    def drive(self):
           print(f"{self.make_and_model} {self.year} {self.gearbox} is now driving")

    def stop_driving(self):
           print(f"{self.make_and_model} {self.year} {self.gearbox} is now STOPPED !")
    def start_drifting(self):
            print(f"{self.make_and_model} {self.year} {self.gearbox} is now DRIFTING !")

my_bmw = Car("BMW 325",2002,"AUTOMATIC")
print(f"My Car's make and model is {my_bmw.make_and_model}")
print(f"My Car's year is {my_bmw.year}")
print(f"My Car's gearbox type is {my_bmw.gearbox}")

my_bmw.drive()
my_bmw.stop_driving()
my_bmw.start_drifting()