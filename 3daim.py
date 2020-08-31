import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(1.5, 6, 1000) #aiming itme
y = np.linspace(2, 20, 1000) #modified dispersion

def time(x, y):
    #return np.log(y)*x
    return np.log(np.sqrt(1+(y)**2)) * x


X, Y = np.meshgrid(x, y)
Z = time(X, Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='z', offset=0, cmap=cm.coolwarm, )
cset = ax.contour(X, Y, Z, zdir='x', offset=0, cmap=cm.coolwarm, )
cset = ax.contour(X, Y, Z, zdir='y', offset=20, cmap=cm.coolwarm, )
ax.set_xlabel('x aiming time')
ax.set_xlim(0, 6)
ax.set_ylabel('y modified dispersion')
ax.set_ylim(0,20)
ax.set_zlabel('z time to aim')

fig.colorbar(surf)
plt.show()
#plt.savefig('3d.png', dpi=600, format='png')

