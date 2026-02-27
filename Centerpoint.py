# Centerpoint
#
# Functions related to the centerpoint, or a 1-point epsilon net

import math
from itertools import combinations
import shapely
from shapely.geometry import Polygon, Point, LineString

# brute force find the centerpoint of a set of vertices
# does so by finding the intersection of sets with > 2/3 vertices
def findCenterpoint(vertices):
    numInSet = math.floor( (2/3)*len(vertices) ) + 1

    polygons = [Polygon(set) for set in combinations(vertices, numInSet)]

    return shapely.intersection_all(polygons)

# A way to find the centerpoint of a set of convex points
# does so by "rotating" around all of the boundary sets that are large enough
def findCenterpointRotation(vertices):
    numInSet = math.floor( (2/3)*len(vertices) ) + 1

    boundaryPolygons = []

    currentSet = [vertices[i] for i in range(numInSet)]

    rotationStart = numInSet
    for i in range(len(vertices)):
        boundaryPolygons.append( Polygon(currentSet) )

        currentSet.pop(0)
        currentSet.append( vertices[(rotationStart + i) % len(vertices)] )

    return shapely.intersection_all(boundaryPolygons)

# Given a vertex from a convex set's centerpoint,
# determines the 2 2/3rds-boundary sets that defined it
# and returns the two lines that defined it
def findDefiningVertexLines(vertices, point):
    numInSet = math.floor( (2/3)*len(vertices) ) + 1
    n = len(vertices)

    lines = []
    for i in range(0,n):
        lines.append( LineString( [vertices[i], vertices[ (i + numInSet - 1) % n ]] ) )

    for pair in combinations(lines, 2):
        int = pair[0].intersection(pair[1])
        if type(int) is Point and int.equals_exact(point, 0.001):
            return pair
        
    return None