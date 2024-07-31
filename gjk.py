import numpy as np
import math

def furthestPoint(shape, d):
    furthest_point = None
    max_distance = float('-inf')
    for point in shape:
        distance = np.dot(point, d)
        if distance > max_distance:
            max_distance = distance
            furthest_point = point
    return furthest_point
       
    
def GJK(s1, s2):
    d = np.array([1, 0, 0])
    simplex = [support(s1, s2, d)]
    d = np.array([0 - simplex[0][0], 0 - simplex[0][1], 0 - simplex[0][2]])  # Fix: Convert d to a numpy array with the same dimension as the points
    while True:
        A = support(s1, s2, d)
        if np.dot(A, d) < 0:
            return False
        simplex.append(A)
        if doSimplex(simplex, d):
            return True
        
    
         
def support(s1, s2, d):
    return furthestPoint(s1, d) - furthestPoint(s2, d)

def doSimplex(simplex, d):
    if len(simplex) == 2:
        return lineCase(simplex, d)
    return triangleCase(simplex, d)

def lineCase(simplex, d):
    B, A = simplex
    AB, AO = B - A, 0 - A
    ABperp = tripleProduct(AB, AO, AB)
    d = ABperp
    return False

def triangleCase(simplex, d):
    C, B, A = simplex
    AB, AC, AO = B - A, C - A, 0 - A
    ABperp = tripleProduct(AC, AB, AB)
    ACperp = tripleProduct(AB, AC, AC)
    if np.dot(ABperp, AO) > 0:
        simplex.remove(C)
        d = ABperp
        return False
    elif np.dot(ACperp, AO) > 0:
        simplex.remove(B)
        d = ACperp
        return False
    return True;

def tripleProduct(a, b, c):
    return np.cross(np.cross(a, b), c)

def main():
    s1 = np.array([(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)])
    s2 = np.array([(2, 2, 0), (2, 3, 0), (3, 3, 0), (3, 2, 0)])
    print(GJK(s1, s2))


if __name__ == "__main__":
    main()