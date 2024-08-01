import drawline
import numpy as np
import renderpoints as rp

def drawRectangle(x1, y1, x2, y2):
    points = []
    points.extend(drawline.draw_line(x1, y1, x1, y2))
    points.extend(drawline.draw_line(x1, y2, x2, y2))
    points.extend(drawline.draw_line(x2, y2, x2, y1))
    points.extend(drawline.draw_line(x2, y1, x1, y1))
    return points

def main():
    x1, y1 = 100, 0
    x2, y2 = 0, 100
    points = drawRectangle(x1, y1, x2, y2)
    rp.render_points(points)

if __name__ == "__main__":
    main()