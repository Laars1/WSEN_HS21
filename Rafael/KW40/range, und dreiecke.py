#seq = range (5)
#for s in seq:
#    print (s)

#prüfungsaufgabe
#for a in range (1, 4):
 #   for b in range (1, 4):
  #      print (a, '*', b, '=', a*b)

#zeigt sterne an
#ns = input("Grösse: ")
#n = int(ns)
#for i in range (1, n + 1):
 #   print(i * "*")



ns = input("Grösse: ")
n = int(ns)
for i in range (1, n + 1):
    print((n - i) * " ", i * "*"),