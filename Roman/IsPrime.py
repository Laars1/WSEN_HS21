from sympy import isprime

zahl = int(input("Gib eine Zahl ein: "))
for i in range(zahl,100000000,1):
    if isprime(i):
        print("Zahl:", i, "ist eine primzahl")
        break

