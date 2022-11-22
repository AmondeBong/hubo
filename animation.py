from cs1graphics import *
from time import *

paper = Canvas()

paper.setBackgroundColor('powderBlue')
paper.setWidth(500)
paper.setHeight(300)
paper.setTitle('draw')


roof = Polygon(Point(105, 105), Point(175, 105),
               Point(170, 85), Point(110, 85))
roof.setFillColor('black')
paper.add(roof)

facade = Square(60, Point(140, 130))
facade.setFillColor('gray')
paper.add(facade)

car = Layer()
tire1 = Circle(10, Point(-20, -10))
tire1.setFillColor('darkGray')
car.add(tire1)

tire2 = Circle(10, Point(20, -10))
tire2.setFillColor('darkGray')
car.add(tire2)

body = Rectangle(70, 30, Point(0, -25))
body.setFillColor('khaki')
car.add(body)

car.moveTo(110, 180)
car.setDepth(20)
paper.add(car)

timeDelay = 1
sleep(timeDelay)

car.move(-10, 0)
sleep(timeDelay)
car.move(-30, 0)
sleep(timeDelay)
car.move(-60, 0)
sleep(timeDelay)
car.move(-100, 0)
sleep(timeDelay)
