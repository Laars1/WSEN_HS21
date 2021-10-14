hasError = True

#Die While Schleife wird so lange ausgeführt, wie hasError ist True

while hasError:
    try:
        x = float(input("Bitte geben Sie eine Zahl ein: "))
        #print("Eingegebene Zahl", x)
        hasError = False

    except:
        print("Du hast keine Zahl eigegeben.. Bitte richtige Zahl eingeben! AMK")

#Else wird nur ausgeführt, wenn es keinen Fehler gibt
    else:
        print("WOOW du hast eine Zahl eingegebebn! Deine Zahl war: ", x)

#finally wird immer ausgeführt, auch wenn das Try Except in einen Fehler läuft. 
    finally:
        print("Bist du Dumm? Ja oder Nein")
        y = str(input("Antworten Sie: "))
        
        if y == "Ja" or y == "J" or y == "j" or y == "ja" or y == "JA":
            print("Ich wusste es du bist ein Honk ;)")
            break
        else: 
            hasError = True
