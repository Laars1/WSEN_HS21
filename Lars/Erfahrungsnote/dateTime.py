timeArray = []
hasError = True

while hasError == True:
    timeInput = str(input('Zeit (HH:MM): '))
    timeArray = timeInput.split(":")
    try:
        if len(timeArray) == 2 and int(timeArray[0]) <= 23 and int(timeArray[0]) >= 0 and int(timeArray[1]) >= 0 and int(timeArray[1]) < 60:
            hasError = False
    except:
        continue


result = int(timeArray[0])*60+int(timeArray[1])
print("Minuten: "+str(result))