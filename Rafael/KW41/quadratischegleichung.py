def qg(A, B, C):
    d = B * B - 4 * A * C
    if d > 0:
        return (42, 42)
    elif d == 0:
        return - B / (2 * A)
    else:
        return ()

print (qg(1, -4, 4))