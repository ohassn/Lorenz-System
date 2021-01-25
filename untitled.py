import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['axes.facecolor'] = 'black'

# constant parameters
roy = 28
sigma = 10
beta = 8/3

# finding a dt value by specifying a certain number of steps and a simulation time
steps = 500000
time = 100
dt = time/steps

# variable which affects animation, higher value > less accurate but faster
fact = 100

# dimension arrays for 2d/3d plots
x = np.zeros(steps)
y = np.zeros(steps)
z = np.zeros(steps)
x[0] = 1
y[0] = 1
z[0] = 1

# utilizing Euler's method to solve these equations
for i in range(steps-1):
    x[i+1] = dt*sigma*(y[i]-x[i]) + x[i]
    y[i+1] = dt*(x[i]*(roy - z[i]) - y[i]) + y[i]
    z[i+1] = dt*(x[i]*y[i] - beta*z[i]) + z[i]

# animation arrays
znew = np.zeros((steps, 2))
xnew = np.zeros((steps, 2))

# placeholder variable to create animation arrays
ss = 0

# creating animation arrays from original arrays (size of arrays depends on fact)
while ss < steps-fact:
    znew[ss, 0] = z[ss]
    znew[ss, 1] = z[ss+fact]
    xnew[ss, 0] = x[ss]
    xnew[ss, 1] = x[ss+fact]
    ss += 1

g = input("1) 2D \n"
          "2) 3D \n"
          "3) Animated ")
    
# 2D:

if g == "1":
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1,1,1)
    fig.set_facecolor((0,0,0))
    ax.plot(x,z, color = 'white', linewidth=0.1)
    #plt.savefig("2d.png",dpi=600)
    plt.show()

# 3D:

if g == "2":
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1,1,1, projection='3d')
    fig.set_facecolor((0,0,0))
    ax.plot(x,y,z, color = 'blue', linewidth=0.1)
    #plt.savefig("3d.png",dpi=600)
    plt.show()

# Animation:

if g == "3":
    plt.figure(figsize=(8,8))
    i = 0
    while i < steps:
        plt.axis((-20,20,0,50))
        plt.plot(xnew[i], znew[i], color='crimson', linewidth=1)
        plt.pause(dt)
        i += fact

