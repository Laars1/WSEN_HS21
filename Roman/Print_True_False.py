for P in (True,False):
    for Q in (True,False):
        for R in (True,False):
            print(P, Q, R, (P and (not Q or R)) and (not (not R and P)))
