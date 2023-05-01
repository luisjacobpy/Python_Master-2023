# Cartesian plane
This code defines two classes: Point and Rectangle. The Point class represents a point in a Cartesian plane, while the Rectangle class represents a rectangle in the same plane.

The Point class has the following methods:

init(self, x=0, y=0): constructor that initializes the x and y coordinates of the point. If no values are provided, 0 is taken as the default.
str(self): method that returns a string that represents the point in the format "(x, y)".
cuadrante(self): method that determines the quadrant in which the point is located. It returns a message with the result.
vector(self, p): method that calculates the vector between two points and returns a message with the result.
distancia(self, p): method that calculates the distance between two points and returns a message with the result.

The Rectangle class has the following methods:

init(self, pInicial=Point(), pFinal=Point()): constructor that initializes the initial and final points of the rectangle. If no values are provided, two points are created at the origin by default.
base(self): method that calculates the base of the rectangle and returns a message with the result.
altura(self): method that calculates the height of the rectangle and returns a message with the result.
area(self): method that calculates the area of the rectangle and returns a message with the result.

In the final part of the code, several objects of the Point class are created and various methods are called to perform different calculations and obtain results in the form of messages. An object of the Rectangle class is also created and its base, height, and area are calculated.