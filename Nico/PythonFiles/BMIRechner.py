import math

#BMI Rechner ganz einfach und ganz dumm

#y = float(input("Geben Sie bitte ihre Grösse in Meterein: "))
#x = float(input("Geben Sie bitte ihr Gewicht in Kilogramm ein: "))

#bmi = x / (y * y)
#print("Ihr BMI beträgt: " , bmi)

#a = float(input("a: "))
#b = float(input("b: "))
#c = math.sqrt(a*a+b*b)
#print("c", c)

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#Berechnung der Mitternachtsformel: -b +- Wurzel B im Quadrat - 4ac über 2a
#Zuerst den Teil unter der Wurzel berechnen und in einem neuen Wert D speichern
d = b * b - 4 * a * c

#Wird nur ausgeführt wenn d Grösser als 0 ist somit funktioniert die Rechnung!
if (d > 0):
#Danach berechnen wir den x1 im Plusfall 
    x1 = (-b + math.sqrt(d)) / (2*a)

#Berechnung x2 im Negativfall
    x2 = (-b - math.sqrt(d)) / (2*a)

    print("Berechnung im Plusfall: ", x1)
    print("Berechnung im Negativfall: ", x2)

#Berechnung nur in einem Fall sollte unter dem Bruch strich eine 0 oder Negativzahl stehen
elif (d == 0):
    x = -b / (2 * a)
    print("x = ", x)

#Sollte keine IF bedinung erfüllt werden, wird keine
else:
    print("Es ist leider keine Lösung möglich! Prüfe die Eingaben nochmal")
