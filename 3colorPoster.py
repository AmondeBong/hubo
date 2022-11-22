from cs1media import *


def luma(p):
    r, g, b = p
    return int(0.213 * r + 0.715 * g + 0.072 * b)


img = load_picture("말티즈.jpg")
img.show()

bright = 100
dark = 30

Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)


w, h = img.size()

for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)

        v = (r+g+b)//3

        if v > bright:
            img.set(x, y, Yellow)
        elif v < dark:
            img.set(x, y, Blue)
        else:
            img.set(x, y, Green)
img.show()
