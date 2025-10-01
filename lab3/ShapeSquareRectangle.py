class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length=0):
        self.length = length
    def print_area(self):
        self.area = self.length ** 2
        print('Area of square: ', self.area)
    def get_length(self):
        self.length = int(input('Lenght of square: '))
class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    def print_area(self):
        self.area = self.length * self.width
        print('Area of rectagle; ', self.area)
    def get(self):
        self.length = int(input('Length of rectangle: '))
        self.width = int(input('Width of rectangle: '))

sq = Square()
sq.get_length()
sq.print_area()

rct = Rectangle()
rct.get()
rct.print_area()