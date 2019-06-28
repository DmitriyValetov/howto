from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, x)

ax.contourf(X, Y, .1*np.sin(3*X)*np.sin(5*Y))
ax.contourf(X, Y, 3+.1*np.sin(5*X)*np.sin(8*Y))
ax.contourf(X, Y, 7+.1*np.sin(7*X)*np.sin(3*Y))
ax.contourf(X, Y, 8+.1*np.sin(7*X)*np.sin(3*Y))
ax.contourf(X, Y, 9+.1*np.sin(7*X)*np.sin(3*Y))

ax.legend()
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 10)

plt.show()