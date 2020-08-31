import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 7, 500)

ticks = np.arange(0,101, 5)

BC_acc = 0.36
BC_speed = 65
BC_coeff = 0.16
BC_aim_time = 2.59

vstabs_coeff = 0.8
irm_coeff = 0.9
iau_coeff = 0.95
gld_coeff = 0.909


def aimfunc(bloom=1, aimTime=3, accuracy=0.3):
    arr = bloom * np.exp(-t/aimTime)
    result = np.maximum(arr, accuracy)
    return result

def bloomFunc(accuracy=0.3, speed=65, coeff=0.3):
    return accuracy * np.sqrt(1+(speed*coeff)**2)


BC_base_bloom = bloomFunc(BC_acc, BC_speed, BC_coeff)
BC_vstabs_bloom = bloomFunc(BC_acc, BC_speed, vstabs_coeff*BC_coeff)
BC_irm_bloom = bloomFunc(BC_acc, BC_speed, irm_coeff*BC_coeff)
BC_gld_bloom = bloomFunc(BC_acc, BC_speed, BC_coeff)
BC_iau_bloom = bloomFunc(iau_coeff*BC_acc, BC_speed, BC_coeff)


fig, ax = plt.subplots()

ax.plot(t, aimfunc(BC_base_bloom, BC_aim_time, BC_acc), label='Base', linewidth=1.5)
ax.plot(t, aimfunc(BC_vstabs_bloom, BC_aim_time, BC_acc), label='VS', linewidth=1.5)
ax.plot(t, aimfunc(BC_irm_bloom, BC_aim_time, BC_acc), label='IRM', linewidth=1.5)
ax.plot(t, aimfunc(BC_gld_bloom, gld_coeff*BC_aim_time, BC_acc), label='GLD', linewidth=1.5)
ax.plot(t, aimfunc(BC_iau_bloom, BC_aim_time, iau_coeff*BC_acc), label='IAU', linewidth=1.5)

ax.set_xlim([0, 7])
#ax.set_ylim([0.3, 0.5])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('Krupp full speed')
ax.grid(which='major', color='#666666', linestyle='-')
ax.grid(which='minor', color='#ccccff', linestyle='-')
plt.minorticks_on()
ax.legend()

plt.show()
#plt.savefig('smol.png', dpi=600, format='png')





