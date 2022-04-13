from Circle import *
from Square import *
from Shape2D import *
c1 = Circle("Red",1)
c2 = Circle("White", 100)
s1 = Square("Green",5)
s2 = Square("Black",7)
def test_Shape2D():
    c1.setColor("Yellow")
    s1.setColor("Green")
    assert c1.getColor()=="Yellow"
    assert s1.getColor() == "Green"
    assert s2.getShapeProperties() == "Shape: SQUARE, Color: Black, Side: 7, Area: 49, Perimeter: 28"
def test_Circle():
    c2.setRadius(10)
    assert c1.getShapeProperties() == "Shape: CIRCLE, Color: Yellow, Radius: 1, Area: 3.14159, Perimeter: 6.28318" 
    assert c1.getRadius() == 1
    assert c2.computePerimeter() == 62.8318
    assert c2.computeArea() == 314.159
def test_Square(): 
    s1.setSide(10) 
    assert s1.getSide() == 10  
    assert s1.computePerimeter() == 40
    assert s2.getShapeProperties() == "Shape: SQUARE, Color: Black, Side: 7, Area: 49, Perimeter: 28"
    assert s1.computeArea()== 100
    
    
    
