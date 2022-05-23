import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
from pyhdf.SD import SD, SDC
import os 
import glob
import time

"""
This project analyses Lake Surface Water Temperature (LSWT) trends for Lake Washington between 1/1/2002 and 12/31/2020. 
This analysis of temperature variation was conducted using daily observations from the Moderate Resolution
Imaging Spectroradiometer (MODIS) over the lake and its surrounding area. 

This is part of a bigger research project conducted by Prof. Bah, and some of the code was inspired by its 
MATLAB equivalent. https://moonbooks.org/Articles/How-to-read-a-MODIS-HDF-file-using-python-/ was also incredibly 
helpful.

The following will also contain a Fourier analysis. The code was designed to be easily adaptable for use of other
lakes with helpful comments.
"""
start = time.time()#to test time complexity, let's see how long this program takes to run!

dirname = "/Users/HNorouzi/Desktop/Global_Lakes_Project/Raw_Data/H09V04/" #insert directory here
x = 9 #The tile number for Lake Washington is H09V04. These are Cartesian Coordinates.
y = 4
longlat_range = [47.60607,47.61984,-122.26706,-122.24389] #Lake Washington longitude and latitude surrounding values
count = 0

mlat = np.zeros([1200,1200])
mlon = np.zeros([1200,1200])

def locator(x,y, longlat_range):
    indices = []
    for i in range(1,1200): #determines the amount of pixels in the lake data
        for j in range (1,1200):
            mlat[i,j] = np.rad2deg(((y+((i-1)/1200))-9)/(-9))*np.pi/2
            mlon[i,j] = (((x+((j-1)/1200)-18)*10))/np.cos(np.deg2rad(mlat[i,1]))
            if mlat[i,j]>longlat_range[0] and mlat[i,j]<longlat_range[1] and mlon[i,j]>longlat_range[2] and mlon[i,j]<longlat_range[3]:
                indices.append([i,j])
                #print(i,j) No longer needed, but this was used to check that the values were correct.
    return indices #we used count to debug

indices = locator(x,y,longlat_range)
count = len(indices)
#print(indices) This can be helpful for debugging.

#file_names = glob.glob(dirname+'*.hdf') Alas, poor glob. I (never) knew him, Horatio.
file_names = os.listdir(dirname)
NT = len(file_names) #that's a lot of files! (number of timesteps)
size = (count,NT) 
all_data = np.ones(size)
years = np.arange(0,NT)

#the following arranges the order of the hdf files chronologically
temp = np.zeros(NT)
for i in range (NT):
    temp[i] = np.int64(file_names[i][28:37])
sorting = np.argsort(temp)
#print(temp[sorting]) this can be used for debugging

for i in range(NT):
    #over the number of times in the files
    lake = SD(dirname + file_names[sorting[i]], SDC.READ)
    sds_obj = lake.select('LST_Day_1km') # select sds
    data = sds_obj.get() # get sds data
    #print(data)
    for j in range(count): #count is the number of pixels in each lake
        id1 = indices[j][0]
        id2 = indices[j][1]
        all_data[j,i] = data[id1,id2]
        
all_data = np.loadtxt('lake.csv')
#print(all_data)
data_y = all_data[0,:]
data_scaled = data_y*0.02
non_zero_avg = np.mean(data_scaled[data_scaled>0])
print("The average value for this lake's temperature is: ",non_zero_avg)#this prints the average temperature of the lake, and is helpful when determining 
#which value to use to get rid of zero-values.
data_scaled[data_scaled<200]=non_zero_avg #this gets rid of the values that equal zero, as well as outliers below 200

#our Fourier transform
def fourier(y, per=0.9): #help from a friend! (50 is a little under 10% of our total)
    fourier_real = np.fft.rfft(y) #rfft is the n-dimensional of real input
    f_array = int(len(fourier_real)*per) #length of array
    new_array = len(fourier_real)-f_array #removes the last 90% or so from the array
    fourier_real = (fourier_real[:f_array]) #the last element of the array
    fourier_real = np.pad(fourier_real,(0,new_array),'constant') #creates a padded array of zeros after the 50th element
    inverse = np.fft.irfft(fourier_real) #inverse FFT of fourier_real
    return inverse

#print(all_data)
data_y = all_data[0,:]
data_scaled = data_y*0.02
non_zero_avg = np.mean(data_scaled[data_scaled>0])
print(non_zero_avg)
data_scaled[data_scaled<200]=non_zero_avg
plt.scatter(years, data_scaled, s=1, marker='.')
plt.ylim([250,350])
labels = ['2002','2003','2004','2005','2006','2007','2008', '2009', '2010', '2011', '2012', '2013', '2014','2015','2016', '2017','2018','2019','2020']
#plt.xticks(np.arange(2002, 2020, step=366))  # Set label locations.
#plt.xtics = (years,labels, rotation='vertical')
plt.xlabel('Julian Days between 2002 and 2020 (time)')
plt.ylabel('Temperature in Kelvin')
plt.suptitle("Lake Washington Surface Temperature (Day)")
trendline = np.polyfit(years.flatten(), data_scaled.flatten(),1) #thanks, Stackoverflow!
p = np.poly1d(trendline)
plt.plot(years,p(years),"r--")
plt.title("y=%6fx+%.6f"%(trendline[0],trendline[1]))
plt.show()

"""
As seen in the accompanying figure, the LSWT of Lake Washington has been progressively warming over 
the last 18 years.
"""

data_scaled = data_scaled - non_zero_avg
mean = np.mean(data_scaled)
#print(mean)
data_scaled = data_scaled - np.mean(data_scaled)
#lake_fourier = np.fft.rfft(data_scaled)
#lake_fourier = lake_fourier - non_zero_avg 
lake_fourier = fourier(data_scaled)
#plt.xlim([0,50])
#plt.plot(np.real(lake_fourier*np.conjugate(lake_fourier)))
plt.plot(fourier(data_scaled))
plt.show()
