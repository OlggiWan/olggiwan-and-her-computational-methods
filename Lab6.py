import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

V = 20
w = 1e-9

E = np.linspace(0.001,19.999,200) #setting the parameters between 0 and 20 forces the program to divide by zero, 
#thus creating a mathematical error.

#given functions

def y1(E):
    return (np.tan(np.sqrt((w**2)*E*(cons.m_e*cons.e)/(2*(cons.hbar**2)))))

def y2(E):
    return (np.sqrt((V-E)/E))

def y3(E):
    return (-1*np.sqrt(E/(V-E)))

def oddfunction(E):
    return (y1(E) -y3(E))

def evenfunction(E):
    return(y1(E)-y2(E))
    
#plotting the values

plt.title("Solutions for Values in a Square Potential Well")
plt.ylim([-20, 20])
plt.xlabel("eV of E")
plt.plot(E,y1(E), label='General')
plt.plot(E,y2(E), label='Even Numbered States')
plt.plot(E,y3(E), label='Odd Numbered States')
plt.legend()
plt.show()

#Now introducing binary search

def binary(x1,x2,func):
    f1 = func(x1) 
    f2 = func(x2) 
    if f1>0 and f2>0:
        print("Both are positive.")
    elif f1<0 and f2<0:
        print("Both are negative.")
    else:
        if f1>0 and f2<0:
            xp=x1
            xn=x2
        else:
            xp=x2
            xn=x1
        while np.abs(xp-xn)>=1e-6:
            x = 0.5*(xp+xn)
            f=y1(x) - y3(x)
            if f>0:
                xp = x
            else:
                xn = x
        return x
       
print('First Solution',binary(0.8,1.5,oddfunction))
print('Second Solution',binary(2.2,2.9,evenfunction))
print('Third Solution',binary(4.9,5.1,oddfunction))
print('Fourth Solution',binary(3.3,3.5,evenfunction))
print('Fifth Solution',binary(10,12,oddfunction))
print('Sixth Solution',binary(14.8,15.1,evenfunction))

