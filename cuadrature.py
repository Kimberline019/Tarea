#!/usr/bin/env/ python3
import numpy as np
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)

    return x, w
def gaussxwab(a, b, x, w):

    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w
x1, w1= gaussxw(2)

# Luego para $N=3$
# Su código aquí
x2, w2= gaussxw(3)

# Y finalmente para $N=4$
# Su código aquí
x3, w3= gaussxw(4)

#Para N = 5
x4, w4= gaussxw(5)

#Para N = 6
x5, w5= gaussxw(6)


#Para N = 7
x6, w6= gaussxw(7)

#Para N = 8
x7, w7= gaussxw(8)

#Para N = 9
x8, w8= gaussxw(9)


#Para N = 10
x9, w9= gaussxw(10)

#Para N = 11
x10, w10= gaussxw(11)

#Para N = 12
x11, w11= gaussxw(12)


print(x1,w1)
print(x2,w2)
print(x3,w3)
print(x4,w4)
print(x5,w5)
print(x6,w6)
print(x7,w7)
print(x8,w8)
print(x9,w9)
print(x10,w10)
print(x11,w11)


a=0
b=np.pi
x1_esc, w1_esc = gaussxwab(a, b, x1, w1)
x2_esc, w2_esc = gaussxwab(a, b, x2, w2)
x3_esc, w3_esc = gaussxwab(a, b, x3, w3)
x4_esc, w4_esc = gaussxwab(a, b, x4, w4)
x5_esc, w5_esc = gaussxwab(a, b, x5, w5)
x6_esc, w6_esc = gaussxwab(a, b, x6, w6)
x7_esc, w7_esc = gaussxwab(a, b, x7, w7)
x8_esc, w8_esc = gaussxwab(a, b, x8, w8)
x9_esc, w9_esc = gaussxwab(a, b, x9, w9)
x10_esc, w10_esc = gaussxwab(a, b, x10, w10)
x11_esc, w11_esc = gaussxwab(a, b, x11, w11)
print(x1_esc, w1_esc)
print(x2_esc, w2_esc)
print(x3_esc, w3_esc)
print(x4_esc, w4_esc)
print(x5_esc, w5_esc)
print(x6_esc, w6_esc)
print(x7_esc, w7_esc)
print(x8_esc, w8_esc)
print(x9_esc, w9_esc)
print(x10_esc, w10_esc)
print(x11_esc, w11_esc)

def integral(vin):
    return np.sin(vin**2)

result_n1= np.sum(w1_esc *integral(x1_esc))
result_n2= np.sum(w2_esc *integral(x2_esc))
result_n3= np.sum(w3_esc *integral(x3_esc))
result_n4= np.sum(w4_esc *integral(x4_esc))
result_n5= np.sum(w5_esc *integral(x5_esc))
result_n6= np.sum(w6_esc *integral(x6_esc))
result_n7= np.sum(w7_esc *integral(x7_esc))
result_n8= np.sum(w8_esc *integral(x8_esc))
result_n9= np.sum(w9_esc *integral(x9_esc))
result_n10= np.sum(w10_esc *integral(x10_esc))
result_n11= np.sum(w11_esc *integral(x11_esc))
print(result_n1)
print(result_n2)
print(result_n3)
print(result_n4)
print(result_n5)
print(result_n6)
print(result_n7)
print(result_n8)
print(result_n9)
print(result_n10)
print(result_n11)


import matplotlib.pyplot as plt
import numpy as np

# Definimos la función a integrar
def f(x):
    return np.sin(x**2)

# Lista de nodos y pesos escalados ya calculados
x_list = [x1_esc, x2_esc, x3_esc, x4_esc, x5_esc, x6_esc, x7_esc, x8_esc, x9_esc, x10_esc, x11_esc]
w_list = [w1_esc, w2_esc, w3_esc, w4_esc, w5_esc, w6_esc, w7_esc, w8_esc, w9_esc, w10_esc, w11_esc]

N_values = list(range(2, 13))  # N = 2 a 12
I_values = [np.sum(w * f(x)) for x, w in zip(x_list, w_list)]

# Graficar
plt.figure(figsize=(8, 5))
plt.plot(N_values, I_values, marker='o', linestyle='-', color='darkred')
plt.title(r"Aproximación de $\int_0^\pi \sin(x^2)\,dx$ con Cuadratura Gaussiana")
plt.xlabel("N (número de nodos)")
plt.ylabel("Valor aproximado de la integral I")
plt.grid(True)
plt.tight_layout()
plt.show()



