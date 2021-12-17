print(f"{'Zeichen':^8}{'Unicode':^8}")
# plus eins da auch j berücksichtigt werden soll
for code in range(ord('A'), ord('J')+1):
    # f string bilden
    #ord durch str ersetzen da wir einen string wollen
    print(f"{chr(code):^8}{str(code):^8}")