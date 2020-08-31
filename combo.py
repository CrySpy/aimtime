import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Users\\Christoffer\\Documents\\Aimtime tings'

t = np.linspace(0, 10, 500)

BC_acc = 0.58
BC_speed = 45.89
BC_coeff = 0.36
BC_aim_time = 3.45

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
#BC_irm_vstab_bloom = bloomFunc(BC_acc, BC_speed, (irm_coeff+vstabs_coeff-1)*BC_coeff)      #most likely not additive
BC_irm_vstab_bloom = bloomFunc(BC_acc, BC_speed, (irm_coeff+vstabs_coeff-1)*BC_coeff)
BC_gld_vstab_bloom = bloomFunc(BC_acc, BC_speed, vstabs_coeff*BC_coeff)
BC_iau_vstab_bloom = bloomFunc(iau_coeff*BC_acc, BC_speed, vstabs_coeff*BC_coeff)


fig, ax = plt.subplots()

ax.plot(t, aimfunc(BC_base_bloom, BC_aim_time, BC_acc), label='Base', linewidth=1.5)
ax.plot(t, aimfunc(BC_vstabs_bloom, BC_aim_time, BC_acc), label='VSTABS', linewidth=1.5)
#ax.plot(t, aimfunc(BC_irm_vstab_bloom, BC_aim_time, BC_acc), label='IRM + VSTABS', linewidth=1.5)
ax.plot(t, aimfunc(BC_gld_vstab_bloom, gld_coeff*BC_aim_time, BC_acc), label='GLD + VSTABS', linewidth=1.5)
ax.plot(t, aimfunc(BC_iau_vstab_bloom, BC_aim_time, iau_coeff*BC_acc), label='IAU + VSTABS', linewidth=1.5)

ax.set_xlim([0,10])
#ax.set_ylim([0.5, 0.7])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('BatChat full speed')
ax.grid(which='major', color='#666666', linestyle='-')
ax.grid(which='minor', color='#ccccff', linestyle='-')
plt.minorticks_on()
ax.legend()

plt.show()
#plt.savefig('smol2.png', dpi=600, format='png')