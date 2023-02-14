#!/usr/bin/env python3
# by Valeria Garcés Mendoza
# UNAM 
# gmvaleriaaa@gmail.com
# License: GNU/GLP 3.0


# Tarea 1:
#   x = x + r -x **2

import matplotlib.pyplot as plt 
import numpy as np

print("First dynamic system\n x = a*x + b")

def f(x, r):
    return x + r - x**2

# Initial conditions
X0 = np.arange(0.1, 0.2, 0.1)
# 50 sistemas dinámicos

#rs = [0.1, 0.5, 1, 1.1, 1.5, 1.6]

for x0 in X0:
    rs = [0.1, 0.5, 1.0, 1.1, 1.5, 1.6]
    #r = 0.1
    N = 30 #número de pasos

    

    for j in range(len(rs)):
        plt.subplot(2, 3, j + 1)

        print("r = "+str(rs[j]))
        print("x0 = "+str(x0))
        print("N = "+str(N))

        i = np.arange(0, N, 1)  #izq:incluyente, der: excluyente
        #lista de índices i

        x = x0 #variable

        X = [] #vector: valores de evaluación

        for _ in i:
            print(x) 
            X.append(x)
         
            x = f(x, rs[j])

        plt.title('r = ' + str(rs[j]))
        plt.plot(X)

    
    # calcula cada pixel entre el par de puntos; interpolación

#plt.ylim([0, 100])
#plt.yscale('log')
plt.show()

#subplot: tarea

# eje x: iteración
# eje y: valor de variable n