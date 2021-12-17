import sys

def schreiben():
    try:
        file = open("hallo.txt", "w")
        file.write("Hallo Welt")
        file.close()
    except:
        sys.exit(0)


def lesen():
    try:
        file = open("hallo.txt", "r")
        lines = file.read()
        print(lines)
    except:
        sys.exit(0)




schreiben()
lesen()