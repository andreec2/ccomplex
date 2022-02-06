import math

def sumaplex(c1,c2):
    """suma de tuplas ordendas"""

    return (c1[0] + c2[0],(c1[1] + c2[1]))

def restaplex(c1,c2):
    """suma de tuplas ordendas"""

    return (c1[0] - c2[0],(c1[1] - c2[1]))

def multiplex(c1,c2):
    """multiplicacion de complejos"""

    real = ((c1[0]*c2[0]) - (c1[1]*c2[1]))
    img = ((c1[0]*c2[1]) + (c2[0]*c1[1]))
    

    return real, img

def diviplex(c1,c2):
    """division de complejos"""

    real = ((c1[0]*c2[0])+ (c1[1]*c2[1]))//((c2[1]** 2) + (c2[0]**2))
    img = ((c2[0]*c1[1]) - (c1[0]*c2[1]))//((c2[1]** 2) + (c2[0]**2))

    real = float(real)
    img = float(img)

    return (real, img)

def modplex(c1):
    """modulo de un complejo"""

    return (c1[0], -c1[1])

def polarplex(c1):
    """pasar de polar a cartesiano"""

    p = ((c1[0]**2) + (c1[1]**2))**0.5
    angulo = math.atan((c1[1])/(c1[0]))

    return (p, angulo)

def carteplex(c1):
    """pasar de polar a cartesiano"""

    real = c1[0] * math.cos(c1[1])
    img = c1[0] * math.sin(c1[1])

    return (real, img)

    

def main():

    print(sumaplex((3.5,7),(4.2,8)))
    print(restaplex((3.5,7),(4.2,8)))
    print(multiplex((3,7),(4,8)))
    print(diviplex((-2,1), (1,2)))
    print(modplex((2,-1)))
    print(polarplex((3,4)))
    print(carteplex((5.0, 0.9272952180016122)))

main()
