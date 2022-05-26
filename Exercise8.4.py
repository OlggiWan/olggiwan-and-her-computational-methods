import numpy as np
import matplotlib.pyplot as plt

"""
The purpose of this laborator activity is to calculate the motion of a pendulum with respect to time. In it, the 
fourth-order Runge-Kutta method is used to calculate the angle of displacement when the pendulum is released at 
179 degrees from the vertical.
"""

theta0 = np.cos(np.radians(179)) #angle from which the pendulum is released
omega0 = 0
g = 9.8 #Earth's gravity
length = 0.1 #length of the pendulum
t0 = 0
tfinal = 7
N = 10000
h = (tfinal-t0)/N

def f(x,t): #inspired by Mark Newman's code in "Computational Physics"
    theta = x[0]
    omega = x[1]
    theta_prime = omega
    omega_prime = (g/length)*np.sin(theta)
    return np.array([theta_prime,omega_prime],float)

time = np.arange(t0,tfinal,h) 
thetapoints = [] #creating a list to be filled later
x = np.array([theta0, omega0],float)

for t in time: #Runge-Kutta!
    thetapoints.append(x[0])
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k1,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6
    
plt.plot(time,thetapoints)
plt.xlabel('Time')
plt.ylabel('Angle theta per second')
plt.show()
