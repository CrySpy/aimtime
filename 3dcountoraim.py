import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from utils import time

x = np.linspace(1, 6, 1000) #aiming itme
y = np.linspace(1, 20, 1000) #modified dispersion

arr = np.linspace(0,20,21)

X, Y = np.meshgrid(x, y)
Z = time(X, Y)

fig, ax = plt.subplots(1, 1)
cp = ax.contourf(X ,Y, Z, cmap=cm.coolwarm, levels=arr)
cbar = fig.colorbar(cp)
cbar.ax.set_ylabel('Seconds to aim')
cbar.set_ticks(arr)


ax.set_xlabel('aiming time')
#ax.set_xlim(0, 6)
ax.set_ylabel('modified dispersion')
#ax.set_ylim(0,20)



plt.show()
#plt.savefig('contour.png', dpi=600, format='png')

