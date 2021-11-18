
hasError = True
while hasError:
    try:
        x = int(input())
    except:
        print("Keine Zahl, Versuche es nochmals")
    #nur nützlich für die übersichtlichkeit -> wenn keine exception
    else:
        print("Eingegebene Zahl",x)
        hasError = False
    #wird immer ausgeführt
    finally:
        print("Wird immer ausgeführt")