import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits import mplot3d
from noise import NoiseHandler
mpl.use('macosx')

#Visualization of Line
axis = plt.axes(projection="3d")
x_data = np.arange(0, 5, (0.1))
y_data = np.arange(0, 5, (0.1))
z_data = x_data * y_data

axis.plot(x_data, y_data, z_data)
#plt.show()

#Visualization of Surface Plot
axis = plt.axes(projection="3d")
x_data = np.arange(0, 5, (0.1))
y_data = np.arange(0, 5, (0.1))
z_data = np.arange(0, 5, (0.1))

noise_handler = NoiseHandler()
noise_handler.genTer(100, (1.0, 3), (0.5, 5))
x_data, y_data, Z = noise_handler.convert_matplotlib()
Z = np.array(Z)

#print (x_data)
X, Y = np.meshgrid(x_data, y_data)
#print(X)
#Z = X * Y


axis.plot_surface(X, Y, Z)
plt.show()