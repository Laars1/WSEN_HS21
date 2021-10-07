zahl = int(input("Gebe eine Zahl ein: "))
zahl += 1

for i in range(1,zahl):
        print(" " * (zahl - i), "*" * i)