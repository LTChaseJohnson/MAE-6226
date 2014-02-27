# Importing our libraries
import numpy as np
import matplotlib.pyplot as plt
from math import *

# Creating our mesh grid
N = 100
xStart,xEnd = -4.0,4.0
yStart,yEnd = -4.0,4.0
x = np.linspace(xStart,xEnd,N)
y = np.linspace(yStart,yEnd,N)
X,Y = np.meshgrid(x,y)

# Creating Source Class
class Source:
    def __init__ (self,strength,x,y):
        self.strength = strength
        self.x,self.y = x,y
    def velocity(self,X,Y):
        self.u = self.strength/(2*pi)*(X-self.x)/((X-self.x)**2+(Y-self.y)**2)
        self.v = self.strength/(2*pi)*(Y-self.y)/((X-self.x)**2+(Y-self.y)**2)
    def stream(self,X,Y):
        self.psi = self.strength/(2*pi)*np.arctan2((Y-self.y),(X-self.x))

# User inputs for source strength and position
SourceStrength = input('Source Strength: ')
xSource,ySource = input('Source position (x,y): ')

# Calculating source characteristics
source = Source(SourceStrength,xSource,ySource)
source.velocity(X,Y)
source.stream(X,Y)

# Calculating image based on x-axis symmetry
sourceimage = Source(SourceStrength,xSource,-ySource)
sourceimage.velocity(X,Y)
sourceimage.stream(X,Y)

# Applying superposition principle
us = source.u + sourceimage.u
vs = source.v + sourceimage.v
psis = source.psi + sourceimage.psi

# Plotting combined velocity field
size = 10
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.title('Combined Source and Image')
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,us,vs,density=4.0,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(source.x,source.y,c='#FF0000',s=80,marker='o')
plt.scatter(sourceimage.x,sourceimage.y,c='#000000',s=80,marker='^')
plt.axhline(y=0,linewidth=4,color='#000000')

# Creating Vortex Class
class Vortex:
    def __init__(self,strength,x,y):
        self.strength = strength
        self.x,self.y = x,y
    def velocity(self,X,Y):
        self.u = self.strength/(2*pi)*(Y-self.y)/((X-self.x)**2+(Y-self.y)**2)
        self.v = -self.strength/(2*pi)*(X-self.x)/((X-self.x)**2+(Y-self.y)**2)
    def stream(self,X,Y):
        self.psi = self.strength/(4*pi)*np.log((X-self.x)**2+(Y-self.y)**2)

# User inputs for vortex strength and positions
VortexStrength = input('Vortex Strength: ')
xVortex,yVortex = input('Vortex position (x,y): ')

# Calculating vortex characteristics
vortex = Vortex(VortexStrength,xVortex,yVortex)
vortex.velocity(X,Y)
vortex.stream(X,Y)

# Calculating image based on x-axis symmetry
vorteximage = Vortex(-VortexStrength,xVortex,-yVortex)
vorteximage.velocity(X,Y)
vorteximage.stream(X,Y)

# Applying superposition principle
uv = vortex.u + vorteximage.u
vv = vortex.v + vorteximage.v
psiv = vortex.stream + vorteximage.stream

# Plotting combined velocity field
size = 10
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.title('Combined Vortex and Image')
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,uv,vv,density=4.0,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(source.x,source.y,c='#FF0000',s=80,marker='o')
plt.scatter(sourceimage.x,sourceimage.y,c='#000000',s=80,marker='^')
plt.axhline(y=0,linewidth=4,color='#000000')
plt.show()