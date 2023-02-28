#!/usr/bin/env python3
# by Valeria Garcés Mendoza
# UNAM 
# gmvaleriaaa@gmail.com
# License: GNU/GLP 3.0

n = 10

sucesion = []

for i in range(1, n+1):
  eval = 1/(10**i)
  ec = "\\frac{1}{10^{" + str(i) + "}}"
  sucesion.append(tuple([eval, ec]))

#\frac{1}{10^{n}}
print(sucesion)