import numpy as np
import drawline
import renderpoints as rp

def drawTriangle(x1, y1, x2, y2, x3, y3):
    points = []
    points.extend(drawline.draw_line(x1, y1, x2, y2))
    points.extend(drawline.draw_line(x2, y2, x3, y3))
    points.extend(drawline.draw_line(x3, y3, x1, y1))
    return points

def main():
    x1, y1 = 100, 0
    x2, y2 = 0, 100
    x3, y3 = -100, 0
    points = drawTriangle(x1, y1, x2, y2, x3, y3)
    print(points)

    rp.render_points(points)

if __name__ == "__main__":
    main()