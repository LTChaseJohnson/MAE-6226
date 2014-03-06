# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
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
xSourceStart,xSourceEnd = 0.0,0.0
SourceStrength = input('Source Strength: ')
SourceDisty = np.linspace(ySourceStart,ySourceEnd,NSource)
SourceDistx = np.linspace(xSourceStart,xSourceEnd,NSource)
source = np.empty(NSource)

# Calculating Source Velocity Fields
for i in range(NSource):
    source[i] = Source(SourceStrength,SourceDistx[i],SourceDisty[i])
    source[i].velocity(X,Y)
    source[i].streamfunction(X,Y)

# Superposition Principle
for j in source:
    u = np.add(u,j.u) + uFreestream
    v = np.add(v,j.v) + vFreestream

# plotting
size = 8
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.grid(True)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,u,v,density=3,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(xSource*np.ones(NSource,dtype=float),ySource,c='#CD2305',s=80,marker='o')
cont = plt.contourf(X,Y,np.sqrt(u**2+v**2),levels=np.linspace(0.0,0.1,10))
cbar = plt.colorbar(cont)
cbar.set_label('U',fontsize=16);
plt.show()