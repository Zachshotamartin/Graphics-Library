import drawquadrilateral as dq
import renderpoints as rp
def orientation(p, q, r):
    # Calculate the orientation of three points (p, q, r)
    # Returns 0 if they are collinear, 1 if clockwise, and 2 if counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

def is_convex(points):
    n = len(points)
    if n < 4:
        return False  # Not enough points to form a polygon or a triangle cannot be concave

    # Check the orientation of each triplet of points
    prev_orientation = orientation(points[0], points[1], points[2])
    for i in range(1, n):
        curr_orientation = orientation(points[i], points[(i + 1) % n], points[(i + 2) % n])
        if curr_orientation != prev_orientation:
            return False  # Points are not consistently oriented
        prev_orientation = curr_orientation

    return True  # All points are consistently oriented, so it's convex

# Example usage

def main():
    points = [(0, 0), (100, 200), (200, 0), (100, 100), (50, 75)]
    if is_convex(points):
        print("The points form a convex polygon")
    else:
        print("The points form a concave polygon")
    points = dq.drawPolygon(points)
    rp.render_points(points)


if __name__ == "__main__":
    main()