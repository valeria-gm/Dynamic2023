#!/usr/bin/env python3
# Valeria Garcés Mendoza
# UNAM 
# gmvaleriaaa@gmail.com
# License: GNU/GLP 3.0

# Triángulo Equilátero

import matplotlib.pyplot as plt
import numpy as np
import random

# Longitud del triángulo
L = random.randint(1,50)

# Coordenadas de los vértices
# Tres ángulos de igual tamaño que son todos de 60° y cada lado tiene la misma longitud
x1, y1 = 0, 0
x2, y2 = L, 0
# The height of an equilateral triangle is sqrt(3) * side/ 2
x3, y3 = L/2, L*np.sqrt(3)/2

# Recta que une los vértices 1 y 2
m12 = (y2-y1)/(x2-x1)
b12 = y1 - m12*x1
x12 = np.linspace(x1, x2, 100)
y12 = m12*x12 + b12

# Recta que une los vértices 2 y 3
m23 = (y3-y2)/(x3-x2)
b23 = y2 - m23*x2
x23 = np.linspace(x2, x3, 100)
y23 = m23*x23 + b23

# Recta que une los vértices 3 y 1
m31 = (y1-y3)/(x1-x3)
b31 = y3 - m31*x3
x31 = np.linspace(x3, x1, 100)
y31 = m31*x31 + b31

plt.plot(x12, y12, 'b')
plt.plot(x23, y23, 'b')
plt.plot(x31, y31, 'b')
plt.title("Triángulo equilátero")
plt.axis('equal')
plt.show()
