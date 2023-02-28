#!/usr/bin/env python3
# by Valeria Garcés Mendoza
# UNAM 
# gmvaleriaaa@gmail.com
# License: GNU/GLP 3.0

def sucesion(n):
  eval = [1/(10**x) for x in range(1, n+1)]
  ec = ["\\frac{1}{10^{" + str(x) + "}}" for x in range(1, n+1)]
  return eval, ec


n = int(input("Dame n: "))
print(sucesion(n))
