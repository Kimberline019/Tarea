#explanation.md Introducción al problema a revolver
## Polinomios de Legendre

Los polinomios de Legendre son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva. Tenemos:
\begin{align}
\forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P$_N(x)P_M(x) = \frac{2\delta_{MN}}{2N+1}.
\end{align}
los polinomios están definidos en el intervalo $[-1, 1]$.
Se definen empezando con
\begin{align}
P$_0(x) = 1 \Rightarrow P_1(x) = x,
\end{align}
tal que los siguientes órdenes se generan con la regla de recursividad
\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP$_N(x) -NP_{N-1}(x).
\end{align}
Alternativamente, los polinomios pueden ser definidos de manera iterativa bajo la regla (fórmula de Rodrigues)
\begin{align}
P$_N(x) = \frac1{2^N N!}\frac{d^N}{dx^N}\left[(x^2-1)^N\right].
\end{align}

Si se quiere evaluar una integral utilizando distintos
intervalos de integración, primero se realiza el cálculo
de los puntos de muestreo $x$_k$ y los pesos $w_k$ 
en el intervalo $[-1, 1]$. Esto por razones historicas se le
da este valor estandar y seguidamente, podemos escalar los
parámetros para ser modificados a un intervalo $[a, b]$ deseado.

# Cuadratura Gaussiana

Cuando ya se han calculado las posiciones y los pesos entonces, la integral esta dada por:
\begin{align}
\int$_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w$_k f(x_k).
\end{align}
donde:
  * $w_k$ son los "pesos"
  * $x_k$ son los puntos de muestreo
  
  Para la cuadratura Gaussiana:
  * Los puntos de muestreo se escogen de manera tal que **no son equidistantes**. Esto introduce más grados de libertad para la misma discretización en $N$ subregiones.
  * Es exacta para un polinomio de orden $(2N - 1)$.

 Los pesos y puntos de muestreo se eligen tal que:
  * $x$_k$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre $P_N(x)$ de orden $N$.
  * Los pesos se eligen tal que:
      - $\displaystyle w_k = \left[\frac{2}{1-x^2}\left(\frac{dP_N}{dx}\right)^{-2}\right]_{x={x$_k}}$, con $x_k$ que cumple $P_N(x_k)=0$


