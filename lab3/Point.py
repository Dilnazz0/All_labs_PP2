class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        print(f"x coordinate is {self.x}  and y coordinate is {self.y}")
    def move(self):
        self.x=int(input("Enter x coordinate of the first point: "))
        self.y=int(input("Enter y coordinate of the first point: "))
    def dist(self):
        x2 = int(input("Enter x coordinate of the second point: "))
        y2 = int(input("Enter x coordinate of the second point: "))
        distance = ((self.x - x2) ** 2 + (self.y - y2) ** 2) ** 0.5
        print(f"the distance between 2 points is {distance}")

obj=Point()
obj.show()
obj.move()
obj.dist()
