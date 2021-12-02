from sympy import isprime

userInput = 0
while userInput < 10:
    userInput = int(input("Zahl x >= 10: "))

while isprime(userInput) != True:
    userInput += 1


print("Zahl p: "+str(userInput))