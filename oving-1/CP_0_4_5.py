import math


a = 3344556600
b = 1.2222222

# Hvis lengden er a og hypotenus er h, så får vi likningen
# h - a = sqrt(pow(a, 2) + pow(b, 2)) - a som gir oss forskjellen mellom
# lengden og hypotenus. Vi ser at vi får subtraksjon av to nesten like tall slik
# at python bare ville gitt oss null hvis vi regner ut dette uttrykket.
# Løsningen er å skrive om likningen til noe som unngår denne type subtraksjon:
#
# sqrt(pow(a, 2) + pow(b, 2)) - a = ((sqrt(pow(a, 2) + pow(b, 2)) - a ) * (sqrt(pow(a, 2) + pow(b, 2)) + a)) / (sqrt(pow(a, 2) + pow(b, 2)) + a)
# 
# which can be written to
# pow(b, 2) / (sqrt(pow(a, 2) + pow(b, 2)) + a)

diff = pow(b, 2) / (math.sqrt(pow(a, 2) + pow(b, 2)) + a)

print("The difference between the length and the hypotenus is: ", diff)