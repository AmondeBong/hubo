from cs1media import *


def luma(p):
    r, g, b = p
    return int(0.213 * r + 0.715 * g + 0.072 * b)


img = load_picture("말티즈.jpg")
img.show()

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)

w, h = img.size()

for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r+g+b)//3

        if v > threshold:
            img.set(x, y, white)
        else:
            img.set(x, y, black)

img.show()
