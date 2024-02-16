class Point:
    def __init__(self,x,y): #Constructor
        self.x=x
        self.y=y  # Self is reference to the current object.
    def move(self):
        print("Move...")

    def draw(self):
        print("Draw...")


point1=Point(30,40)
#point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2=Point(10,20)
#point2.x=23
print(point2.x)

class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi, I am {self.name}")

Ali=Person("Ali Akber")
print(Ali.name)
Ali.talk()
