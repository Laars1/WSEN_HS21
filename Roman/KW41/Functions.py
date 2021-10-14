
def stars(n):
    print(n * "*")

# stars(int(input("Gib eine Zahl ein: ")))

def triangel(n):
    while(n > 0):
        stars(n)
        n -= 1

triangel(int(input("Gib eine Zahl ein: ")))