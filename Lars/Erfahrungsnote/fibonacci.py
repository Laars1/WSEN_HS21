def fibLis(n):
  if n <= 0:
     return []
  if n == 1:
     return [0]
  result = [0, 1]
  if n == 2:
     return result
  for i in range(2, n):
     result.append(result[i - 2] + result[i - 1])
  return result


userInput = 0
while userInput < 10:
    userInput = int(input("Zahl x >= 10: "))


allElements = fibLis(userInput)
print("Zahl f1: "+str(list(filter(lambda x: x <= userInput, allElements))[-1]))
print("Zahl f2: "+str(list(filter(lambda x: x > userInput, allElements))[0]))