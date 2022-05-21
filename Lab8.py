import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
%matplotlib inline

"""
This is a particularly delightful laboratory assignment that follows the path of a particle on a random walk, 
through the use of the Monte Carlo technique to trace Brownian motion.
"""

rng = np.random.default_rng(seed=42) #I chose seed 42 as it's the number that represents the Ultimate Answer to
#Life, the Universe, and Everything, according to Galactic Hitchhikers everywhere, but you may choose any
#that you wish.

#f,ax=plt.subplots() These are commented out because they were found to not work, but I left them in as they are 
#a part of my journey in this assignment.
#ax.scatter([-50,50],[-50,50])
#L = 101
i = 0
j = 0
N = 100000 #number of moves

#directions = dict(0:i+1, 1:i-1, 2:j+1, 3:j-1) 

def up(i,j):
    return i,j+1

def down(i,j):
    return i,j-1

def left(i,j):
    return i-1,j

def right(i,j):
    return i+1,j

move = {0:up, 1:down, 2:left, 3:right} #my dictionary!

#i,j=move[0](i,j)

#creating a list to store the values
position = []
position.append([i,j])

motion = rng.integers(low=0,high=3,size=N) #dictionary index between 0 and 3
for k in range (len(motion)):
    i,j = (move[motion[k]](i,j))
    
    #creating boundary conditions for the particle
    if i<=-50:
        i=i+1
    elif i>=50:
        i=i-1
    elif j<=-50:
        j=j+1
    elif j>=50:
        j=j-1
    position.append([i,j]) #saves each i and j


#plotting the animation

fig = plt.figure()
ax = plt.axes(xlim=(-70, 70), ylim=(-70, 70))
particle = plt.Circle((0,0),radius=3,facecolor='green')
ax.add_patch(particle)

def init():
    particle.center = (0,0)
    ax.add_patch(particle)
    return particle,

def animate(i):
    x = position[i][0]
    y = position[i][1]
    particle.center = (x,y)
    return particle,
    
anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)
anim.save('brownian_motion.mp4') 

#let's name a gif, too! Why not?

writergif = animation.PillowWriter(fps=30) 
anim.save('brownian_motion.gif',writer=writergif)
plt.show()
