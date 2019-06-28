import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec

delta = 0.025

x = y = np.arange(0, 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = plt.mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = plt.mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = 1e6 * (Z1 * Z2)

fig=plt.figure()

#
# define 2 subplots, using gridspec to control the 
# width ratios:
#
# note: you have to import matplotlib.gridspec for this
#
gs = gridspec.GridSpec(1, 2,width_ratios=[15,1])

# the 1st subplot
ax1 = plt.subplot(gs[0])

lvls = np.logspace(0,4,20)

cm = plt.get_cmap('jet_r')

CF = ax1.contourf(X,Y,Z,
                  norm = LogNorm(),
                  levels = lvls,
                  cmap=cm)
CS = ax1.contour(X,Y,Z,
                 norm = LogNorm(),
                 colors = 'k',
                 levels = lvls
                 )

#
# the pseudo-colorbar
#

# the 2nd subplot
ax2 = plt.subplot(gs[1])        

#
# new levels!
#
# np.logspace gives you logarithmically spaced levels - 
# this, however, is not what you want in your colorbar
#
# you want equally spaced labels for each exponential group:
#
levls = np.linspace(1,10,10)
levls = np.concatenate((levls[:-1],np.linspace(10,100,10)))
levls = np.concatenate((levls[:-1],np.linspace(100,1000,10)))
levls = np.concatenate((levls[:-1],np.linspace(1000,10000,10)))

#
# simple x,y setup for a contourf plot to serve as colorbar
#
XC = [np.zeros(len(levls)), np.ones(len(levls))]
YC = [levls, levls]

CM = ax2.contourf(XC,YC,YC, levels=levls, norm = LogNorm(), cmap=cm)
# log y-scale
ax2.set_yscale('log')  
# y-labels on the right
ax2.yaxis.tick_right()
# no x-ticks
ax2.set_xticks([])

plt.show()