#reference.md
```python:
import numpy as np

def gaussxw(N):
   
    """
    Calcula los nodos y pesos para la cuadratura de Gauss-Legendre en el intervalo [-1, 1].

    Parameters
    ----------
    N : int
        Número de puntos (nodos).
   
    Returns
    -------
    x : Nodos de integración.
    w : Pesos correspondientes a los nodos.

    Ejemplo:
    --------
    >>> x, w = gaussxw(3)
    >>> x
    ([-0.77459667,  0.        ,  0.77459667])
    >>> w
    array([0.55555556, 0.88888889, 0.55555556])
    """
    return np.polynomial.legendre.leggauss(N)


def gaussxwab(a, b, x, w):
    """
    Escala los nodos y pesos desde [-1, 1] al intervalo [a, b].

    Parameters
    ----------
    a : Límite inferior del intervalo.
    b :  Límite superior del intervalo.
    x : Nodos en [-1, 1].
    w : Pesos en [-1, 1].

    Returns
    -------
    x:Nodos escalados al intervalo [a, b].
    w :Pesos escalados para el nuevo intervalo.

    Ejemplo:
    --------
    >>> x, w = gaussxw(2)
    >>> x, w = gaussxwab(0, np.pi, x, w)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def integral(vin):
    """
    Función a integrar: sin(x²)

    Parameters
    ----------
    vin : Valor de entrada.

    Returns
    -------
    
        Resultado de aplicar sin(x^2) elemento a elemento.

    Ejemplo
    --------
    >>> integral(np.pi)
    1.2246467991473532e-16
    >>> integral(np.array([0, np.sqrt(np.pi)]))
    array([0.        , 0.98776595])
    """
    return np.sin(vin**2)


