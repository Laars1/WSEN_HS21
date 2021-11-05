
zahl = int(input("Gebe eine Zahl ein: "))

#plus 1, da range immer eins weniger als das Maximum macht
zahlen = range(1,zahl +1,2)

i = 0
for a in zahlen:
    print(" " * (zahl -i), "*" * a)
    i += 1

