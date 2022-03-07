import matplotlib.pyplot as plt
import numpy as np

# This section of the lab deals with the derivative problem. (Exercise 4.3)

print("The following program calculates the derivative of a function, then tests its accuracy as sigma becomes increasingly smaller.")

delta = np.array ([1e-2, 1e-4, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-12, 1e-14])
x = 1

def limit (x):
    return (x*(x-1))

derivative = ((limit(x+delta) - limit(x))/delta)

print("These are the derivative values: ",derivative)

plt.xscale("log")
plt.ylim([0.998, 1.002])
plt.xlabel("Delta")
plt.ylabel("Derivative")
_=plt.plot(delta,derivative)
plt.show()
