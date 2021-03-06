import matplotlib.pyplot as plt
import numpy as np

#Creating the plot for the Deltoid Curve:

theta = np.linspace(0.0,2*np.pi)

x=(2*np.cos(theta))+(np.cos(theta*2))
y=(2*np.sin(theta))-(np.sin(theta*2))

plt.plot(x,y)
_=plt.title('Deltoid Curve')
plt.show()

#Creating the plot for the Galilean Spiral

polar_theta = np.linspace(0.0,10000*np.pi)
r = (polar_theta)*2

#converting to Cartesian Coordinates

polar_x = r*np.cos(polar_theta)
polar_y = r*np.sin(polar_theta)

plt.plot(polar_x,polar_y)
_=plt.title ("Galilean Spiral")
plt.show()

#Creating the plot for Fey's Function

Fey_theta = np.linspace(0.0,24*np.pi,7000)
r_Fey = (np.exp(np.cos(Fey_theta) - 2*np.cos(Fey_theta*4) + np.sin(Fey_theta/12)**5))

x_Fey = r_Fey*np.cos(Fey_theta)
y_Fey = r_Fey*np.sin(Fey_theta)

plt.plot(x_Fey,y_Fey)
_=plt.title ("Fey's Function")
plt.show()

#putting them all together

fig,axs = plt.subplots(3)
axs[0].plot(x,y)
axs[1].plot(polar_x,polar_y)
axs[2].plot(x_Fey,y_Fey)
plt.show()
