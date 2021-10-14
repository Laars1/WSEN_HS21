i = 0
j = 0
for i in range(1,4):
    for j in range(1,4):
        print(i, "x", j, "=", i*j)


i = 1
j = 1

while i <= 3:
    j = 1
    while j <=3:
        print(i, "x", j, "=", i*j)
        j += 1
    i += 1
