import math

print(math.pi)

#x = int(input('Geben Sie bitte x ein: '))
#print (x)




#gew = float(input( 'gewicht/kg: '))
#gr = float(input('grösse/m: '))
#print('gew:' , gew)
#print('gr: ', gr)
#BMI = gew / (gr * gr)
#print('BMI: ', BMI)

#a = float(input('a: '))
#b = float(input('b: '))
#print()
#c = math.sqrt (a*a+b*b)
#print('c:' , c)


a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
print()
d = (b *b - 4 * a * c )
if d > 0: 
    x1 = (-b + math.sqrt (d) )/ 2 * a
    x2 = (-b - math.sqrt (d) )/ 2 * a
    print(' x1 =', x1)
    print('x2 =', x2)
elif d == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    print('Keine reelle Lösung')

    

