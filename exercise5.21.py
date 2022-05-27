import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

"""
This laboratory activity asks us to first calculate the electric potential of two charges, and then to find the 
resulting electric field.
"""

q1 = [45,50] #the charges
q2 = [55,50]
N = 100
h = 10

def r(delta_x,delta_y): #this is the distance formula
    return np.sqrt(delta_x**2+delta_y**2)

x = np.linspace(45, 55, N)
xgrid, ygrid = np.meshgrid(x,x)

potential = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        p1 = np.sqrt((xgrid[i][j] - q1[0])**2 + (ygrid[i][j] - q1[1])**2)
        p2 = np.sqrt((xgrid[i][j] - q2[0])**2 + (ygrid[i][j] - q2[1])**2)
        potential[i][j] = (1/ 4 * np.pi*cons.epsilon_0) * (1/p1 - 1/p2)

plt.imshow(potential)

plt.title("Electric Potential")
plt.show()

dist_x1, dist_y1 = xgrid - q1[0], ygrid - q1[1]
dist_x2, dist_y2 = xgrid - q2[0], ygrid - q2[1]

#calculating the partial derivatives
def Partials(q,delta_x, delta_y):
    return q*(1 / 4 * np.pi*cons.epsilon_0)*(1/r(delta_x, delta_y))

partialx = ((Partials(1, (dist_x1 + h / 2), dist_y1) - Partials(1, (dist_x2 - h / 2), dist_y2)) / h) + ((Partials(-1, (dist_x2 + h / 2), dist_y2) - Partials(-1, (dist_x2 - h / 2), dist_y2)) / h)
partialy = ((Partials(1, dist_x1, (dist_y1 + h / 2)) - Partials(1, dist_x1, (dist_y1 - h / 2))) / h) + ((Partials(-1, dist_x2, (dist_y2 + h / 2)) - Partials(-1, dist_x2, (dist_y2 - h / 2))) / h)

plt.streamplot(xgrid, ygrid, partialx, partialy)
plt.title("Electric Field")
plt.show()

