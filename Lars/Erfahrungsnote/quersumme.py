
def queersumme(zahl):
    sum = 0
    zahl = abs(zahl)
    for i in str(zahl):
            sum += i
    return sum

print(queersumme(-2903))