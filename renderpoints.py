import matplotlib.pyplot as plt
import drawline
def render_points(points):
    
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.scatter(x_values, y_values)
    plt.show()