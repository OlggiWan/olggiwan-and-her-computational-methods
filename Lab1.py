"""
This lab comes in two parts. The first requests that: "A ball is dropped from a tower of height h with an initial velocity of zero. Write a program that
asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring air 
resistance. Use your program to calculate the time for a ball dropped from a 100 m high tower.
"""

g = 9.8
h = 100
time = (((2*h)**0.5)/g)
print(time)
