# This section deals with the integral problem. (Exercise 4.4)

import numpy as np
import time
import timeit

import time
start=time.time()

def yk(x):
    return (1-x**2)

print(timeit.timeit("1-x**2","x=2"))

def integral(n):
    sum = 0
    h = 2/n
    x_values = np.linspace(-1,1,n)
    
    for x in x_values:
        xk = -1 + (h*k)
    sum = h*xk(yk)
    return (sum)

print(integral)

end=time.time()
print(f"Program took :{end-start} seconds to run")
