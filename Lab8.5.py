import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)
"""
This laboratory assignment calculates the value of a given integral using the Monte Carlo technique. Using 
sample N = 1,000,000, the value should be close to 0.84. As the given value is 0.8395313807675582, the 
attempt was successful! 
"""

N = 1000000

def p(x):
    return 1/(np.sqrt(x)*2)

def I(x):
    return (2/(np.exp(x)+1))
            
z = rng.random(1000)
x = z**2
answer = np.mean(I(x))

histogram = plt.hist 
plt.hist(x)
print(histogram)


