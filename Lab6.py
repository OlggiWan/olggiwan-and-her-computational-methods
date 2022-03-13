import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

V = 20
w = 1e-9

E = np.linspace(0,20,200)

def y1(E):
    return (np.tan(np.sqrt((w**2)*E*(cons.m_e*cons.e)/(2*(cons.hbar**2)))))

def y2(E):
    return (np.sqrt((V-E)/E))

def y3(E):
    return (-1*np.sqrt(E/(V-E)))

plt.title("Solutions for Values in a Square Potential Well")
plt.ylim([-20, 20])
plt.xlabel("eV of E")
plt.plot(E,y1(E), label='General')
plt.plot(E,y2(E), label='Even Numbered States')
plt.plot(E,y3(E), label='Odd Numbered States')
plt.legend()
plt.show()
