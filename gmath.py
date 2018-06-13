import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, lights, constants):
    normalize(normal)
    normalize(view)

    a = calculate_ambient(ambient, constants)
    d = calculate_diffuse(normal, lights, constants)
    s = calculate_specular(normal, lights, constants, view)

    i = [0, 0, 0]
    i[RED] = int(a[RED] + d[RED] + s[RED])
    i[GREEN] = int(a[GREEN] + d[GREEN] + s[GREEN])
    i[BLUE] = int(a[BLUE] + d[BLUE] + s[BLUE])
    limit_color(i)

    return i


def calculate_ambient(ambient, constants):
    a = [0, 0, 0]
    a[RED] = ambient[RED] * constants['red'][0]
    a[GREEN] = ambient[GREEN] * constants['green'][0]
    a[BLUE] = ambient[BLUE] * constants['blue'][0]
    return a

def calculate_diffuse(normal, lights, constants):
    d = [0, 0, 0]

    for light in lights:
        light = lights[light]
        normalize(light['location'])
        dot = dot_product(normal, light['location'])
        d[RED] += light['color'][RED] * constants['red'][1] * dot
        d[GREEN] += light['color'][GREEN] * constants['green'][1] * dot
        d[BLUE] += light['color'][BLUE] * constants['blue'][1] * dot
    return d

def calculate_specular(normal, lights, constants, view):
    s = [0, 0, 0]
    n = [0, 0, 0]

    for light in lights:
        light = lights[light]
        normalize(light['location'])
        result = 2 * dot_product(light['location'], normal)
        n[0] = (normal[0] * result) - light['location'][0]
        n[1] = (normal[1] * result) - light['location'][1]
        n[2] = (normal[2] * result) - light['location'][2]
        result = dot_product(n, view)
        result = pow(result, SPECULAR_EXP) if result > 0 else 0
        s[RED] += light['color'][RED] * constants['red'][2] * result
        s[GREEN] += light['color'][GREEN] * constants['green'][2] * result
        s[BLUE] += light['color'][BLUE] * constants['blue'][2] * result
    return s

def limit_color(color):
    color[:] = [min((max((int(c),0)), 255)) for c in color]


#vector functions
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
