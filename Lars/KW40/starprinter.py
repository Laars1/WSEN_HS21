import sys
num = int(input("Grösse: "))

for x in range(1, num+1):
    print(x *"*")


for x in range(1, num+1):
    amSpaces = num-x
    print(amSpaces*" "+ x *"*")

