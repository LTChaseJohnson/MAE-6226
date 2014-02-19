import numpy as np
import matplotlib.pyplot as plt
from math import *

N = 50
xStart,xEnd = -4.0,4.0
yStart,yEnd = -2.0,2.0
x = np.linspace(xStart,xEnd,N)
y = np.linspace(yStart,yEnd,N)
X,Y = np.meshgrid(x,y)

def getvelocityvortex(strength,xv,yv,X,Y):
    u = strength/(2*pi)*(Y-yv)/((X-xv)**2+(Y-yv)**2)
    v = -strength/(2*pi)*(X-xv)/((X-xv)**2+(Y-yv)**2)
    return u,v

def getstreamfunctionvortex(strength,xv,yv,X,Y):
    psi = strength/(4*pi)*np.log((X-xv)**2+(Y-yv)**2)
    return psi

gamma = 5.0
Nv = 10
xVortex = np.linspace(xStart,xEnd,Nv)
yVortex = np.zeros(Nv)
u = np.zeros((N,N))
v = np.zeros((N,N))

for i in range(0,Nv):
    uVortex,vVortex = getvelocityvortex(gamma,xVortex[i],yVortex[i],X,Y)
    psiVortex = getstreamfunctionvortex(gamma,xVortex[i],yVortex[i],X,Y)
    u = u + uVortex
    v = v + vVortex

size = 10
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.title('Finite Vortices')
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,u,v,density=2.0,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(xVortex,yVortex,c='#CD2305',s=80,marker='o')

a = 1
xinfVortex = np.arange(xStart,xEnd,a)
yinfVortex = np.zeros_like(xinfVortex)

def getvelocityinfvortex(strength,xv,yv,X,Y):
    u = strength/(2*a)*np.sinh(2*pi*Y/a)/(np.cosh(2*pi*Y/a)-np.cos(2*pi*X/a))
    v = -strength/(2*a)*np.sin(2*pi*X/a)/(np.cosh(2*pi*Y/a)-np.cos(2*pi*X/a))
    return u,v

uinfVortex,vinfVortex = getvelocityinfvortex(gamma,xinfVortex,yinfVortex,X,Y)

plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.title('Infinite Vortices')
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,uinfVortex,vinfVortex,density=2.0,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(xinfVortex,yinfVortex,c='#CD2305',s=80,marker='o')

gamma = 5.0
Nv = 100
xVortex1 = np.linspace(-50,50,Nv)
yVortex1 = np.zeros(Nv)
u1 = np.zeros((N,N))
v1 = np.zeros((N,N))

for i in range(0,Nv):
    uVortex1,vVortex1 = getvelocityvortex(gamma,xVortex1[i],yVortex1[i],X,Y)
    psiVortex1 = getstreamfunctionvortex(gamma,xVortex1[i],yVortex1[i],X,Y)
    u1 = u1 + uVortex1
    v1 = v1 + vVortex1

size = 10
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.title('Finite Vortices')
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,u1,v1,density=2.0,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(xVortex1,yVortex1,c='#CD2305',s=80,marker='o')


plt.show()