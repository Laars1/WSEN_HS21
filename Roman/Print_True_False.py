for P in (True,False):
    for Q in (True,False):
        for R in (True,False):
            print("P = ", P, "Q = ", Q, "R = ",R, " Rechnung: (P and (not Q or R)) and (not (not R and P))", " Lösung der Rechnung = ", (P and (not Q or R)) and (not (not R and P)))
