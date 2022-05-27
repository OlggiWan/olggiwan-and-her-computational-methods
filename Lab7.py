import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

'''
For this laboratory assignment, the goal is to create three plots -- for a square wave, a sawtooth wave, and a 
modulated sine wave, respectively. The task is then to create a Fourier Transform plot for each.
'''
x = np.linspace(0, 1000, 1000) #x-values

#Fourier transform from my project!
def fourier(y): #help from a friend! (50 is a little under 10% of our total) Keep biggest coefficients
    fourier_real = np.fft.rfft(y) #rfft is the n-dimensional of real input
    f_array = int(len(fourier_real)) #length of array
    new_array = len(fourier_real)-f_array #removes the last 90% or so from the array
    fourier_real = (fourier_real[:f_array]) #the last element of the array
    fourier_real = np.pad(fourier_real,(0,new_array),'constant') #creates a padded array of zeros after the 50th element
    inverse = np.fft.irfft(fourier_real) #inverse FFT of fourier_real 
    return inverse 

def square_wave(x): 
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < 0.5*x[-1]:
            y[i] = 1
        else:
            y[i] = -1
    return y
                           
plt.plot(x,square_wave(x))
plt.title('Square Wave')
plt.show()
    
#print(x) testing to see if code works
#adapted code from y = np.array([1 if np.floor(2 * a) % 2 == 0 else 0 for a in x]) (thanks, Stackoverflow!)
#plt.plot(square_wave(x,y))

#plotting the functions

def sawtooth_wave(x):
    y = x
    return y

plt.plot(sawtooth_wave(x))
plt.title('Sawtooth Wave')
plt.show()
   
def modulated_wave(x):
    N = (len(x))
    y = np.zeros(len(x))
    for i in range(N):
        y[i] = np.sin(np.pi*i/N)*np.sin(20*np.pi*i/N)
    return y
        
plt.plot(modulated_wave(x))
plt.title('Modulated Sine Wave')
plt.show()

#creating Fourier Transforms for each

plt.plot (fourier(square_wave(x)))
plt.title ('Fourier Transform of Square Wave')
plt.show()

plt.plot (fourier(sawtooth_wave(x)))
plt.title('Fourier Transform of Sawtooth Wave')
plt.show()

plt.plot(fourier(modulated_wave(x)))
plt.title('Fourier Transform of Modulated Sine Wave')
plt.show()
