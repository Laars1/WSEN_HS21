
hasError = True

while hasError:
    try:
        x = int(input())
    except:
        print("Keine Zahl, Versuche es nochmals")
    #nur nützlich für die übersichtlichkeit
    else:
        print("Eingegebene Zahl",x)
        hasError = False