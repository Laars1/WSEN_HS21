
x = int(input("Gib eine Zahl ein "))
y = int(input("Gib eine Zahl ein "))
z = int(input("Gib eine Zahl ein "))



def zahleingeben(x,y,z):
    if x >= y and x >= z:
        print(x,"ist grösser als", y, "oder als", z)
    if y >= x and y >= z:
        print(y,"ist grösser als", x, "oder als", z)
    else:
        print(z,"Ist am grössten")


zahleingeben(x,y,z)