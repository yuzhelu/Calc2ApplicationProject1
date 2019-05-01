# Application Project 1
# Code created by Yuzhe Lu

import numpy as np
import matplotlib.pyplot as plt
import scipy as spi
from scipy import integrate
import cmath as math


def simpson(f, a, b, N):

    if N % 2 == 1:
        raise ValueError("N must be an even integer")
    dx = (b-a)/N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S

def trapzoid(f,a, b, N):
    x = np.linspace(a,b,N+1)
    y = f(x)
    y_right = y[1:] # right enpoints
    y_left = y[:-1] # left endpoints
    dx = (b-a)/N
    T = (dx)/2 * np.sum(y_right + y_left)
    return T


a = 0
b = 1
exactValue = 1-math.pi/4

f1 = lambda x: x**2/(1+x**2)

print("Question 1: For n = 8")
print("For 2n = 16, integration value for using simpson methos = ", simpson(f1, a, b, 2*8))

ss = (4*trapzoid(f1, a, b, 16)-trapzoid(f1, a, b, 8))/3
print("for n = 8, S(2n) = (4*[T(2n)-T(n)]/3 is: ", ss)
print("as you can see, they are very similar")

print()
print("Question 2:")

N = [4, 8, 16, 32, 64]

# header
print("\tn\t\tT(n)\t\tS(n)\t\tError T(n)\t\tError S(n)")
y = lambda x: x**2/(1+x**2)

for i in N:
    #trap and simpson
    x = np.linspace(a, b, i + 1)

    val_S = simpson(y, a, b, i)
    val_T = trapzoid(y, a, b, i)

    error_S = abs(val_S - exactValue)/exactValue
    error_T = abs(val_T - exactValue)/exactValue

    print('\t{}\t{:.6f}\t{:.6f}\t\t{:.4E}\t\t\t{:.4E}'.format(i, val_T, val_S, error_T, error_S))


print()
print("Checking using scipy built in functions")
print("\tn\t\tT(n)\t\tS(n)\t\tError T(n)\t\tError S(n)")
for i in N:
    x = np.linspace(a, b, i + 1)
    y = x ** 2 / (1 + x ** 2)
    val_S = spi.integrate.simps(y, x)
    val_T = spi.integrate.trapz(y, x)
    error_S = abs(val_S - exactValue)/exactValue
    error_T = abs(val_T - exactValue)/exactValue

    print('\t{}\t{:.6f}\t{:.6f}\t\t{:.4E}\t\t\t{:.4E}'.format(i, val_T, val_S, error_T, error_S))



## part 6 7 test
print()
print("Number 6.1")
print("\tn\t\tS(n)\t\tError S(n)")
N = [8, 16, 32, 64]
act61 = np.pi * np.log(1 + np.sqrt(3)/2)

for i in N:
    x = np.linspace(0, math.pi, i + 1)
    y = np.log(2+np.cos(x))
    val_S = spi.integrate.simps(y,x)
    error_S = abs(val_S - act61)/act61
    print('\t{}\t{:.10f}\t\t\t{:.5E}'.format(i, val_S, error_S))

print()
print("Number 6.2")
print("\tn\t\tS(n)\t\tError S(n)")
act62 = np.log(32) - 2

for i in N:
    x = np.linspace(0, 2, i + 1)
    y = (x**2 + 1)/(x+2)
    val_S = spi.integrate.simps(y,x)
    error_S = abs(val_S - act62)/act62
    print('\t{}\t{:.10f}\t\t\t{:.5E}'.format(i, val_S, error_S))


