import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Users\\Christoffer\\Documents\\Aimtime tings'

t = np.linspace(0, 5.5, 500)

acc = 0.37
#speed = 65
coeff = 3.36
aim_time = 2.01
intra_clip = 2

vstabs_coeff = 0.8
irm_coeff = 0.9
iau_coeff = 0.95
gld_coeff = 1/1.1


def aimfunc(bloom=1, aimTime=3, accuracy=0.3):
    arr = bloom * np.exp(-t/aimTime)
    result = np.maximum(arr, accuracy)
    return result

def bloomFunc(accuracy=0.3, coeff=0.3):
    return accuracy * np.sqrt(1+coeff**2)

base_bloom = bloomFunc(acc, coeff)
vstabs_bloom = bloomFunc(acc, vstabs_coeff*coeff)
irm_bloom = bloomFunc(acc, irm_coeff*coeff)
gld_bloom = bloomFunc(acc, coeff)
iau_bloom = bloomFunc(iau_coeff*acc, coeff)


fig, ax = plt.subplots()

ax.plot(t, aimfunc(base_bloom, aim_time, acc), label='Base', linewidth=1.25)
ax.plot(t, aimfunc(vstabs_bloom, aim_time, acc), label='VSTABS', linewidth=1.25)
ax.plot(t, aimfunc(irm_bloom, aim_time, acc), label='IRM', linewidth=1.25)
ax.plot(t, aimfunc(gld_bloom, gld_coeff*aim_time, acc), label='GLD', linewidth=1.25)
ax.plot(t, aimfunc(iau_bloom, aim_time, iau_coeff*acc), label='IAU', linewidth=1.25)
plt.axvline(x=intra_clip)

ax.set_xlim([0,5.5])
#ax.set_ylim([0.3, 0.5])
ax.set_xlabel('t time[s]')
ax.set_ylabel('y aim circle radius[m]')
ax.set_title('T71 after firing')
ax.grid()
ax.legend()

plt.show()
#plt.savefig('big2.png', dpi=600, format='png')