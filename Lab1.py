"""
This lab comes in two parts. The first requests that: "A ball is dropped from a tower of height h with an initial velocity of zero. Write a program that
asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring air 
resistance. Use your program to calculate the time for a ball dropped from a 100 m high tower.
"""

g = 9.8
h = 100
time = (((2*h)**0.5)/g)
print(time)

"""
The second part asks: A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away. Write a program to
ask the user for the value of x and the speed v as a fraction of the speed of light c, then print out the time in years that the spaceship takes to reach
its destination (a) in the rest frame of an observer on Earth and (b) as perceived by a passenger on board the ship. Use your program to calculate the 
answers for a planet 10 light years away with v = 0.99c.
"""
import numpy as np

ly = 0.99
v = 10
gamma = 1/((1-v**2)**0.5)
dilation = ly/gamma
earth = ly/v
spaceship = dilation/v

print("This is time, in years, that passes on the rest frame of the observer on Earth", earth)
print("This is the time, in years, that the spaceship takes to get to its destination, as perceived by as passenger on board the ship ",spaceship)


