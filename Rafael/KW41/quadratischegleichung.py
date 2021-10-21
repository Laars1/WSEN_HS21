
def qg(A, B, C):
    from math import sqrt
    D = B * B - 4 * A * C
    if D > 0:
        return ((-B + sqrt(D)) / (2 * A), (-B - sqrt (D)) / (2 * A))
    elif d == 0:
        return (- B / (2 * A))
    else:
        return ()

print(qg(1, -3, 2))