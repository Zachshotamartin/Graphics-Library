import matplotlib.pyplot as plt

def DrawPolygons(shapes):
    for shape in shapes:
        xs, ys, zs = zip(*shape)
        xs += (xs[0],)  # Add the first point to the end to close the polygon
        ys += (ys[0],)  # Add the first point to the end to close the polygon
        plt.plot(xs, ys)
        plt.plot(xs,ys)
    plt.show()
