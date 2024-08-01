import numpy as np
import renderpoints as rp

def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy

    points = []
    if x1 == x2:
        for y in range(y1, y2 + sy, sy):
            points.append((x1, y))
    elif y1 == y2:
        for x in range(x1, x2 + sx, sx):
            points.append((x, y1))
    else:
        while True:
            points.append((x1, y1))

            if x1 == x2 and y1 == y2:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    return points

def main():
    x1, y1 = 0, 0
    x2, y2 = 100, 100
    points = draw_line(x1, y1, x2, y2)
    print(points)

    rp.render_points(points)

if __name__ == "__main__":
    main()