#frage 10
#meine lösung
# 2/3 Punkte
summe = 0
for i in range(0,10,1):
    wert = 2**i
    summe += wert

print(summe)

#lösung
summe2 = 0
for i in range(10):
    summe2 += 2**i

print(summe2)


#frage 12
#0/3 Punkte
myList = ["PYnative",[4,8,12,16]]

#meine lösung
text = myList[0]
print(text[1])

zahlen=myList[1]
print(zahlen[3])

#lösung
print(myList[0][1])
print(myList[1][3])