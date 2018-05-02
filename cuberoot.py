__author__ = 'Douzette'
import math

def cube_root(a):
    q, exponent = math.frexp(a)

    exponent_1 = 0.629960524947
    exponent_2 = 0.793700525984
    x0 = 0.896821469

    x = ((q / (x0*x0))+2*x0)/3
    x = ((q / (x0*x0))+2*x0)/3
    x = ((q / (x0*x0))+2*x0)/3
    x = ((q / (x0*x0))+2*x0)/3
    x = ((q / (x0*x0))+2*x0)/3

    if exponent % 3 == 0:
        exponent = exponent / 3
        svar = math.ldexp(x, exponent)
    elif exponent % 3 == 1:
        exponent = exponent + 2
        exponent = exponent / 3
        svar = exponent_1 * math.ldexp(x, exponent)
    elif exponent % 3 == 2:
        exponent = exponent + 1
        exponent = exponent / 3
        svar = exponent_2 * math.ldexp(x, exponent)
    return svar

a = 27.0
print cube_root(a), 'vs', a**(1.0/3.0)
