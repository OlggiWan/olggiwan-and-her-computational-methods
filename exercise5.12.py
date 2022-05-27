import scipy.constants as cons
import numpy as np

"""
In this laboratory activity, the goal is to derive the Stefan-Boltzmann constant by evaluating an integral.
"""

a = 0.000001
b = 10
n = 10000
SB = cons.Stefan_Boltzmann

def first_term(T):
    x = (cons.k**4)/(4*cons.pi**2)*(cons.c**2)*(cons.hbar**3)
    return (T**4 *x)

def integrand(x):
    return (x**3)/(np.exp(x)-1)

def Trapezoid(a,b,n): #inspired by Mark Newman's code in his textbook, "Computational Physics"
    
    delta_x = ((b-a)/n)
    s = (0.5*integrand(a)+0.5*integrand(b))

    for k in range (1,n):
        s+=integrand(a+k*delta_x)
        
    return (delta_x*s)

W = first_term(1) * Trapezoid(a,b,n)

print("This is my result using the Trapezoidal integration method: ",W)
print("This is the known value of the Stefan-Boltzmann constant: ",SB)
