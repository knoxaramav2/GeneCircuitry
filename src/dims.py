from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Dim = namedtuple('Dim', ['x', 'y', 'z'])

def centerDim(point:Point)->list:
    return [point.x/2, point.y/2]


