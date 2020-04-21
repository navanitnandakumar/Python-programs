import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as dt
from matplotlib.colors import LightSource

#download .nc topography data from --> http://apdrc.soest.hawaii.edu/las/v6/dataset?catitem=1285
#it contains bathymetry of the Indian ocean
#save as netCDF file
filestr = 'yourfilenamegoeshere.nc'

#file pointer
ncfile = dt(filestr, 'r')

#extracting variables and type casting them as numpy arrays
lon = np.array(ncfile.variables['LON1_2758'][:], dtype=np.float64)
lat = np.array(ncfile.variables['LAT1_2099'][:], dtype=np.float64)
time = np.array(ncfile.variables['TIME'][:], dtype=np.float64)
TOPO2 = np.array(ncfile.variables['TOPO2'][0,:], dtype=np.float32)

#replacing all the occurance of 1e33 (indicates land) with NaN (not a number)
TOPO2[TOPO2 == 1e33] = np.NaN

#to plot the figure
plt.figure()

#azdeg = azimuth
#alt deg = altitude
ls = LightSource(azdeg=270, altdeg=20)

#for activating the filter, remove '#' and run

#a contour filter. features are somewhat visible -
# plt.contourf(TOPO2)

#a hillshade filter. features have distinctive colours -
#plt.imshow(ls.hillshade(TOPO2, vert_exag=10), origin='lower')

#a hillshade filter with blend mode as 'overlay'. featurs can be distinguished easily -
#plt.imshow(ls.shade(TOPO2, cmap=plt.cm.gist_earth, vert_exag=10, blend_mode='overlay'), origin='lower')

#a hillshade filter with blend mode as 'hsv'. features are clearly visible -
#plt.imshow(ls.shade(TOPO2, cmap=plt.cm.gist_earth, vert_exag=10, blend_mode='hsv'), origin='lower')

#to show the plot
plt.show()
