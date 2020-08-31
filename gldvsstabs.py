import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize



x = np.linspace(0,5,1000)



def time(disp, stabs=1, gld=1):
    return np.log(np.sqrt(1+(stabs * disp)**2)) * gld


fig, ax = plt.subplots()

ax.plot(x, time(x), label='BASE')
ax.plot(x, time(x, stabs=0.8), label='VS')
ax.plot(x, time(x, gld=1/1.1), label='GLD')
ax.plot(x, time(x, stabs=0.9), label='IRM')
ax.set_xlabel('Dispersion penalty')
#ax.set_ylabel('Time to aim')
#ax.set_title('3s aiming time')
ax.grid(which='major', color='#666666', linestyle='-')
ax.grid(which='minor', color='#ccccff', linestyle='-')
plt.minorticks_on()
ax.legend()
plt.show()
#plt.savefig('glsvsirm.png', dpi=600, format='png')


def prep(y):
    return time(y, stabs=0.8) - time(y, gld=1/1.1)


#result = optimize.root_scalar(prep, bracket=[0.1, 30])
#print(result)
