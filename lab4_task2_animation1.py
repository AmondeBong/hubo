from cs1graphics import*
from time import*
import copy

paper = Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(300)
paper.setHeight(200)
paper.setTitle('My World')

roof = Polygon(Point(105, 105), Point(175, 105), Point(170, 85), Point(110, 85))
roof.setFillColor('darkgray')
roof.setDepth(30) # in front of façade
paper.add(roof)
facade = Square(60, Point(140, 130))
facade.setFillColor('white')
paper.add(facade)
window=Square(10, Point(130, 120))
window.setFillColor('black')
window.setBorderColor('red')
window.setBorderWidth(1)
paper.add(window)
chimney = Rectangle(15, 28, Point(155, 85))
chimney.setFillColor('red')
chimney.setBorderColor('red')
chimney.setDepth(20) # in front of roof
paper.add(chimney)
smoke = Path(Point(155, 70), Point(150, 65),
Point(160, 55), Point(155, 50))
smoke.setBorderWidth(2)
paper.add(smoke)


tree=Polygon(Point(20,20),Point(-20,20),Point(0,-100))
tree.setFillColor("darkgreen")
tree.setDepth(50)
tree.moveTo(60,170)
paper.add(tree)

sun=Layer()
ci = Circle(20)
p1=Rectangle(13,4,Point(30,0))
p2=Rectangle(4,13,Point(0,30))
p3=Rectangle(13,4,Point(-30,0))
p4=Rectangle(4,13,Point(0,-30))
p1.setFillColor("darkorange")
p1.setBorderColor("darkorange")
p2.setFillColor("darkorange")
p2.setBorderColor("darkorange")
p3.setFillColor("darkorange")
p3.setBorderColor("darkorange")
p4.setFillColor("darkorange")
p4.setBorderColor("darkorange")
ci.setFillColor("darkorange")


ground=Rectangle(300,60,Point(150,170))
ground.setBorderColor("green")
ground.setFillColor("green")
ground.setDepth(100)
paper.add(ground)
sun.add(ci)
sun.add(p1)
sun.add(p2)
sun.add(p3)
sun.add(p4)
sun.rotate(45)
sun.moveTo(250, 50)
paper.add(sun)

car = Layer()
tire1 = Path(Point(-20, -10),Point(-20, 0))
tire1.setBorderWidth(3)
car.add(tire1)
tire2 = Path(Point(20, -10),Point(20, 0))
tire2.setBorderWidth(3)
car.add(tire2)
body = Rectangle(70, 30, Point(0, -25))
body.setFillColor('blue')
body.setDepth(60)# behind the tires
car.add(body)
car.moveTo(110, 180)
car.setDepth(20)# in front of the house
paper.add(car)

timeDelay= 1
j=0
for i in range(100):
    car.move(-i,0)
    if j%2==0:         
        tire1.rotate(330)
        tire2.rotate(330)
    else:
        tire1.rotate(30)
        tire2.rotate(30)
    sleep(timeDelay)
    j+=1