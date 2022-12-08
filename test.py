from cs1graphics import *
from time import *
import copy
RADIUS = 3

paper = Canvas()
paper.setBackgroundColor('white')
paper.setWidth(40)
paper.setHeight(30)
paper.setTitle('My World')

dia = Layer()
triangle1 = Polygon(Point(0, 0), Point(-RADIUS*2,
                                       RADIUS*3), Point(RADIUS*2, RADIUS*3))
triangle1.setFillColor('red')
triangle1.setBorderWidth(0)
dia.add(triangle1)

triangle2 = Polygon(Point(0, 0), Point(-RADIUS*2, -
                                       RADIUS*3), Point(RADIUS*2, -RADIUS*3))
triangle2.setFillColor('red')
triangle2.setBorderWidth(0)
dia.add(triangle2)


paper.add(dia)
