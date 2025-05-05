#tutorials
```python:
import numpy as np
def gaussxw (N):
    x,w = np.polynomial.legendre.leggauss(N) 
    """""
    Calcula los nodos y pesos para la cuadratura de Gaussiana 
    en el intervalo [-1, 1].

    Parámetros:
    N: Número de nodos.

    Retorna:
    x: Arreglo de nodos.
    w: Arreglo de pesos asociados a los nodos.
    """
    
    return x, w

def gaussxwab(a, b, x, w):
    x, w = np.polynomial.legendre.leggauss(N)
    """
    Realiza el cambio de variable para transformar los nodos
    y pesos de [-1, 1] al intervalo [a, b].

    Parámetros:
    a: Límite inferior del nuevo intervalo.
    b: Límite superior del nuevo intervalo.
    x: Nodos en el intervalo [-1, 1].
    w: Pesos correspondientes en [-1, 1].

    Retorna:
    x(mapeado): Nodos transformados al intervalo [a, b].
    w_(mapeado): Pesos transformados para el intervalo [a, b].
    """


  
    
    return x, w

def gaussxwab(a, b, x, w):
   
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

# Obtener nodos y pesos para distintos N
x1, w1= gaussxw(2)

#  N=3

x2, w2= gaussxw(3)

# N = 4 
x3, w3= gaussxw(4)

# Imprimir nodos y pesos en [-1, 1]

print(x1,w1)
print(x2,w2)
print(x3,w3)


# Transformar nodos y pesos en el intervalo [0, 2]
a=0
b=2
x1_esc, w1_esc = gaussxwab(a, b, x1, w1)
x2_esc, w2_esc = gaussxwab(a, b, x2, w2)
x3_esc, w3_esc = gaussxwab(a, b, x3, w3)

# Imprimir nodos y pesos escalados
print(x1_esc, w1_esc)
print(x2_esc, w2_esc)
print(x3_esc, w3_esc)

def integral(vin):
    return (vin**4) - 2*(vin**3) + 1
    """
    Función a integrar: f(x) = x^4 - 2x^3 + 1

    Parámetros:
    vin: Valor o arreglo de valores de entrada.

    Retorna:
     Resultado de aplicar la función a vin.
    """
  

    

#Calcular la integral aproximada con los nodos/pesos escalados

result_n1= np.sum(w1_esc *integral(x1_esc))
result_n2= np.sum(w2_esc *integral(x2_esc))
result_n3= np.sum(w3_esc *integral(x3_esc))

#Imprimir resultados

print(result_n1)
print(result_n2)
print(result_n3)

