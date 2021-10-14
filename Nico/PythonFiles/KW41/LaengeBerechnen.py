
def laengeBerechnen(x,y):
    from math import sqrt
    return sqrt(x * x + y * y)

#print(laengeBerechnen(3,4))

def quadratischeGleichungBerechnen(A,B,C):
    import math

    d = B * B - 4 * A * C
    print(d)
    
    if d > 0:
        x1 = (-B + math.sqrt(d)) / (2*A)
        x2 = (-B - math.sqrt(d)) / (2*A)
        return "Es gibt 2 Lösungen. Lösung Nr:1 " , x1, "Lösung Nr.2 " ,x2
    
    elif d == 0:
        return "Es gibt nur eine Lösung: " - B / (2 * A)

    else:
        return("Keine Lösung")
    
print(quadratischeGleichungBerechnen(7,2,-9))