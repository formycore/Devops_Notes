from abc import ABC,abstractmethod
from math import sqrt
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def figure(self):
        return 'this is a 2D plane figure'
class Rectangle(Polygon):
    def sides(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth # area of rectangle length X breadth
    def perimeter(self):
        return 2*(self.length+self.breadth) # perimeter of rectangle is 2*(length+breadth)
    def extramethod(self):
        return 'rectangle has 4 sides'
class Square(Polygon):
    def sides(self,side):
        self.side = side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*(self.side)
    def extramethod(self):
        print("This square has 4 sides")
rec = Rectangle()
rec.sides(10,20)
squ = Square()
squ.sides(10)

for obj in [rec,squ]:
    print(f"This is for {obj} are : {obj.area()}")
    print(f"This is for {obj} are : {obj.perimeter()}")
    print(f"This is for {obj} are : {obj.extramethod()}")
    print(f"This is for {obj} are : {obj.figure()}")
        
