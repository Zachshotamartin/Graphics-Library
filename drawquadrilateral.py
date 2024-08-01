import numpy as np
import drawline
import renderpoints as rp

def drawPolygon(points):
    length = len(points)
    new_points = []
    for i in range (length):
        if len(points[i]) == 3:
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[(i + 1) % len(points)]
            print(x1, y1, x2, y2)
            new_points.extend(drawline.draw_line(x1, y1, x2, y2))
            print(new_points)
        elif len(points[i]) == 2:
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            new_points.extend(drawline.draw_line(x1, y1, x2, y2))
    return new_points

def main():
    x1, y1 = 0, 0
    x2, y2 = 0, 100
    x3, y3 = 100, 600
    x4, y4 = 200, 100
    x5, y5 = 200, 0
    points = drawPolygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)])
    print(points)

    rp.render_points(points)

if __name__ == "__main__":
    main()