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

# Defining Freestream perpindicular to line source
Uinf = input('Freestream velocity:')
uFreestream = Uinf * np.ones((N,N),dtype=float)
vFreestream = np.zeros((N,N),dtype=float)
psiFreestream = Uinf * Y

# Defining Source Class
class Source:
    def __init__(self,strength,X,Y):
        self.strength = strength
        self.x,self.y = x,y
    def velocity(self,x,y):
        self.u = self.strength/(2*pi)*(X-self.x)/((X-self.x)**2+(Y-self.y)**2)
        self.v = self.strength/(2*pi)*(Y-self.y)/((X-self.x)**2+(Y-self.y)**2)
    def streamfunction(self,x,y):
        self.psi = self.strength/(2*pi)*np.arctan2((Y-self.y),(X-self.x))

# Defining number of sources in finite line
NSource = input('Number of sources: ')
ySourceStart,ySourceEnd = input('Finite line dimensions (ymax,ymin): ')
SourceStrength = input('Source Strength: ')
SourceDist = np.linspace(ySourceStart,ySourceEnd,Nsource)

# Calculating Source Velocity Fields
