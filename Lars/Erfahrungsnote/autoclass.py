class Auto:
    marke: None
    jahr: None
    geschwindigkeit: None

    def __init__(self, marke, jahr, geschwindigkeit = 0):
        self.marke = marke
        self.jahr = jahr
        self.geschwindigkeit = geschwindigkeit

    def beschleunige(self):
        self.geschwindigkeit += 5
    
    def bremse(self):
        if(self.geschwindigkeit >= 5):
            self.geschwindigkeit -= 5
        else:
            self.geschwindigkeit = 0
    
    def hupe(self):
        print(self.marke, "hupt")



test = Auto("Toyota", 2000, 209)

print(test.marke)
print(test.jahr)
print(test.geschwindigkeit)
test.beschleunige()
print(test.geschwindigkeit)
test.bremse()
print(test.geschwindigkeit)
test.hupe()

    