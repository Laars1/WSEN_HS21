import random

retry = True
while(retry):
    number = random.randint(1,6)
    print("Wurf: "+str(number))
    if(input("Nochmals?") != "Ja"):
        retry = False