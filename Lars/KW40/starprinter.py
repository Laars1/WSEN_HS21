import sys
num = int(input("Grösse: "))

for x in range(1, num+1):
    print(x *"*")


for x in range(1, num+1):
    amSpaces = num-x
    print(amSpaces*" "+ x *"*")

z = num-1
x = 1
for i in range(num):
    print(' ' * z + '+' * x + ' ' * z)
    x+=2
    z-=1