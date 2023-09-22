# Andy Yu
# Sep 15, 2023
# Pi Calculator, Quadtree

import math
CANVAS_SIZE = 1
precision = 10
circle_x = circle_y = CANVAS_SIZE
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def in_circle(x, y):
    return dist(x, y, circle_x, circle_y) < CANVAS_SIZE

def rect_in_circle(x1, y1, x2, y2):
    return in_circle(x1, y1) != in_circle(x2, y1) or in_circle(x1, y1) != in_circle(x1, y2) or in_circle(x1, y2) != in_circle(x2, y2)

def subdivide_area(x1, y1, x2, y2, precision, start = True):
    area_sum = 0
    xm = (x1+x2)/2
    ym = (y1+y2)/2
    if precision > 0 and (start or rect_in_circle(x1, y1, x2, y2)):
        area_sum += 0.25*subdivide_area(x1, y1, xm, ym, precision-1, False) 
        area_sum += 0.25*subdivide_area(xm, y1, x2, ym, precision-1, False)
        area_sum += 0.25*subdivide_area(xm, ym, x2, y2, precision-1, False)
        area_sum += 0.25*subdivide_area(x1, ym, xm, y2, precision-1, False)
        return area_sum
    return float(in_circle(xm, ym))
for i in range(1, 24):
    print(f"{i} - {subdivide_area(0, 0, CANVAS_SIZE, CANVAS_SIZE, i)*4}")


