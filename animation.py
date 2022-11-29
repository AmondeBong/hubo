from cs1graphics import *
from time import *
import math
import random

# rotate(n) 시계 방향으로 n도 회전 시킴
# scale(n) n배 커짐
# flip(n) 축을  n도 회전시켜서 기준으로 접힘
paper = Canvas()

paper.setBackgroundColor('powderBlue')
paper.setWidth(500)
paper.setHeight(200)
paper.setTitle('draw')


def animate_sunrise(sun):
    w = paper.getWidth()
    h = paper.getHeight()
    r = sun.getRadius()
    x0 = w / 2.0
    y0 = h + r
    xradius = w / 2.0 - r
    yradius = h
    for angle in range(181):  # 0 ~ 180
        rad = (angle/180.0) * math.pi
        x = x0 - xradius * math.cos(rad)
        y = y0 - yradius * math.sin(rad)
        sun.moveTo(x, y)


ground = Ellipse(700, 100, Point(300, 200))
ground.setFillColor('green')
paper.add(ground)

sun = Circle(50, Point(400, 100))
sun.setFillColor('orange')
sun.setDepth(60)
paper.add(sun)

roof = Polygon(Point(105, 105), Point(175, 105),
               Point(170, 85), Point(110, 85))
roof.setFillColor('black')
paper.add(roof)

facade = Square(60, Point(140, 130))
facade.setFillColor('gray')
paper.add(facade)

cat = Layer()
leg1 = Rectangle(10, 10, Point(-20, -10))
leg1.setFillColor('brown')
cat.add(leg1)

leg2 = Rectangle(10, 10, Point(20, -10))
leg2.setFillColor('brown')
cat.add(leg2)

body = Rectangle(60, 30, Point(0, -30))
body.setFillColor('brown')
cat.add(body)

head = Circle(20, Point(-30, -50))
head.setFillColor('brown')
cat.add(head)

eyes1 = Circle(3, Point(-21, -53))
eyes1.setFillColor('black')
cat.add(eyes1)

eyes2 = Circle(3, Point(-41, -53))
eyes2.setFillColor('black')
cat.add(eyes2)

nose = Ellipse(10, 5, Point(-30, -43))
nose.setFillColor('black')
cat.add(nose)


ear1 = Polygon(Point(-15, -80), Point(-25, -65), Point(-15, -60))
ear1.setFillColor('brown')
cat.add(ear1)

ear2 = Polygon(Point(-45, -80), Point(-35, -65), Point(-45, -60))
ear2.setFillColor('brown')
cat.add(ear2)


giraffe = Layer()

leg1 = Rectangle(10, 70, Point(400, 150))
leg1.setFillColor('yellow')
giraffe.add(leg1)

leg2 = Rectangle(10, 70, Point(320, 150))
leg2.setFillColor('yellow')
giraffe.add(leg2)

body = Rectangle(100, 30, Point(360, 130))
body.setFillColor('yellow')
giraffe.add(body)
neck = Rectangle(20, 70, Point(400, 100))
neck.setFillColor('yellow')
giraffe.add(neck)

head = Polygon(Point(400, 50), Point(450, 110), Point(400, 100))
head.setFillColor('yellow')
giraffe.add(head)

ear1 = Rectangle(8, 15, Point(410, 50))
ear1.setFillColor('brown')
giraffe.add(ear1)
ear2 = Rectangle(8, 15, Point(400, 50))
ear2.setFillColor('brown')
giraffe.add(ear2)

eyes2 = Circle(10, Point(415, 70))
eyes2.setFillColor('white')
giraffe.add(eyes2)

eyes1 = Circle(3, Point(415, 70))
eyes1.setFillColor('black')
giraffe.add(eyes1)

pattern = [None for _ in range(8)]

for i in range(8):
    num1 = random.randrange(320, 400)
    num2 = random.randrange(120, 140)
    pattern[i] = Square(6, Point(num1, num2))
    pattern[i].setFillColor('brown')
    giraffe.add(pattern[i])

giraffe.setDepth(10)
paper.add(giraffe)

cat.moveTo(110, 180)
cat.setDepth(10)
paper.add(cat)


timeDelay = 0.1


for i in range(10):
    cat.move(-10 - i*10, 0)

    sun.move(10+i*15, 5*i)
    sleep(timeDelay*2)

    giraffe.move(10+i*5, +5*i)
    sleep(timeDelay)
