import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

"""
For this laboratory activity, the goal is to measure the trajectory of a cannonball with air resistance. (The very same,
much-neglected air resistance from freshman Physics! It can now finally feel some love and validation.) 
"""

m = 1 #cannonball mass
R = 0.08 #radius
C = 0.47 #coefficient of drag
rho = 1.22 #density of air
g = 9.8
#F = np.pi(0.5)*(R**2)*rho*C*(v**2)
N = 1000
h = 1
vx = 100*np.cos(np.radians(30))
vy = 100*np.sin(np.radians(30))
time = np.arange (0,N,h)
xpoints = []

def Newton(vx,vy): #F=ma! (This was made during my function obsession -- so I decided to create functions within functions.)
    def x_prime(vx,vy):
        return vx*(np.sqrt(vx**2+vy**2))
    def y_prime(vx,vy):
        return vy*(np.sqrt(vx**2+vy**2))
    def x_diff(vx,vy):
        return ((-1*np.pi*R**2*rho*C)/2*m*x_prime(vx,vy))
    def y_diff(vx,vy):
        return -g+(-1*np.pi*R**2*rho*C)/2*m*y_prime(vx,vy)
    return (x_diff(vx,vy),y_diff(vx,vy))
    
print(Newton(vx,vy)) #testing! 
