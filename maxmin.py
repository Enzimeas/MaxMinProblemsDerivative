import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


def calcDerivada(funcao, x):
    return sp.diff(funcao, x)


def calcularMaxMin(derivada):
    pontos_criticos = sp.solve(derivada)
    return pontos_criticos


def resolverEquacao(equacao, titulo):
    x = sp.symbols('x')
    derivada = calcDerivada(equacao, x)
    segunda_derivada = calcDerivada(derivada, x)
    pontos_criticos = calcularMaxMin(derivada)

    pontos_criticos_text = [str(pontos_criticos) + ' ' for pontos_criticos in pontos_criticos]
    pontos_criticos_text = ''.join(pontos_criticos_text)

    x_vals = np.linspace(-10000, 10000, 10000)
    y_vals = sp.lambdify(x, equacao, 'numpy')(x_vals)
    deriv_vals = sp.lambdify(x, derivada, 'numpy')(x_vals)

    plt.figure(figsize=(8, 6))

    plt.plot(x_vals, y_vals, label=str(equacao))

    plt.plot(x_vals, deriv_vals, label=str(derivada))

    for ponto_critico in pontos_criticos:
        plt.scatter(ponto_critico, sp.lambdify(x, equacao, 'numpy')(ponto_critico), color='red', marker='o', label='Critical Point')

    if len(pontos_criticos) > 1:
        concavidade = 'MAX | MIN  Possui ponto de inflexao'
    elif segunda_derivada.is_negative:
        concavidade = 'MAX'
    else:
        concavidade = 'MIN'

    plt.title(titulo + '   Pontos criticos: ' + pontos_criticos_text + ' ' + concavidade)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Problema 1: Caixa
resolverEquacao('x*(1-2*x)**2', 'Problema 1: Caixa')

# Problema 2: Jardim
resolverEquacao('-3/4*x**2+6*x', 'Problema 2: Jardim')

# Problema 3: Campo retangular
resolverEquacao('500*x - (x**2)/2', 'Problema 3: Campo Retangular')
