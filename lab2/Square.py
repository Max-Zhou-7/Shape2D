from Shape2D import Shape2D
class Square(Shape2D):
    pass
    def __init__(self, color = None, side = None):
        self.color = color
        self.side = side
    def getSide(self):
        return self.side
    def setSide(self,side):
        self.side = side
    def computeArea(self):
        return self.side**2
    def computePerimeter(self):
        return 4*self.side
    def getShapeProperties(self):
        return "Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}"\
            .format(self.color,self.side,self.computeArea(),self.computePerimeter())
# s1 = Square("blue", 2.5)
# print(s1.getShapeProperties())  