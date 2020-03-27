from abc import ABCMeta, abstractmethod
class shape(metaclass=ABCMeta):
    @abstractmethod
    def printArea(self):
        return 0





class Rectangle(shape):
    type="Rectangle"
    sides=4

    def __init__(self):
        self.length=6
        self.breadth=4

    def printArea(self):
        return self.length*self.breadth

rect1=Rectangle()
rect2=shape()
print(rect1.printArea())