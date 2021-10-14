loop = True
while loop:
    xs = input("x: ")
    try:
        x = int(xs)
    except:
        print("Das ist keine Ganzzahl.")
    else:
        print("Sie haben", x, "eingegeben.")
        break