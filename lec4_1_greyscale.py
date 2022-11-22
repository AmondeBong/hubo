from cs1media import *


def luma(p):
    r, g, b = p
    return int(0.213 * r + 0.715 * g + 0.072 * b)


img = load_picture("말티즈.jpg")
img.show()
w, h = img.size()

for y in range(h):  # 세로
    for x in range(w):  # 가로
        color = img.get(x, y)
        l = luma(color)
        grey = (l, l, l)
        img.set(x, y, grey)
img.show()
