print("Sprit")

a = input("Gebe Kilometer ein die du fahren willst >> ")
a = int(a)

print("Es wird auf kilometer gerechnet")

e = input("Gebe ein wie viel Liter dein Auto verbraucht  >> ")
e = int(e)

print("Dein verbrauch wird mit liter gerechnet")

e = e / a

print("Dein verbrauch pro kilometer betraegt", e)

c = input("Gebe ein wie viel Kilometer du fahren willst >> ")
c = int(c)

e = e * c

print("Dein verbrauch für", c, "Kilometer beträgt", e, "Liter")