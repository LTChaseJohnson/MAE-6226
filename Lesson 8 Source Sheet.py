# Importing libraries
import numpy as np
import pyplot.lib as plt
from math import *

# Creating mesh
N = 100
xStart,xEnd = -3.,3.
yStart,yEnd = -2.,2.
x = np.linspace(xStart,xEnd,N)
y = np.linspace(yStart,yEnd,N)
X,Y = np.meshgrid(x,y)

