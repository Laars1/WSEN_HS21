#Definition einer Funktion (n) ist Parameter die die Funktion benötigt
def stars(n):
    stars = n * "*"
    
    return stars

#stars(3)

def triangle(n):

    for i in range(1,n+1):
        print(stars(i))

triangle(4)


