import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

'''
For this laboratory assignment, the goal is to create three plots -- for a square wave, a sawtooth wave, an a 
modulated sine wave, respectively. The task is then to create a Fourier Transform plot for each.
'''
x = np.linspace(0, 1000, 1000) #x-values

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
    y = np.zeros(len(x))
    for i in range(len(x)):
        y = np.sin(np.pi*i/x)*np.sin(20*np.pi*i/x)
    return y
        
plt.plot(modulated_wave(x))
plt.title('Modulated Sine Wave')
plt.show()

#creating Fourier Transforms for each

fourier_square = np.fft.fft(square_wave(x))
plt.plot (np.real(fourier_square*np.conjugate(fourier_square)))
plt.title ('Fourier Transform of Square Wave')
plt.show()

fourier_sawtooth = np.fft.fft(sawtooth_wave(x))
plt.plot (np.real(fourier_sawtooth*np.conjugate(fourier_sawtooth)))
plt.title('Fourier Transform of Sawtooth Wave')
plt.show()

fourier_modulated = np.fft.fft(modulated_wave(x))
plt.plot(np.real(fourier_modulated*np.conjugate(fourier_modulated)))
plt.title('Fourier Transform of Modulated Sine Wave')
plt.show()
