# x = int(input())

# print("x: "+ str(x+x))

x = 0
for i in range(1,11):
    x += i**2
print(x)

for i in range(4):
    print(i)

liste = []
liste.append(x)


print(bin(5|6))
print(bin(5&6))

o = 0
for i in range(1,100,2):
    o += i

print(o)


def namensliste():
    liste = []
    abbruch = False
    while abbruch == False:
        name = input("Name eingben: ")
        if name == ".":
            abbruch = True
            print(liste)
        else:
            liste.append(name)
