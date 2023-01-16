#Application 1
# Write a Python program that computes for the area and perimeter of a rectangle
# Use the Shape as parent class
# Use Area() and Perimeter () as methods with its attributes length and width
# Use Rectangle as child class

class Shape:
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def Area(self):
    return self.length * self.width

  def Perimeter(self):
    return (self.length + self.width)*2
  def display(self):
    print("The area of a rectangle is", self.Area())
    print("The perimeter of a rectangle is", self.Perimeter())


class Rectangle(Shape):
  pass

rectangle = Shape(10,5)
rectangle2 = Rectangle(10,5)

rectangle.display()
rectangle2.display()
