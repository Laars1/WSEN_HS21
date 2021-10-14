#ns = input("Grösse: ")
#n = int(ns)
#i = 0
#while (i < n):
    #i += 1
    #print( i * "*")

    #Wenn i nicht definiert mit += ergibt Endlosschleife bei while loop

#summe = 0
#i = 1
#while (i <= 71):
 #   summe += i
  #  i += 2
#print("summe =", summe)


a = int(input("a = "))
b = int(input("b = "))
r = a % b
while r != 0:
  a = b
  b = r
  r = a % b
print("\nggT =", b)